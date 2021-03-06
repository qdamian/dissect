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

'''
This module creates instances of some classes (from dissect and other
libraries) that serve as 'templates' to create other instance objects. These
objects created from the templates are meant to be used as sample data or
mocks in unit tests. They can be either real instances (deep copies of the
template objects) or mock objects (generated using Mock's autospeccing).

http://www.voidspace.org.uk/python/mock/helpers.html#autospeccing
'''

from copy import deepcopy
import inspect
import uuid

from astroid.bases import NodeNG
from formic.formic import FileSet
from mock import create_autospec, Mock, MagicMock

from dissect.consolidation.async_publisher import AsyncPublisher
from dissect.model.entity.function_call import FunctionCall
from dissect.collection.static.source_code_parser import SourceCodeParser
from dissect.consolidation.observable_model import ObservableModel
from dissect.collection.dynamic.frame_digest import FrameDigest
from dissect.collection.dynamic.process_scoped_tracer import ProcessScopedTracer
from dissect.collection.dynamic.thread_scoped_tracer import ThreadScopedTracer
from dissect.model.entity.class_ import Class_
from dissect.model.entity.function import Function
from dissect.model.entity.method import Method
from dissect.model.entity.module import Module
from dissect.model.entity.thread import Thread
from dissect.model.model import Model
from dissect.model.util.entity_id_generator import EntityIdGenerator
from dissect.model.util.entity_repo import EntityRepo
from dissect.modeling.orchestrator import Orchestrator
from dissect.modeling.static.driver import Driver as StaticModelingDriver
from dissect.modeling.dynamic.driver import Driver as DynamicModelingDriver
from dissect.modeling.static.class_ import Class_ as ClassModeler
from dissect.modeling.static.function import Function as FunctionModeler
from dissect.modeling.dynamic.thread import Thread as ThreadModeler
from dissect.modeling.dynamic.process import Process as ProcessModeler


def fake(class_name, spec_set=True):
    return create_autospec(spec=globals()['__' + class_name], spec_set=spec_set)

def real(class_name):
    return deepcopy(globals()['__' + class_name])

def unique(entity):
    entity.id_ = str(uuid.uuid4())
    return entity

__base_path = '.'
__SourceCodeParser = SourceCodeParser(__base_path)
__EntityIdGenerator = EntityIdGenerator(__base_path)
__Model = Model()
__Module = Module('module_id', 'module_name')
__NodeNG = NodeNG()
__Orchestrator = Orchestrator(__base_path, __Model)
__Thread = Thread('thread_id')
__EntityRepo = EntityRepo()
__ProcessScopedTracer = ProcessScopedTracer(MagicMock())
__ThreadScopedTracer = ThreadScopedTracer(MagicMock())
__FrameDigest = FrameDigest(inspect.currentframe())
__Class_ = Class_('class_id', 'class_name', __Module)
__FileSet = FileSet(directory=__base_path, include='*.py')
__Function = Function('function_id', 'function_name', __Module)
__Method = Method('method_id', 'method_name', __Class_)
__ClassModeler = ClassModeler(__SourceCodeParser, __EntityIdGenerator, __Model)
__FunctionModeler = FunctionModeler(__SourceCodeParser, __EntityIdGenerator, __Model)
__StaticModelingDriver = StaticModelingDriver(__FileSet)
__DynamicModelingDriver = DynamicModelingDriver(MagicMock(), __EntityIdGenerator, __Orchestrator)
__FunctionCall = FunctionCall('function_call_id', __Function, __Thread)
__ThreadModeler = ThreadModeler(__EntityIdGenerator, __Model)
__ProcessModeler = ProcessModeler(__EntityIdGenerator, __Model)
__AsyncPublisher = AsyncPublisher(Mock())
__ObservableModel = ObservableModel(__AsyncPublisher)
