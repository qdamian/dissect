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

from dissect.consolidation.async_publisher import AsyncPublisher
from dissect.test.object_factory import fake
from mock import Mock, call


class TestAsyncPublisher(object):
    def test_it_invokes_the_callback_for_one_entity(self):
        # Given
        callback = Mock()
        fake_entity = fake('Function')
        async_publisher = AsyncPublisher(callback)
        async_publisher.start()

        # When
        async_publisher.on_entity(fake_entity)
        async_publisher.stop()

        # Then
        callback.assert_called_once_with(fake_entity)

    def test_it_invokes_the_callback_for_two_entities(self):
        # Given
        callback = Mock()
        fake_class = fake('Class_')
        fake_function = fake('Function')
        async_publisher = AsyncPublisher(callback)
        async_publisher.start()

        # When
        async_publisher.on_entity(fake_class)
        async_publisher.on_entity(fake_function)
        async_publisher.stop()

        # Then
        callback.assert_has_calls([call(fake_class),
                                   call(fake_function)])

    def test_on_entity_returns_before_the_callback_completes(self):
        # Given
        finish = threading.Event()
        callback = Mock()
        callback.side_effect = lambda entity: finish.wait()
        fake_entity = fake('Function')
        async_publisher = AsyncPublisher(callback)
        async_publisher.start()

        # When
        async_publisher.on_entity(fake_entity)
        finish.set()

        # Then
        async_publisher.stop()