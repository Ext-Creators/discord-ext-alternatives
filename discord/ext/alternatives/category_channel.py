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

"""An experiment that allows you to shuffle the positions of channels
in a CategoryChannel in a way that isn't quickly rate-limited.

Works with TextChannels and VoiceChannels alike.

Example:
```py
@is_owner()
@bot.command()
async def shuffle(ctx):
    await ctx.channel.category.shuffle()
```
"""

import random

from discord import CategoryChannel


async def _shuffle(self):
    """|coro|

    Shuffles the channels within the CategoryChannel.

    You must have the :attr:`~discord.Permissions.manage_channels` permission to
    do this.

    Raises
    -------
    Forbidden
        You do not have permissions to shuffle the channels.
    HTTPException
        Shuffling the channels failed.
    """

    channel_ids = [channel.id for channel in self.channels]
    random.shuffle(channel_ids)

    payload = [
        {"id": channel_id, "position": index}
        for index, channel_id in enumerate(channel_ids)
    ]

    await self._state.http.bulk_channel_update(self.guild.id, payload)


CategoryChannel.shuffle = _shuffle
