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

from mock import patch, call
from nose.tools import assert_equal

from dissect.modeling.dynamic.process import Process
from dissect.test.object_factory import fake, unique


@patch('dissect.modeling.dynamic.process.threading')
@patch('dissect.modeling.dynamic.process.Thread')
class TestProcess(object):
    def test_it_creates_a_thread_modeler_for_the_main_thread(self,
                                                    thread_modeler,
                                                    threading):
        # Arrange
        process_modeler = Process('fake_entityid_gen',
                                                'fake_model')

        # Act
        threading.current_thread.return_value.name = 'MainThread'
        process_modeler.on_call(fake('FrameDigest'))

        # Assert
        thread_modeler.assert_called_once_with('fake_entityid_gen',
                                                         'fake_model')


    def test_it_passes_the_frame_digest_to_the_thread_modeler(self,
                                    thread_modeler, threading):
        # Arrange
        process_modeler = Process('fake_entityid_gen',
                                                'fake_model')

        # Act
        fake_frame_digest = fake('FrameDigest')
        threading.current_thread.return_value.name = 'MainThread'
        process_modeler.on_call(fake_frame_digest)

        # Assert
        thread_modeler.return_value.on_call.assert_called_once_with(
            fake_frame_digest)


    def test_it_passes_all_calls_from_the_same_thread_to_the_same_modeler(self,
                                        thread_modeler, threading):
        # Arrange
        process_modeler = Process('fake_entityid_gen',
                                                'fake_model')

        fake_frame_digest_1 = fake('FrameDigest')
        fake_frame_digest_2 = fake('FrameDigest')
        threading.current_thread.return_value.name = 'MainThread'

        # Act
        process_modeler.on_call(fake_frame_digest_1)
        process_modeler.on_call(fake_frame_digest_2)

        # Assert
        thread_modeler.return_value
        assert_equal(thread_modeler.call_count, 1)
        expected_calls = [call(fake_frame_digest_1), call(fake_frame_digest_2)]
        modeler = thread_modeler.return_value
        modeler.on_call.assert_has_calls(expected_calls)

    def test_it_passes_all_calls_from_the_same_thread_to_the_same_modeler(self,
                                         thread_modeler, threading):
        # Arrange
        process_modeler = Process('fake_entityid_gen',
                                                'fake_model')

        fake_frame_digest_1 = fake('FrameDigest')
        fake_frame_digest_2 = fake('FrameDigest')

        # Act
        threading.current_thread.return_value.name = 'MainThread'
        process_modeler.on_call(fake_frame_digest_1)
        threading.current_thread.return_value.name = 'Thread-1'
        process_modeler.on_call(fake_frame_digest_2)

        # Assert
        thread_modeler.return_value
        assert_equal(thread_modeler.call_count, 2)
        #expected_calls = [call(fake_frame_digest_1), call(fake_frame_digest_2)]
        #modeler = thread_modeler.return_value
        #modeler.on_call.assert_has_calls(expected_calls)
