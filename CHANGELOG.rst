Changelog
=========

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
