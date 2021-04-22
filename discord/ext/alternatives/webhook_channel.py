"""An experiment to allow for webhooks to change channels.

Example:
```py
webhook = await ctx.bot.fetch_webhook(id)
channel = ctx.guild.text_channels[1]

await webhook.move_to(channel=channel)
```
"""
from discord.webhook.async_ import Webhook
from discord.webhook.sync import SyncWebhook


async def _async_move_to(self, channel, *, reason=None):
    return await self.edit(reason=reason, channel=channel)


async def _sync_move_to(self, channel, *, reason=None):
    return self.edit(reason=reason, channel=channel)


Webhook.move_to = _async_move_to
SyncWebhook.move_to = _sync_move_to
