#region GPLv3 notice
# Copyright 2013 Damian Quiroga
#
# This file is part of depict.
#
# depict is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# depict is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with depict.  If not, see <http://www.gnu.org/licenses/>.
#endregion

import threading
from dissect.modeling.dynamic.thread import Thread


class Process(object):
    def __init__(self, entity_id_generator, model):
        self.entity_id_gen = entity_id_generator
        self.model = model
        self.thread = None
        self.threads = {}

    def on_call(self, frame_digest):
        thread_name = threading.current_thread().name
        if not thread_name in self.threads:
            self.threads[thread_name] = Thread(self.entity_id_gen,
                                                        self.model)
        self.threads[thread_name].on_call(frame_digest)

