"""An experiment that enables ``Message.__eq__``.

It compares the IDs of each ``Message``.

Example:

```py
>>> m1 == m1
True # Same IDs
>>> m1 == m2
False # Different IDs
```
"""

import discord


discord.Message.__eq__ = lambda s, o: isinstance(o, discord.Message) and s.id == o.id
