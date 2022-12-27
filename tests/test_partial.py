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


from phun import partial


def f(a, b, c=3, d=4):
    return a, b, c, d


def test_partial0():
    g = partial(f, {})
    assert g(1,2) == (1,2,3,4)

def test_partial1():
    g1 = partial(f, {0:1})
    assert g1(2) == (1,2,3,4)

def test_partial2():
    g1 = partial(f, {1:2})
    assert g1(1) == (1,2,3,4)

def test_partial3():
    g1 = partial(f, {0:1, 1:2})
    assert g1() == (1,2,3,4)


def test_partial4():
    g1 = partial(f, {})
    assert g1(1,2) == (1,2,3,4)

def test_partial5():
    g1 = partial(f, {'c':30})
    assert g1(1,2) == (1,2,30,4)

def test_partial6():
    g1 = partial(f, {'d':40})
    assert g1(1,2) == (1,2,3,40)

def test_partial7():
    g1 = partial(f, {'c':30, 'd':40})
    assert g1(1,2) == (1,2,30,40)


def test_partial8():
    g1 = partial(f, {'c':30, 'd':40})
    assert g1(1,2) == (1,2,30,40)

def test_partial9():
    g1 = partial(f, {'c':30, 'd':40})
    assert g1(1,2,c=3) == (1,2,3,40)

def test_partial10():
    g1 = partial(f, {'c':30, 'd':40})
    assert g1(1,2,d=4) == (1,2,30,4)

def test_partial11():
    g1 = partial(f, {'c':30, 'd':40})
    assert g1(1,2,c=3,d=4) == (1,2,3,4)
