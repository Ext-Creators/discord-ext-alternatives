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

import discord
from discord.ext import menus


_old_update = menus.Menu.update


async def update(self: menus.Menu, payload: discord.RawReactionActionEvent):
    await _old_update(self, payload)

    if payload.event_type != "REACTION_ADD":
        return

    permissions = self.ctx.channel.permissions_for(self.ctx.me)
    if not (permissions.manage_messages or permissions.administrator):
        return

    await self.message.remove_reaction(payload.emoji, discord.Object(id=payload.user_id))


update.__doc__ = _old_update.__doc__
menus.Menu.update = update
