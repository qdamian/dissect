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

from dissect.model.util.entity_id_generator import EntityIdGenerator
from dissect.collection.static.source_code_parser import SourceCodeParser

class AlreadyProcessed(Exception):
    pass

class Orchestrator(object):
    def __init__(self, base_path, model):
        self.model = model
        self.entity_id_generator = EntityIdGenerator(base_path)
        self.source_code_parser = SourceCodeParser(base_path)

    def include(self, modeler):
        modeler(self.source_code_parser,
                self.entity_id_generator,
                self.model)

    def process(self, file_paths):
        assert file_paths
        if not self.source_code_parser.add_files(file_paths):
            raise AlreadyProcessed(file_paths)

        self.source_code_parser.parse()
