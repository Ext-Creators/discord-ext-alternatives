import discord
from discord.ext import commands


def wait_for(self, event, *, check=None, timeout=None):
    actual_wait_for = self._state.dispatch.__self__.wait_for

    if check is None:
        def check(*args):
            return True

    def actual_check(*args):
        for arg in args:
            if isinstance(arg, (discord.Message, commands.Context)):
                if arg.channel.id == self.id:
                    return check(*args)
            elif isinstance(arg, discord.abc.Messageable):
                if arg.id == self.id:
                    return check(*args)

    return actual_wait_for(event, check=actual_check, timeout=timeout)

discord.abc.Messageable.wait_for = wait_for
