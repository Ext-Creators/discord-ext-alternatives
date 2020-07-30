# discord-ext-alternatives
Enable some experimental features for [discord.py](https://github.com/Rapptz/discord.py/).

> ⚠️ **This is experimental and should be used with caution.**
> If you encounter any issues with this extension, please make an issue.

## Installation

This extension is on [PyPI](https://pypi.org/project/discord-ext-alternatives/).

```sh
$ python3 -m pip install -U discord-ext-alternatives
```

## Usage

```py
from discord.ext.alternatives import asset_converter, message_eq
# Patches the related features into discord.py
# OR
from discord.ext.alternatives.class_commands import ClassGroup, Config
```

## Available Experiments

- `asset_converter` - Implements a converter for ``Asset``.
- `bot_send_help` - Implements `Bot.send_help`.
- `command_suffix` - Implements `Bot.command_suffix` and `Context.suffix`.
- `command_piping` - Implements piping for `return` in command callbacks
- `converter_dict` - Implements `Bot.converters`.
- `dict_converter` - Implements `**kwargs` mapping for command arguments.
- `guild_converter` - Implements a converter for ``Guild``.
- `inline_bot_commands` - Implements support for commands directly defined in a `Bot` subclass.
- `int_map` - Implements `__int__` to return `.id`.
- `jump_url` - Implements `Guild.jump_url` and `abc.Messagable.jump_url`.
- `material_colours` - Implements [material.io](https://material.io/resources/color/) shade 400's colours.
- `message_eq` - Implements `Message.__eq__` (`Message == Message`).
- `silent_delete` - Implements a `silent` keyword argument for `Message.delete`.
- `specific_error_handler` - Implements `@Command.error(Exception)`.
- `subcommand_error` - Implements `root_parent` error handling.
- `webhook_channel` - Implements `Webhook.move_to`.

#### Standalone
- `class_commands` - Implements a way to use classes and functions as commands.

## Changelog

### 2020.06.16

- Updated `asset_converter` and `guild_converter` to be compatible with `converter_dict`.
- Added `jump_url`.
- Added `converter_dict`.

### 2020.05.20

- Fixed bug with `silent_delete`.
- Added `guild_converter`.
- Added `class_commands`.

### 2020.05.12

- Added `silent_delete`
- `int_map` no longer errors on `Invite.__int__`
- `specific_error_handler` now works in cogs, and walks `__mro__` to check exceptions.
- `subcommand_error` no longer errors in Cog exception propagation.

### 2020.05.10

- Added `int_map`
- Added `specific_error_handler`
- `message_eq` checks for a ``Message`` instance

### 2020.05.09

- Added `asset_converter`
- Added `bot_send_help`
- Added `message_eq`
- Added `subcommand_error`
- Added `webhook_channel`
