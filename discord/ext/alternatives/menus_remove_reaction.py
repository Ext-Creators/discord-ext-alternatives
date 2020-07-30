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
