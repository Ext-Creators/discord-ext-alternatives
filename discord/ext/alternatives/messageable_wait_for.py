from discord.abc import Messageable
from discord.message import Message


def wait_for(self, event, *, check=None, timeout=None):
    actual_wait_for = self._state.dispatch.__self__.wait_for

    if check is None:
        def check(*args):
            return True

    def actual_check(*args):
        for i in args:
            if isinstance(i, Messageable):
                if i.id == self.id:
                    return check(*args)
            elif isinstance(i, Message):
                if i.channel.id == self.id:
                    return check(*args)
            

    return actual_wait_for(event, check=actual_check, timeout=timeout)

Messageable.wait_for = wait_for
