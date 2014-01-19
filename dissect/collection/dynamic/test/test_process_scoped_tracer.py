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

from nose.tools import *
from mock import Mock, call, patch

from dissect.collection.dynamic.process_scoped_tracer import ProcessScopedTracer


def function1():
    return 1

def function2(arg):
    return arg

class TestProcessScopedTracer():
    def setUp(self):
        self.original_tracer = sys.gettrace()

    def tearDown(self):
        sys.settrace(self.original_tracer)
        threading.settrace(self.original_tracer)

    def test_it_notifies_a_function_call_in_the_current_thread(self):
        # Arrange
        call_handler = Mock()
        process_scoped_tracer = ProcessScopedTracer(call_handler)

        # Act
        process_scoped_tracer.start()
        function1()
        process_scoped_tracer.stop()

        # Assert
        assert_equal(call_handler.on_call.call_count, 1)
        assert_in('function1', [call[0][0].function_name for call in call_handler.on_call.call_args_list])

    def test_it_notifies_a_function_call_in_a_new_thread(self):
        # Arrange
        call_handler = Mock()
        process_scoped_tracer = ProcessScopedTracer(call_handler)

        # Act
        process_scoped_tracer.start()
        new_thread = threading.Thread(target=function1)
        new_thread.start()
        new_thread.join()
        process_scoped_tracer.stop()

        # Assert
        assert_in('function1', [call[0][0].function_name for call in call_handler.on_call.call_args_list])
