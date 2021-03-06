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
import os

from astroid.exceptions import AstroidBuildingException
from astroid.manager import AstroidManager

from dissect.collection.static.defs_visitor import DefsVisitor
from dissect.collection.static.relations_visitor import RelationsVisitor
from dissect.model.util.entity_id_generator import EntityIdGenerator


class SourceCodeParser(object):
    '''
    Parse source files using Astroid and notify definitions and relations to
    modeler objects.

    The source files to parse are specified by the user of this class by passing
    a "base path" on construction (root of the program to be analyzed) and
    relative paths to the source files later.
    '''

    def __init__(self, base_path):
        self.file_paths = set()
        self.modelers = set()
        self.entity_id_gen = EntityIdGenerator(base_path)
        # For ASTNManager:
        sys.path.insert(0, base_path)

    def add_files(self, paths):
        '''Try to add the given path(s). Return True if at least one path was
           added, False otherwise'''
        if not isinstance(paths, list):
            paths = [paths]

        paths = [path for path in paths if os.path.isfile(path)]

        len_before = len(self.file_paths)
        self.file_paths.update(paths)
        return len(self.file_paths) != len_before

    def register(self, modeler):
        self.modelers.update([modeler])

    def parse(self):
        manager = AstroidManager()
        project = manager.project_from_files(list(self.file_paths),
                            func_wrapper=astroid_ignore_modname_wrapper)

        # First collect all definitions (e.g. module X, function foo) before
        # trying to relate one definition with another (e.g. module X depends on
        # module Y)
        DefsVisitor(self.modelers).visit(project)
        RelationsVisitor(self.modelers).visit(project)

def astroid_ignore_modname_wrapper(func, modname):
    '''A no-op decorator that must be passed to AstroidManager to override its
       default behavior which is to print the module names to stdout'''
    try:
        return func(modname)
    except AstroidBuildingException, exc:
        print exc
    except Exception, exc:
        import traceback
        traceback.print_exc()
