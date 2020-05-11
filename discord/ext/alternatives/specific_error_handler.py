"""An experiment that allows handlers to handle specific errors.

This overrides the default behaviour of ``Command.error``.
(Change ``@Command.error`` to ``@Command.error()``).

Example:
```py
@bot.command()
async def throw_error(ctx):
    raise Exception

@command.error(CommandInvokeError)
async def handle(ctx, error):
    if isinstance(error.original, Exception):
        await ctx.send('oh no')
```
"""

import asyncio
from discord.ext.commands import Command

async def _on_error(ctx, error: Exception):
    cls = error.__class__
    if cls in ctx.command._handled_errors:
        await ctx.command._handled_errors[cls](ctx, error)

def _error(self, *exceptions):
    def decorator(func):
        if not asyncio.iscoroutinefunction(func):
            raise TypeError('The error must be a funcutine.')

        if not exceptions:
            self.on_error = func
            return

        try:
            self._handled_errors
        except AttributeError:
            self._handled_errors = {}
        finally:
            for exc in exceptions:
                self._handled_errors[exc] = func

        try:
            self.on_error
        except AttributeError as e:
            self.on_error = _on_error

        return func
    return decorator

Command.error = _error
