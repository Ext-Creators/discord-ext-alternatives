Changelog
=========

.. _id_20201011:

``2020.10.11``
--------------

- Added ``binary_checks``.
- Add a ``py_allow`` function for restricting Python versions.
- Fix issues with `literal_converter`
- Fix a name error with ``converter_dict``
- Simplify ``converter_dict`` to work with ``typing.Union``

.. _id_20200730:

``2020.07.30``
--------------

-  Added ``menus_remove_reaction``.
-  Added ``command_suffix``.
-  Added ``command_piping``.
-  Added ``inline_bot_commands``.
-  Added ``literal_converter``.
-  Added ``messageable_wait_for``.
-  Added ``material_colours``.
-  Added ``dict_converter``.
-  Fix ``Optional`` behaviour of ``asset_converter``.

.. _id_20200616:

``2020.06.16``
--------------

-  Updated ``asset_converter`` and ``guild_converter`` to be compatible
   with ``converter_dict``.
-  Added ``jump_url``.
-  Added ``converter_dict``.

.. _id_20200520:

``2020.05.20``
--------------

-  Fixed bug with ``silent_delete``.
-  Added ``guild_converter``.
-  Added ``class_commands``.

.. _id_20200512:

``2020.05.12``
--------------

-  Added ``silent_delete``
-  ``int_map`` no longer errors on ``Invite.__int__``
-  ``specific_error_handler`` now works in cogs, and walks ``__mro__``
   to check exceptions.
-  ``subcommand_error`` no longer errors in Cog exception propagation.

.. _id_20200510:

``2020.05.10``
--------------

-  Added ``int_map``
-  Added ``specific_error_handler``
-  ``message_eq`` checks for a ``Message`` instance

.. _id_20200509:

``2020.05.09``
--------------

-  Added ``asset_converter``
-  Added ``bot_send_help``
-  Added ``message_eq``
-  Added ``subcommand_error``
-  Added ``webhook_channel``
