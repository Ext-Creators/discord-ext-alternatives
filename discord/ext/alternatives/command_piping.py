"""An experiment that allows the use of returns in the command callback to reply to the user

Example:
```py
@bot.command()
async def foo(ctx):
    await ctx.send('hello')
    return 'world!'

'?foo' -->

'hello'
'world!'
"""


from discord.ext.commands.core import hooked_wrapped_callback, Command

async def invoke(self, ctx):
    await self.prepare(ctx)
    ctx.invoked_subcommand = None
    injected = hooked_wrapped_callback(self, ctx, self.callback)
    ret = await injected(*ctx.args, **ctx.kwargs)
    if ret is not None:
        await ctx.send(ret)

Command.invoke = invoke
