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

from discord.ext import commands


async def invoke(self, ctx):
    await self.prepare(ctx)

    ctx.invoked_subcommand = None
    injected = commands.core.hooked_wrapped_callback(self, ctx, self.callback)

    ret = await injected(*ctx.args, **ctx.kwargs)
    if ret is not None:
        await ctx.send(ret)

commands.Command.invoke = invoke
