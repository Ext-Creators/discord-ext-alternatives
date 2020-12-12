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

"""**STANDALONE**: An experiment that allows the use of classes and
functions as a way to represent a group of commands.

Example:
```py
@bot.group(cls=ClassGroup)
class A(Config, invoke_without_command=True): # A group command
    _CONFIG = Config(invoke_without_command=True, description='no')

    async def __call__(ctx):
        await ctx.send('test')
    
    async def fmt(ctx): # A command
        await ctx.send('toot')
    
    class B: # A group command
        #_CONFIG = Config(description='yes')

        async def __call__(ctx):
            await ctx.send('no')

        async def oops(ctx): # A command
            await ctx.send('yert')
```

```
!A -> 'test'
!A fmt -> 'toot'
!A B -> 'no'
!A B oops -> 'no', 'yert'
```
"""

import inspect

from discord.ext import commands


class ClassGroup(commands.Group):
    def __init__(self, cls, *, name=None, parent=None):
        kwargs = {"name": name or cls.__name__, "parent": parent}
        func = cls.__call__

        try:
            cls._CONFIG
        except AttributeError:
            pass
        else:
            kwargs.update(cls._CONFIG.to_dict())

        super().__init__(func, **kwargs)

        for f in dir(cls):
            if f.startswith("_"):
                continue

            attr = getattr(cls, f)

            if inspect.isclass(attr):
                self.add_command(ClassGroup(attr, parent=self))
            elif inspect.iscoroutinefunction(attr):
                self.add_command(commands.Command(attr))

class Config():
    def __init__(self, *, 
                 invoke_without_command: bool=False, 
                 case_insensitive: bool=False,
                 help: str="",
                 brief: str="",
                 usage: str="",
                 aliases: list=[],
                 checks: list=[],
                 description: str="",
                 hidden: bool=False,
        ):
        self.invoke_without_command = invoke_without_command
        self.case_insensitive = case_insensitive
        self.help = help
        self.brief = brief
        self.usage = usage
        self.aliases = aliases
        self.checks = checks
        self.description = description
        self.hidden = hidden

    def to_dict(self):
        d = {}
        for attr in dir(self):
            if not attr.startswith("_"):
                d[attr] = getattr(self, attr)

        return d
