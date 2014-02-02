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

from mock import patch, Mock, ANY
from nose.tools import *
from dissect.collection.static.source_code_parser import SourceCodeParser


class TestSourceCodeParser():

    def setUp(self):
        self.ast_ng_manager_patcher = patch('dissect.collection.static.source_code_parser.AstroidManager')
        self.ast_ng_manager_mock = Mock()
        self.ast_ng_manager_class_mock = self.ast_ng_manager_patcher.start()
        self.ast_ng_manager_class_mock.return_value = self.ast_ng_manager_mock
        self.os_patcher = patch('dissect.collection.static.source_code_parser.os')
        self.os_patcher.start()

    def tearDown(self):
        patch.stopall()

    @patch('dissect.collection.static.source_code_parser.sys')
    def test_adds_base_path_to_top_of_python_path(self, sys_mock):
        # Act
        SourceCodeParser('fake_base_path')

        # Assert
        sys_mock.path.insert.assert_called_once_with(0, 'fake_base_path')

    def test_creates_project_from_file_paths(self):
        # Arrange
        file_paths = ['path/to/a.py', 'path/to/b.py']
        source_code_parser = SourceCodeParser('.')
        source_code_parser.add_files(file_paths)

        # Act
        source_code_parser.parse()

        # Assert
        self.ast_ng_manager_mock.project_from_files.assert_called_once_with(file_paths, func_wrapper=ANY)

    def test_add_files_accepts_a_single_file(self):
        # Arrange
        file_path = 'path/to/a/single/file.py'
        source_code_parser = SourceCodeParser('.')

        # Act
        source_code_parser.add_files(file_path)
        source_code_parser.parse()

        # Assert
        self.ast_ng_manager_mock.project_from_files.assert_called_once_with([file_path], func_wrapper=ANY)

    @patch('dissect.collection.static.source_code_parser.RelationsVisitor')
    @patch('dissect.collection.static.source_code_parser.DefsVisitor')
    def test_visits_definitions_and_relations(self, defs_visitor_class_mock, relations_visitor_class_mock):
        # Arrange
        defs_visitor_mock = Mock()
        defs_visitor_class_mock.return_value = defs_visitor_mock
        relations_visitor_mock = Mock()
        relations_visitor_class_mock.return_value = relations_visitor_mock
        source_code_parser = SourceCodeParser('.')
        source_code_parser.add_files('dummy/path.py')

        # Act
        source_code_parser.parse()

        # Assert
        defs_visitor_mock.visit.assert_called_once_with(ANY)
        relations_visitor_mock.visit.assert_called_once_with(ANY)

    def test_add_files_returns_true_if_at_least_one_file_was_added(self):
        # Arrange
        paths1 = ['path/to/a.py', 'path/to/b.py']
        paths2 = ['path/to/b.py', 'path/to/c.py']
        source_code_parser = SourceCodeParser('.')
        source_code_parser.add_files(paths1)

        # Act
        result = source_code_parser.add_files(paths2)

        # Assert
        assert_true(result)

    def test_add_files_returns_false_no_file_was_added(self):
        # Arrange
        paths1 = ['path/to/a.py', 'path/to/b.py']
        paths2 = ['path/to/b.py']
        source_code_parser = SourceCodeParser('.')
        source_code_parser.add_files(paths1)

        # Act
        result = source_code_parser.add_files(paths2)

        # Assert
        assert_false(result)

    def test_if_only_add_files_that_exist(self):
        with patch('dissect.collection.static.source_code_parser.os.path.isfile',
                   new=Mock(side_effect=lambda f: f == 'file-which-exists')):
            # Given
            parser = SourceCodeParser('.')

            # When
            parser.add_files(['file-which-exists', 'file-which-does-not-exist'])
            parser.parse()

            # Then
            self.ast_ng_manager_mock.project_from_files.assert_called_once_with(
                ['file-which-exists'], func_wrapper=ANY)