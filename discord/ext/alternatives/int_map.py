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

from discord.mixins import Hashable
from discord.abc import User
from discord.invite import Invite
from discord.appinfo import AppInfo
from discord.audit_logs import AuditLogEntry
from discord.partial_emoji import _EmojiTag
from discord.message import Attachment, Message
from discord.reaction import Reaction
from discord.team import Team
from discord.webhook import Webhook

_int = lambda self: self.id

Hashable.__int__ = _int
AppInfo.__int__ = _int
AuditLogEntry.__int__ = _int
_EmojiTag.__int__ = _int
Attachment.__int__ = _int
Message.__int__ = _int
Reaction.__int__ = _int
Team.__int__ = _int
Webhook.__int__ = _int
