"""An experiment to allow for ``Message.delete`` to be silenced
of any exception. 

It uses a keyword argument called `silent`, and is by default
``False``.
"""

import discord


_old_delete = discord.Message.delete

async def delete(self, *, silent=False, **kwargs):
    try:
        await _old_delete(self, **kwargs)
    except Exception as e:
        if not silent:
            raise e

discord.Message.delete = delete
