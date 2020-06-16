"""An experiment that allows you to register converters for classes,
as a helpful aid for readability when using typehints for custom converters.

You could also override base converters if you wanted to.

Example:
```py
class YertConverter(commands.Converter):
    async def convert(self, ctx, arg):
        return 'yert'

class Yert(object):
    ...

bot.converters[Yert] = YertConverter

@bot.command()
async def yert(ctx, yert: Yert):
    '''This will always send `yert`!'''
    await ctx.send(yert)
```
"""
import discord
from discord.ext.commands import Bot, converter, Command

from ._alternative_converters import _ALL

_BUILTINS = (
    bool,
    str,
    int,
    float,
)

_CONVERTERS = {
    discord.CategoryChannel: converter.CategoryChannelConverter,
    discord.Colour:          converter.ColourConverter,
    discord.Emoji:           converter.EmojiConverter,
    discord.Game:            converter.GameConverter,
    discord.Invite:          converter.InviteConverter,
    discord.Member:          converter.MemberConverter,
    discord.Message:         converter.MessageConverter,
    discord.PartialEmoji:    converter.PartialEmojiConverter,
    discord.Role:            converter.RoleConverter,
    discord.TextChannel:     converter.TextChannelConverter,
    discord.User:            converter.UserConverter,
    discord.VoiceChannel:    converter.VoiceChannelConverter,
}

_CONVERTERS.update({ b: b for b in _BUILTINS })

class _ConverterDict(dict):
    """An easy way to register converters for classes.
    
    Can help for both linting and readability.
    """
    def __init__(self):
        super().__init__(_CONVERTERS)
        super().update(_ALL)

    def __setitem__(self, k, v):
        if not (issubclass(v, converter.Converter) or issubclass(v, _BUILTINS)):
            raise TypeError('Excepted value of type \'Converter\' or built-in, received %r' % v.__name__)
        super().__setitem__(k, v)
    
    def set(self, k, v):
        """Same as doing ``ConverterDict[Obj] = ObjConverter`` but fluid.
        """
        self.__setitem__(k, v)
        return self

_GLOBAL_CONVERTER_DICT = _ConverterDict()

Bot.converters = _GLOBAL_CONVERTER_DICT

def _get_converter(self, param):
    obj = param.annotation
    if obj is param.empty:
        if param.default is not param.empty:
            converter = _GLOBAL_CONVERTER_DICT.get(type(param.default), str)
        else:
            converter = str
    else:
        converter = _GLOBAL_CONVERTER_DICT.get(obj, obj) # fall back on its typehint if its converter isn't registered
    return converter

Command._get_converter = _get_converter
