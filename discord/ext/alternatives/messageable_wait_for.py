"""
    Copyright 2020 Ext-Creators

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from discord.abc import Messageable
from discord.message import Message


def wait_for(self, event, *, check=None, timeout=None):
    actual_wait_for = self._state.dispatch.__self__.wait_for

    if check is None:
        def check(*args):
            return True

    def actual_check(*args):
        for i in args:
            if isinstance(i, Messageable):
                if i.id == self.id:
                    return check(*args)
            elif isinstance(i, Message):
                if i.channel.id == self.id:
                    return check(*args)
            

    return actual_wait_for(event, check=actual_check, timeout=timeout)

Messageable.wait_for = wait_for
