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


discord.Message.__eq__ = lambda self, other: isinstance(other, discord.Message) and self.id == other.id
