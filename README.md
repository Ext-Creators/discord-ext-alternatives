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
```

## Available Experiments

- `asset_converter` - Implements a converter for ``Asset``.
- `bot_send_help` - Implements `Bot.send_help`.
- `message_eq` - Implements `Message.__eq__` (`Message == Message`)
- `subcommand_error` - Implements `root_parent` error handling.
- `webhook_channel` - Implements `Webhook.move_to`.

## Changelog

### 2020.05.09

- Added `asset_converter`
- Added `bot_send_help`
- Added `message_eq`
- Added `subcommand_error`
- Added `webhook_channel`
