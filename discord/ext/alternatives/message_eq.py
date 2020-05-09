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

from discord import Message
Message.__eq__ = lambda self, other: self.id == other.id
