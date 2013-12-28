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

from mock import Mock, call, patch

from dissect.modeling.static.driver import Driver as StaticDriver
from dissect.test.object_factory import fake, real, unique


class TestDriver():
    def setUp(self):
        self.patcher = patch('dissect.modeling.static.driver.Orchestrator')
        self.orchestrator_mock = Mock()
        self.orchestrator_class = self.patcher.start()
        self.orchestrator_class.return_value = self.orchestrator_mock

        self.file_set = fake('FileSet')
        self.observer = Mock()
        self.static_driver = StaticDriver(self.file_set)

    def tearDown(self):
        self.patcher.stop()

    def test_it_models_data_from_each_file(self):
        # Arrange
        self.file_set.__iter__.return_value = ['a.py', 'path/to/b.py']

        # Act
        self.static_driver.run()

        # Assert
        self.orchestrator_mock.process.assert_called_once_with(['a.py', 'path/to/b.py'])
