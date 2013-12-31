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

from dissect.consolidation.data_sink import EntityDataSink
from dissect.model.util.entity_id_generator import EntityIdGenerator
from dissect.modeling.dynamic.driver import Driver \
                                           as DynamicModelingDriver
from dissect.consolidation.data_source import DataSource
from dissect.consolidation.observable_model import ObservableModel
from dissect.modeling.orchestrator import Orchestrator
from dissect.model.entity.module import Module
import logging
import Queue
import sys
import os

class Trace(object):
    def __init__(self, base_path, callback):
        queue = Queue.Queue()
        data_source = DataSource(queue)
        self.model = ObservableModel(data_source)
        self.data_sink = EntityDataSink(queue, self)

        entity_id_generator = EntityIdGenerator(base_path)
        modeling_orchestrator = Orchestrator(base_path, self.model)
        self.dynamic_modeling_driver = DynamicModelingDriver(self,
                                                     entity_id_generator,
                                                     modeling_orchestrator)
        self.callback = callback

    def handle(self, entity):
        self.callback(entity)

    def start(self):
        self.data_sink.start()
        self.dynamic_modeling_driver.start()

    def stop(self):
        self.dynamic_modeling_driver.stop()
        self.data_sink.stop()

def run(filepath, callback):
    dir_path = os.path.dirname(filepath)
    sys.path = [dir_path] + sys.path
    trace = Trace(dir_path, callback)
    trace.start()
    globals_namespace = {'__file__': filepath,
                         '__name__': '__main__',
                         '__package__': None,
                         '__cached__': None
                        }
    execfile(filepath, globals_namespace)
    trace.stop()
