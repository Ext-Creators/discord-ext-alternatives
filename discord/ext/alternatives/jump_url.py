"""An experiment that implements ``Guild.jump_url`` and ``abc.GuildChannel.jump_url``.

Example:

```py
>>> message.channel.jump_url
https://discord.com/channels/364412422540361729/708518465820033105
```
"""

from discord import Guild
from discord.abc import GuildChannel

@property
def guild_jump_url(self):
    """:class:`str`: Returns a URL that allows the client to jump to this guild."""
    return 'https://discord.com/channels/{0.id}'.format(self)

Guild.jump_url = guild_jump_url

@property
def channel_jump_url(self):
    """:class:`str`: Returns a URL that allows the client to jump to this guild."""
    return 'https://discord.com/channels/{0.guild.id}/{0.id}/'.format(self)

GuildChannel.jump_url = channel_jump_url
