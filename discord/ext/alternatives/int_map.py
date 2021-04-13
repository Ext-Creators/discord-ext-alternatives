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
discord.Member.__int__ = _int
discord.Message.__int__ = _int
discord.Reaction.__int__ = _int
discord.Team.__int__ = _int
discord.Webhook.__int__ = _int
