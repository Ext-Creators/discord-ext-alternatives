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

"""An experiment that enables auto removing reactions added to menus.

"""

from discord import Object, RawReactionActionEvent
from discord.ext.menus import Menu


_old_update = Menu.update


async def _update(self: Menu, payload: RawReactionActionEvent):
    await _old_update(self, payload)
    if payload.event_type != 'REACTION_ADD':
        return

    if not self.ctx.channel.permissions_for(self.ctx.me).manage_messages:
        if not self.ctx.channel.permissions_for(self.ctx.me).administrator:
            return

    await self.message.remove_reaction(payload.emoji, Object(id=payload.user_id))

_update.__doc__ = _old_update.__doc__

Menu.update = _update
