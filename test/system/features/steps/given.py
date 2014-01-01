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

import os
from nose.tools import assert_false


@given(u'my program has modules aa, ab, ba, bb')
@given(u'my program has modules aa_func, ab_func, ba_func, bb_func')
@given(u'my program calls functions aa_func, ab_func, ba_func, bb_func')
def step_impl(context):
    assert_false(hasattr(context, 'program_path'))
    context.program_path = os.path.abspath(
        os.path.join('test', 'system', 'data', 'four_modules', 'main.py'))
