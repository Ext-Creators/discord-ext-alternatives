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

"""An experiment to allow for ``Message.delete`` to be silenced
of any exception. 

It uses a keyword argument called `silent`, and is by default
``False``.
"""

import discord


_old_delete = discord.Message.delete

async def delete(self, *, silent=False, **kwargs):
    try:
        await _old_delete(self, **kwargs)
    except Exception as e:
        if not silent:
            raise e

discord.Message.delete = delete
