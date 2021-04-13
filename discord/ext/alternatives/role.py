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

"""An experiment that allows you to shave a role off of all members. Optionally,
you can pass Member objects (or IDs) to spare those members from having the role shaved.
"""

from discord import Role
from discord.abc import Snowflake
from typing import Union, Optional


async def _shave(
    self,
    *except_members: Union[int, Snowflake],
    reason: Optional[str] = None,
    atomic: bool = True,
):
    r"""|coro|

    Shaves :class:`Role`\s from all members with the role, unless explicitly
    added to except_members.

    You must have the :attr:`~Permissions.manage_roles` permission to
    use this.

    Parameters
    -----------
    \*except_members: :class:`abc.Snowflake`
        An argument list of :class:`abc.Snowflake` representing a :class:`Member`
        to not shave the role from.
    reason: Optional[:class:`str`]
        The reason for removing these roles. Shows up on the audit log.
    atomic: :class:`bool`
        Whether to atomically remove roles. This will ensure that multiple
        operations will always be applied regardless of the current
        state of the cache.

    Raises
    -------
    Forbidden
        You do not have permissions to remove these roles.
    HTTPException
        Removing the roles failed.
    """

    except_members_ids = {int(m) for m in except_members}

    for member in self.members:
        if member.id in except_members_ids:
            continue

        await member.remove_roles(self, reason=reason, atomic=atomic)


Role.shave = _shave
