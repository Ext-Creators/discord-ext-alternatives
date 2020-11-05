"""An experiment that enables ``__int__`` on certain objects
to return the ``id`` attribute.
"""

import discord


_int = lambda self: self.id

discord.AppInfo.__int__ = _int
discord.Attachment.__int__ = _int
discord.AuditLogEntry.__int__ = _int
discord.emoji._EmojiTag.__int__ = _int
discord.mixins.Hashable.__int__ = _int
discord.Message.__int__ = _int
discord.Reaction.__int__ = _int
discord.Team.__int__ = _int
discord.Webhook.__int__ = _int
