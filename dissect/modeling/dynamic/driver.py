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

from dissect.collection.dynamic.filter.calls_per_time_period import \
    CallsPerTimePeriod

from dissect.collection.dynamic.filter.project_modules import \
                                                         ProjectModules
from dissect.collection.dynamic.thread_scoped_tracer import ThreadScopedTracer
from dissect.modeling.dynamic.function_call import FunctionCall \
                                                          as FunctionCallModeler
from dissect.modeling.static.function import Function as FunctionModeler
from dissect.modeling.static.module import Module as ModuleModeler
from dissect.modeling.static.class_ import Class_ as ClassModeler
from dissect.modeling.orchestrator import AlreadyProcessed


class Driver(object):
    def __init__(self, observer, entity_id_generator, orchestrator):
        self.observer = observer
        self.orchestrator = orchestrator

        self.function_call_modeler = FunctionCallModeler(entity_id_generator,
                                                         orchestrator.model)

        self._setup_static_data_modeling()

        one_call_per_second_filter = CallsPerTimePeriod(1, 1, self)

        project_modules_filter = ProjectModules(entity_id_generator.base_path,
                                                one_call_per_second_filter)

        self.thread_scoped_tracer = ThreadScopedTracer(project_modules_filter)
        self.stop = self.thread_scoped_tracer.stop

    def start(self):
        self.thread_scoped_tracer.start()

    def on_call(self, frame_digest):
        # I wonder what this is...
        if frame_digest.function_name == '<module>':
            return

        self._model_static_entities_from(frame_digest.file_name)
        function_call = self.function_call_modeler.on_call(frame_digest)
        self.observer.on_call(function_call)
        return True

    def _setup_static_data_modeling(self):
        self.orchestrator.include(ModuleModeler)
        self.orchestrator.include(ClassModeler)
        self.orchestrator.include(FunctionModeler)

    def _model_static_entities_from(self, file_name):
        try:
            self.orchestrator.process(file_name)
        except AlreadyProcessed:
            pass
