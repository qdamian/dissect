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

import sys
import threading
from dissect.collection.dynamic.thread_scoped_tracer import ThreadScopedTracer


class ProcessScopedTracer(object):
    def __init__(self, call_handler):
        self.call_handler = call_handler
        self.stop = self.__stop_trace__

    def start(self):
        threading.settrace(self._set_trace)
        self._install_tracer()

    def __stop_trace__(self):
        sys.settrace(None)
        threading.settrace(None)

    # pylint: disable=unused-argument
    def _set_trace(self, frame, event, _):
        self._install_tracer()

    def _install_tracer(self):
        ThreadScopedTracer(self.call_handler).start()
