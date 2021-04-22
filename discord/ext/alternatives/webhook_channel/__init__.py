"""An experiment to allow for webhooks to change channels.

Example:
```py
webhook = await ctx.bot.fetch_webhook(id)
channel = ctx.guild.text_channels[1]

await webhook.move_to(channel=channel)
```
"""
import discord


if discord.version_info < (2, 0, 0):
    from . import v1
else:
    from . import v2
