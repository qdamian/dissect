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

from dissect.model.entity.entity import Entity
from dissect.model.entity.function import Function

class Method(Function):
    '''Represent a class method'''

    __metaclass__ = Entity

    def __init__(self, id_=None, name=None, class_=None):
        super(Method, self).__init__(id_, name, class_)
        self.class_ = class_

    def __repr__(self):
        return str(self.__dict__)
