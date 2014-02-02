#region GPLv3 notice
# Copyright 2014 Damian Quiroga
#
# This file is part of dissect.
#
# dissect is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# dissect is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dissect.  If not, see <http://www.gnu.org/licenses/>.
#endregion

import threading
from Queue import Queue

from dissect.consolidation.util.json_to_entity import JsonToEntity


class AsyncPublisher(object):

    def __init__(self, callback):
        self.queue = Queue()
        self.callback = callback
        self._stop_sentinel = None
        self.json_to_entity = JsonToEntity()

    def start(self):
        self.thread = threading.Thread(target=self._process_queue)
        self.thread.setDaemon(True)
        self.thread.start()

    def on_entity(self, entity):
        self.queue.put(entity)

    def stop(self):
        self.queue.put_nowait(self._stop_sentinel)
        self.thread.join()

    def _process_queue(self):
        while True:
            try:
                entity = self.queue.get()
                if entity is self._stop_sentinel:
                    return
                self.callback(entity)
            except KeyError:
                pass
