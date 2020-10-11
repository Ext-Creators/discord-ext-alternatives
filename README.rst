discord-ext-alternatives
========================

|package| |versions| |dependencies| |license| |cloned|

Patches some additional/alternative features into discord.py.

    ⚠️ **This is experimental and should be used with caution.**
    If you encounter any issues with this extension, please make an issue.


Installation
------------

This extension is on `PyPI <https://pypi.org/project/discord-ext-alternatives/>`_.

.. code-block:: sh

    $ python3 -m pip install -U discord-ext-alternatives

Usage
-----

.. code-block:: py

    from discord.ext.alternatives import asset_converter, message_eq
    # Patches the related features into discord.py
    # OR
    from discord.ext.alternatives.class_commands import ClassGroup, Config

Available Experiments
---------------------

- ``asset_converter`` - Implements a converter for ``Asset``.
- ``bot_send_help`` - Implements ``Bot.send_help``.
- ``binary_checks`` - Implements `OR`, `AND`, `NOT` operators for command checks.
- ``command_suffix`` - Implements ``Bot.command_suffix`` and ``Context.suffix``.
- ``command_piping`` - Implements piping for ``return`` in command callbacks
- ``converter_dict`` - Implements ``Bot.converters``.
- ``dict_converter`` - Implements ``**kwargs`` mapping for command arguments.
- ``guild_converter`` - Implements a converter for ``Guild``.
- ``inline_bot_commands`` - Implements support for commands directly defined in a ``Bot`` subclass.
- ``int_map`` - Implements ``__int__`` to return ``.id``.
- ``jump_url`` - Implements ``Guild.jump_url`` and ``abc.Messagable.jump_url``.
- ``material_colours`` - Implements `material.io <https://material.io/resources/color/>`_ shade 400's colours.
- ``menus_remove_reaction`` - Adds support for automatically removing reactions on menus.
- ``message_eq`` - Implements ``Message.__eq__`` (``Message == Message``).
- ``silent_delete`` - Implements a ``silent`` keyword argument for ``Message.delete``.
- ``specific_error_handler`` - Implements ``@Command.error(Exception)``.
- ``subcommand_error`` - Implements ``root_parent`` error handling.
- ``webhook_channel`` - Implements ``Webhook.move_to``.

Standalone
----------

-  ``class_commands`` - Implements a way to use classes and functions as commands.

.. _Extension experiments can be found in the `ext/` directory.: discord/ext/alternatives/ext/README.rst

.. |package| image:: https://img.shields.io/pypi/v/discord-ext-alternatives.svg
.. |versions| image:: https://img.shields.io/pypi/pyversions/discord-ext-alternatives.svg
.. |dependencies| image:: https://img.shields.io/librariesio/github/Ext-Creators/discord-ext-alternatives
.. |license| image:: https://img.shields.io/pypi/l/discord-ext-alternatives.svg
.. |cloned| image:: https://img.shields.io/pypi/dm/discord-ext-alternatives.svg