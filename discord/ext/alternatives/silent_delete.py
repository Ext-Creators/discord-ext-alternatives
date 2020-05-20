"""An experiment to allow for ``Message.delete`` to be silenced
of any exception. 

It uses a keyword argument called `silent`, and is by default
``False``.
"""

from discord import Message

_old_delete = Message.delete

async def delete(self, *, delay=None, silent=False):
    try:
        await _old_delete(delay=delay)
    except Exception:
        if not silent:
            raise

Message.delete = delete
