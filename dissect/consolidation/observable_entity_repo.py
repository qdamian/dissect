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

from dissect.model.util.entity_repo import EntityRepo

class ObservableEntityRepo(EntityRepo):
    def __init__(self, observer):
        self.observer = observer
        super(ObservableEntityRepo, self).__init__()

    def add(self, entity):
        if entity.id_ in self.elements_by_id:
            return

        super(ObservableEntityRepo, self).add(entity)
        self.observer.on_entity(entity)
