discord-ext-alternatives-ext
============================

Enable some experimental features various for `discord.py`_ extension
packages.

Usage
-----

.. code:: py

   from discord.ext.alternatives.ext.menus import remove_reaction
   # Patches the related features into relevant discord.py extensions

Available Experiments
---------------------

``.menus``
~~~~~~~~~~

-  ``remove_reaction`` - Adds support for automatically removing
   reactions on menus.

Changelog
---------

.. _id_20200730:

2020.07.30
~~~~~~~~~~

-  Added ``menus.remove_reaction``

.. _discord.py: https://github.com/Rapptz/discord.py/
