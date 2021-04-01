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

"""An experiment that allows you to change the positions of channels
in a CategoryChannel in a way that isn't quickly rate-limited.

Works with TextChannels and VoiceChannels alike.

Example:
```py
@is_owner()
@bot.command()
async def by_length(ctx):
    await ctx.channel.category.sort(key=lambda c: len(c.name))

@is_owner()
@bot.command()
async def alphabetize(ctx):
    await ctx.channel.category.alphabetize()

@is_owner()
@bot.command()
async def shuffle(ctx):
    await ctx.channel.category.shuffle()
```
"""

import random

from discord import CategoryChannel


async def _sort(self, *, key=None, reverse=False):
    """|coro|

    Sorts the channels within the CategoryChannel, similar to Python's list.sort().

    You must have the :attr:`~discord.Permissions.manage_channels` permission to
    do this.

    Parameters
    -----------
    key: Callable
        A callable function to customize the sort order.
        The supplied argument is of type ``GuildChannel``.
    reverse: :class:`bool`
        Whether or not to sort in descending order. False by default.

    Raises
    -------
    Forbidden
        You do not have permissions to sort the channels.
    HTTPException
        Sorting the channels failed.
    """
    payload = [
        {"id": channel.id, "position": index}
        for index, channel in enumerate(sorted(self.channels, key=key, reverse=reverse))
    ]

    await self._state.http.bulk_channel_update(self.guild.id, payload)


async def _alphabetize(self, *, reverse=False):
    """|coro|

    Alphabetizes the channels within the CategoryChannel.

    You must have the :attr:`~discord.Permissions.manage_channels` permission to
    do this.

    Parameters
    -----------
    reverse: :class:`bool`
        Whether or not to alphabetize in descending order. False by default.

    Raises
    -------
    Forbidden
        You do not have permissions to alphabetize the channels.
    HTTPException
        Alphabetizing the channels failed.
    """

    await self.sort(key=lambda c: c.name, reverse=reverse)


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

    await self.sort(key=lambda _: random.random())


CategoryChannel.sort = _sort
CategoryChannel.alphabetise = _alphabetize
CategoryChannel.alphabetize = _alphabetize
CategoryChannel.shuffle = _shuffle
