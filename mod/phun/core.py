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


from functools import wraps

from .helper import *


def partial(f, params={}):
    """An Improved Version of `functools.partial()`"""

    fargs = get_argnames(f)
    fkeys = get_keywords(f)

    pargs   = {}
    pkwargs = {}
    for k, v in params.items():
        if isinstance(k, int):
            pargs[k] = v
        elif isinstance(k, str):
            pkwargs[k] = v
        else:
            raise ValueError(
                f'Do not know how to interpret key {k} for `args` or `kwargs`')

    assert len(pargs)   <= len(fargs)
    assert set(pkwargs) <= set(fkeys)

    n = len(fargs)

    @wraps(f)
    def p(*args, **kwargs): # closure on `pargs`, `pkwargs`, and `n`
        assert len(args) + len(pargs) == n
        args = list(args)
        args = tuple(params[i] if i in params else args.pop(0) for i in range(n))
        kwargs = {**pkwargs, **kwargs}
        return f(*args, **kwargs)

    return p


def phun(mkf):
    """Physics Aware Function Generator Transformer

    ``phun`` is a decorator that transforms a restricted physics aware
    function generator ``mkf()`` into a more flexible function
    generator ``mkph()``.

    """

    @wraps(mkf)
    def mkph(*args, **kwargs):
        u = get_default(kwargs, 'u_res',   mkf)
        b = get_default(kwargs, 'backend', mkf)

        kwargs['backend'] = get_backend(b)

        ph = mkf(*args, **kwargs)
        ph.unit = u
        return ph

    return mkph
