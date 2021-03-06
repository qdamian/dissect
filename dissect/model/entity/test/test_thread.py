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

from nose.tools import *

from dissect.model.entity.thread import Thread


class TestFunction():
    def test_creation(self):
        thread = Thread('fake_thread_id')
        assert_equal(thread.id_, 'fake_thread_id')
        assert_equal(thread.name, 'fake_thread_id')

    def test_equal_comparison(self):
        thread1 = Thread('fake_thread_id')
        thread2 = Thread('fake_thread_id')
        assert_equal(thread1, thread2)
