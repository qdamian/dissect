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

import os


class ProjectModules(object):
    '''
    Decorate a 'call handler' proxying function calls to functions of the
    project's modules and discarding functions to functions of external
    libraries.
    '''
    def __init__(self, base_path, call_handler):
        self.base_path = base_path
        self.call_handler = call_handler

    def on_call(self, frame_digest):
        rel_path = os.path.relpath(frame_digest.file_name,
                                   os.path.dirname(self.base_path))
        if not rel_path.startswith('..'):
            return self.call_handler.on_call(frame_digest)
        return False
