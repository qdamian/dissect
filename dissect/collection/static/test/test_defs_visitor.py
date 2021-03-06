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

from dissect.collection.static.defs_visitor import DefsVisitor
from dissect.test.object_factory import fake

class TestDefsVisitor():

    def test_function_notifications_are_suitable_for_the_function_defs_collector(self):
        # Arrange
        function_def_collector = fake('FunctionModeler')
        node = fake('NodeNG')
        defs_visitor = DefsVisitor([function_def_collector])

        # Act
        defs_visitor.visit_function(node)

        # Assert
        function_def_collector.on_function.assert_called_once_with(node)
