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
import time


class CallsPerTimePeriod(object):
    '''
    Decorate a 'call handler' discarding functions calls that exceed a maximum
    call rate.
    '''

    def __init__(self, calls_per_period, period, call_handler):
        self.calls_per_period = calls_per_period
        self.period = period
        self.call_handler = call_handler
        self.call_count = {}
        flusher_thread = threading.Thread(target=self._flusher_thread)
        flusher_thread.setDaemon(True)
        flusher_thread.start()

    def on_call(self, frame_digest):
        func_name = frame_digest.function_name
        try:
            if self.call_count[func_name] >= self.calls_per_period:
                return False
            else:
                self.call_count[frame_digest.function_name] += 1
        except KeyError:
            self.call_count[frame_digest.function_name] = 1

        self.call_handler.on_call(frame_digest)
        return True

    def _flusher_thread(self):
        while True:
            time.sleep(self.period)
            self._flush()

    def _flush(self):
        self.call_count = {}
