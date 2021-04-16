"""
    Copyright 2021 Ext-Creators

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

"""An experiment that allows `x in y` syntax for various discord objects.

Example:
```py
channel in guild

member in channel

member in role
```
"""

import discord
from discord.channel import CategoryChannel, DMChannel, TextChannel

if discord.version_info < (1, 7, 0):
    from discord.channel import VoiceChannel as VocalGuildChannel
else:
    from discord.channel import VocalGuildChannel

from discord.guild import Guild
from discord.member import Member
from discord.message import Message
from discord.role import Role
from discord.user import User, BaseUser


def guild_contains(self, item):
    if hasattr(item, 'guild'):
        return item.guild == self

    if isinstance(item, BaseUser):
        return item.id in self._members


    return False


Guild.__contains__ = guild_contains


def role_contains(self, item):
    if isinstance(item, User):
        item = self.guild._members.get(item.id)
    
    if isinstance(item, Member):
        return item._roles.has(self.id)

    return False


Role.__contains__ = role_contains


def textchannel_contains(self, item):
    if hasattr(item, 'channel'):
        return item.channel == self
    
    if isinstance(item, User):
        item = self.guild._members.get(item.id)

    if isinstance(item, Member):
        return self.permissions_for(item).read_messages
    
    return False


TextChannel.__contains__ = textchannel_contains


def vocalguildchannel_contains(self, item):
    if isinstance(item, BaseUser):
        for user_id, state in self.guild._voice_states.items():
            if state.channel and state.channel.id == self.id and item.id == user_id:
                return True

    return False


VocalGuildChannel.__contains__ = vocalguildchannel_contains


def categorychannel_contains(self, item):
    if hasattr(item, 'category'):
        return item.category == self

    return False


CategoryChannel.__contains__ = categorychannel_contains


def dmchannel_contains(self, item):
    if hasattr(item, 'channel'):
        return item.channel == self

    if isinstance(item, BaseUser):
        return item in (self.me, self.recipient)

    return False


DMChannel.__contains__ = dmchannel_contains