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

"""An experiment that allows you to send help without requiring ``Context``,
or inside of ``on_message``.

Example:
```py
@bot.event
async def on_message(message):
    if message.content == message.guild.me.mention:
        await bot.send_help(message) # sends the entire help command.
```
"""

from discord.ext import commands


def send_help(self, message, *args, **kwargs):
    ctx = kwargs.get("cls", commands.Context)(prefix=self.user.mention, bot=self, message=message)
    return ctx.send_help(*args)

commands.bot.BotBase.send_help = send_help
