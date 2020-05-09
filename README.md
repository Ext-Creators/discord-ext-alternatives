# discord-ext-alternatives
Enable some experimental features for [discord.py](https://github.com/Rapptz/discord.py/).

## Installation

This extension is on [PyPI](https://pypi.org/project/discord-ext-alternatives/).

```sh
$ python3 -m pip install -U discord-ext-alternatives
```

## Available Experiments

- `asset_converter` - Implements a converter for ``Asset``.
- `bot_send_help` - Implements `Bot.send_help`.
- `message_eq` - Implements `Message.__eq__` (`Message == Message`)
- `subcommand_error` - Implements `root_parent` error handling.
- `webhook_channel` - Implements `Webhook.move_to`.
