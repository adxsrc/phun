# Copyright 2022 Chi-kwan Chan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Unit tests for `phun.partial()`"""


from phun.helper import istreeof


def test_istreeof1():

    assert     istreeof('a', str)
    assert not istreeof('a', int)

def test_istreeof2():

    assert     istreeof(('a', 'b'), str)
    assert not istreeof(('a', 'b'), int)

    assert not istreeof(('a', 456), str)
    assert not istreeof(('a', 456), int)

    assert     istreeof((123, 456), int)
    assert     istreeof((123, 456), int)

    assert     istreeof(('a', 'b'), (int, str))
    assert     istreeof(('a', 456), (int, str))
    assert     istreeof((123, 456), (int, str))

def test_istreeof3():

    assert     istreeof(( 'a', ('b',  'c')), str)
    assert     istreeof((('a',  'b'), 'c' ), str)
    assert not istreeof(( 'a', ('b',  'c')), int)
    assert not istreeof((('a',  'b'), 'c' ), int)

    assert not istreeof(( 123, (456,  789)), str)
    assert not istreeof(((123,  456), 789 ), str)
    assert     istreeof(( 123, (456,  789)), int)
    assert     istreeof(((123,  456), 789 ), int)
