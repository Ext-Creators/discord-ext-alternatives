from typing import Literal, get_args
from discord.ext.commands import Command
from discord.ext.commands.errors import ConversionError

_old_actual_conversion = Command._actual_conversion

def _actual_conversion(self, ctx, converter, argument, param):
    if converter is Literal:
        items = get_args(converter)

        if all(i for i in items if isinstance(i, str)):
            if argument in items:
                return argument
                
            raise commands.BadArgument(f"Expected literal: one of {list(map(repr, self.literals))}")
        elif all(i for i in items if not isinstance(i, str)):
            ret = _old_actual_conversion(self, ctx, type(items[0]), argument, param)
            return ret in items
        else:
            raise ConversionError('Literal contains multiple conflicting types.')
    
    return _old_actual_conversion(self, ctx, converter, argument, param)

Command._actual_conversion = _actual_conversion
