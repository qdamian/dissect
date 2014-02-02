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

from dissect.consolidation.async_publisher import AsyncPublisher
from dissect.model.util.entity_id_generator import EntityIdGenerator
from dissect.modeling.dynamic.driver import Driver \
                                           as DynamicModelingDriver
from dissect.consolidation.observable_model import ObservableModel
from dissect.modeling.orchestrator import Orchestrator
from dissect.model.entity.module import Module
from contextlib import contextmanager
import logging
import sys
import os

class Trace(object):
    def __init__(self, base_path, callback):
        self.async_publisher = AsyncPublisher(callback)
        self.model = ObservableModel(self.async_publisher)

        entity_id_generator = EntityIdGenerator(base_path)
        modeling_orchestrator = Orchestrator(base_path, self.model)
        self.dynamic_modeling_driver = DynamicModelingDriver(self,
                                                     entity_id_generator,
                                                     modeling_orchestrator)

    def start(self):
        self.async_publisher.start()
        self.dynamic_modeling_driver.start()

    def stop(self):
        self.dynamic_modeling_driver.stop()
        self.async_publisher.stop()

def run(filepath, callback):
    root_path = os.path.dirname(filepath)
    sys.path = [root_path] + sys.path
    globals_namespace = {'__file__': filepath,
                         '__name__': '__main__',
                         '__package__': None,
                         '__cached__': None
                        }
    with trace(root_path, callback):
        execfile(filepath, globals_namespace)

@contextmanager
def trace(root_path, callback):
    trace = Trace(root_path, callback)
    try:
        trace.start()
        yield
    finally:
        trace.stop()
