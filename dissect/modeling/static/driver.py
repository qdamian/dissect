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

from dissect.modeling.static.class_ import Class_
from dissect.modeling.orchestrator import Orchestrator
from dissect.modeling.static.function import Function
from dissect.modeling.static.module import Module
from dissect.model.model import Model

class Driver(object):
    def __init__(self, file_set):
        self.file_set = file_set
        self.model = Model()

    def run(self):
        print 'Static driver run called'
        orchestrator = Orchestrator(self.file_set.directory, self.model)
        orchestrator.include(Module)
        orchestrator.include(Class_)
        orchestrator.include(Function)

        file_list = [f for f in self.file_set]

        orchestrator.process(file_list)

        return self.model
