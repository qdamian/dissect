#region GPLv3 notice
# Copyright 2013 Damian Quiroga
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

from nose_parameterized import parameterized
from nose.tools import assert_equal
from mock import Mock

from dissect.consolidation.observable_entity_repo import ObservableEntityRepo
from dissect.test.object_factory import real


class TestObservableEntityRepo():

    @parameterized.expand([('Module',),
                           ('Class_',),
                           ('Function',),
                           ('Thread',),
                           ('FunctionCall',)])
    def test_add_still_works(self, entity_class):
        # Arrange
        observable_repo = ObservableEntityRepo(Mock())
        entity = real(entity_class)

        # Act
        observable_repo.add(entity)

        # Assert
        assert_equal(observable_repo.get_by_id(entity.id_), entity)

    @parameterized.expand([('Module'),
                           ('Class_'),
                           ('Function'),
                           ('Thread'),
                           ('FunctionCall')])
    def test_it_notifies_when_one_entity_is_added(self, entity_class):
        # Arrange
        observer = Mock()
        repo = ObservableEntityRepo(observer)
        entity = real(entity_class)

        # Act
        repo.add(entity)

        # Assert
        observer.on_entity.assert_called_once_with(entity)

    def test_it_does_not_notify_if_an_entity_is_added_again(self):
        # Arrange
        observer = Mock()
        repo = ObservableEntityRepo(observer)
        module = real('Module')

        # Act
        repo.add(module)
        repo.add(module)

        # Assert
        observer.on_entity.assert_called_once_with(module)
