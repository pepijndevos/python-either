# python-either
# Homepage: https://github.com/kennknowles/python-either
#
# Copyright 2012- Kenneth Knowles
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class Either(object):
    __slots__ = ['value']
    def __bool__(self):
        # by convention Right contains
        # the right = correct = truthy value
        return isinstance(self, Right)

class Left(Either):
    __slots__ = ['value']
    def __init__(self, v): self.value = v

class Right(Either):
    __slots__ = ['value']
    def __init__(self, v): self.value = v


class Maybe(object):
    __slots__ = ['value']
    def __bool__(self):
        return isinstance(self, Just)

class Nothing(Maybe):
    __slots__ = []
    @property
    def value(self): raise AttributeError('Nothing has no value')

class Just(Maybe):
    __slots__ = ['value']
    def __init__(self, v): self.value = v
