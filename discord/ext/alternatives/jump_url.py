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

"""An experiment that enables ``Guild.jump_url`` and ``abc.Messagable.jump_url``.

Example:

```py
>>> message.channel.jump_url
https://discord.com/channels/364412422540361729/708518465820033105
```
"""

import discord


@property
def guild_jump_url(self):
    """:class:`str`: Returns a URL that allows the client to jump to this guild."""

    return "https://discord.com/channels/{0.id}".format(self)

discord.Guild.jump_url = guild_jump_url

@property
def messageable_jump_url(self):
    """:class:`str`: Returns a URL that allows the client to jump to this channel."""

    if isinstance(self, discord.abc.User):
        if self.dm_channel is None:
            raise AttributeError("Could not find DM channel for user '{0}'".format(self))

        channel_id = self.dm_channel.id
    else:
        channel_id = self.channel.id if hasattr(self, "channel") else self.id

    guild_id = self.guild.id if isinstance(self, discord.abc.GuildChannel) else "@me"

    return "https://discord.com/channels/{0}/{1}".format(guild_id, channel_id)

discord.abc.Messageable.jump_url = messageable_jump_url
