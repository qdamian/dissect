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

from astroid.utils import LocalsVisitor
from dissect.collection.static.notifier import best_effort_notify

class DefsVisitor(LocalsVisitor):
    '''
    Visit the project notifying the observers about (some types of) definitions
    found. Nodes that define a relation between entities are not notified.
    '''
    def __init__(self, observers):
        LocalsVisitor.__init__(self)
        self.observers = observers

    def visit_module(self, node):
        best_effort_notify(self.observers, 'on_module', node)

    def visit_class(self, node):
        best_effort_notify(self.observers, 'on_class', node)

    def visit_function(self, node):
        best_effort_notify(self.observers, 'on_function', node)
