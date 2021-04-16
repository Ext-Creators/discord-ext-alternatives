.. raw:: html

    <p align="center">
        <a href="https://github.com/Ext-Creators/discord-ext-alternatives/actions?query=workflow%3AAnalyze+event%3Apush">
            <img alt="Analyze Status"
                 src="https://github.com/Ext-Creators/discord-ext-alternatives/workflows/Analyze/badge.svg?event=push" />
        </a>

        <a href="https://github.com/Ext-Creators/discord-ext-alternatives/actions?query=workflow%3ABuild+event%3Apush">
            <img alt="Build Status"
                 src="https://github.com/Ext-Creators/discord-ext-alternatives/workflows/Build/badge.svg?event=push" />
        </a>

        <a href="https://github.com/Ext-Creators/discord-ext-alternatives/actions?query=workflow%3ALint+event%3Apush">
            <img alt="Lint Status"
                 src="https://github.com/Ext-Creators/discord-ext-alternatives/workflows/Lint/badge.svg?event=push" />
        </a>
    </p>

----------

.. raw:: html

    <h1 align="center">discord-ext-alternatives</h1>
    <p align="center">A discord.py extension with additional and alternative features.</p>
    <h6 align="center">Copyright 2020-present Ext-Creators</h6>


Installation
------------

.. code-block:: sh

    pip install --upgrade discord-ext-alternatives


Usage
-----

.. code-block:: py

    from discord.ext.alternatives import asset_converter, message_eq
    # Patches the related features into discord.py
    # OR
    from discord.ext.alternatives.class_commands import ClassGroup, Config
