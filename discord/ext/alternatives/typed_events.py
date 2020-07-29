"""
An experiment that has typed events registered to the Client/Bot when TYPE_CHECKING returns `True`.
and at runtime will only have the subclassed events be registered. A better version of #4134.

```py
from discord.ext.alternatives.typed_events import Bot


class MyBot(Bot):
    async def on_message(self, message):
        # most good linters should be able to pick message up as discord.Message
        # otherwise use autocomplete on the method and have it easily typed for you.
        print(message.author, "said", message.content)
```
"""

import sys
import traceback
from datetime import datetime
from typing import AnyStr, List, Optional, TYPE_CHECKING, Union

import discord
from discord.ext import commands

# from .inline_bot_commands import Bot

Channels = Union[discord.TextChannel, discord.GroupChannel, discord.DMChannel]
Users = Union[discord.User, discord.Member]


class Client(discord.Client):
    if TYPE_CHECKING:
        async def on_connect(self):
            """|coro|
            Called when the client has successfully connected to Discord. This is not
            the same as the client being fully prepared, see :meth:`on_ready` for that.
            The warnings on :meth:`on_ready` also apply.
            """

        async def on_disconnect(self):
            """|coro|
            Called when the client has disconnected from Discord. This could happen either through
            the internet being disconnected, explicit calls to logout, or Discord terminating the connection
            one way or the other.
            This function can be called many times.
            """

        async def on_ready(self):
            """|coro|
            Called when the client is done preparing the data received from Discord. Usually after login is successful
            and the :attr:`Client.guilds` and co. are filled up.

            .. warning::

                This function is not guaranteed to be the first event called.
                Likewise, this function is **not** guaranteed to only be called
                once. This library implements reconnection logic and thus will
                end up calling this event whenever a RESUME request fails.
            """

        async def on_shard_ready(self, shard_id: int):
            """|coro|
            Similar to :meth:`on_ready` except used by :class:`~discord.AutoShardedClient`
            to denote when a particular shard ID has become ready.

            Parameters
            ------------
            shard_id: :class:`int`
                The shard ID that is ready.
            """

        async def on_resumed(self):
            """|coro|
            Called when the client has resumed a session.
            """

        async def on_error(self, event: str, *args, **kwargs):
            r"""|coro|
            The default error handler provided by the client.

            Usually when an event raises an uncaught exception, a traceback is
            printed to stderr and the exception is ignored. If you want to
            change this behaviour and handle the exception yourself,
            this event can be overridden. Which, when done, will
            suppress the default action of printing the traceback.

            If you want exception to propagate out of the :class:`Client` class
            you can define an ``on_error`` handler consisting of a single empty
            :ref:`py:raise`. Exceptions raised by ``on_error`` will not be
            handled in any way by :class:`Client`.

            Parameters
            ------------
            event: :class:`str`
                The name of the event that raised the exception.
            \*args:
                The positional arguments for the event that raised the exception.
            \*\*kwargs:
                The keyword arguments for the event that raised the exception.
            """
            print('Ignoring exception in {}'.format(event), file=sys.stderr)
            traceback.print_exc()

        async def on_socket_raw_receive(self, msg: AnyStr):
            """|coro|
            Called whenever a message is received from the WebSocket, before
            it's processed. This event is always dispatched when a message is
            received and the passed data is not processed in any way.
            This is only really useful for grabbing the WebSocket stream and
            debugging purposes.

            .. note::

                This is only for the messages received from the client
                WebSocket. The voice WebSocket will not trigger this event.

            Parameters
            ------------
            msg: Union[:class:`bytes`, :class:`str`]
                The message passed in from the WebSocket library.
                Could be :class:`bytes` for a binary message or :class:`str`
                for a regular message.
            """

        async def on_socket_raw_send(self, payload: AnyStr):
            """|coro|
            Called whenever a send operation is done on the WebSocket before the
            message is sent. The passed parameter is the message that is being
            sent to the WebSocket.

            This is only really useful for grabbing the WebSocket stream and
            debugging purposes.

            .. note::

                This is only for the messages received from the client
                WebSocket. The voice WebSocket will not trigger this event.

            Parameters
            ------------
            payload: Union[:class:`bytes`, :class:`str`]
                The message that is about to be passed on to the
                WebSocket library. It can be :class:`bytes` to denote a binary
                message or :class:`str` to denote a regular text message.
            """

        async def on_typing(self, channel: Channels, user: Users, when: datetime):
            """|coro|
            Called when someone begins typing a message.

            The ``channel`` parameter can be a :class:`~discord.abc.Messageable` instance.
            Which could either be :class:`~discord.TextChannel`, :class:`~discord.GroupChannel`, or
            :class:`~discord.DMChannel`.

            If the ``channel`` is a :class:`~discord.TextChannel` then the ``user`` parameter
            is a :class:`~discord.Member`, otherwise it is a :class:`~discord.User`.

            Parameters
            ------------
            channel: :class:`~discord.abc.Messageable`
                The location where the typing originated from.
            user: Union[:class:`~discord.User`, :class:`~discord.Member`]
                The user that started typing.
            when: :class:`datetime.datetime`
                When the typing started as a naive datetime in UTC.
            """

        async def on_message(self, message: discord.Message):
            """|coro|
            Called when a :class:`~discord.Message` is created or sent.

            .. warning::

                Your bot's own messages and private messages are sent through this
                event. This can lead cases of 'recursion' depending on how your bot was
                programmed. If you want the bot to not reply to itself, consider
                checking the user IDs. Note that :class:`~discord.ext.commands.Bot` does not
                have this problem.

            Parameters
            ------------
            message: :class:`~discord.Message`
                The message that was created or sent.
            """

        async def on_message_delete(self, message: discord.Message):
            """|coro|
            Called when a message is deleted. If the message is not found in the
            internal message cache, then this event will not be called.
            Messages might not be in cache if the message is too old
            or the client is participating in high traffic guilds.

            If this occurs increase the :attr:`Client.max_messages` attribute
            or use the :meth:`on_raw_message_delete` event instead.

            Parameters
            ------------
            message: :class:`~discord.Message`
                The deleted message.
            """

        async def on_bulk_message_delete(self, messages: List[discord.Message]):
            """|coro|
            Called when messages are bulk deleted. If none of the messages deleted
            are found in the internal message cache, then this event will not be called.
            If individual messages were not found in the internal message cache,
            this event will still be called, but the messages not found will not be included in
            the messages list. Messages might not be in cache if the message is too old
            or the client is participating in high traffic guilds.

            If this occurs increase the :attr:`Client.max_messages` attribute
            or use the :meth:`on_raw_bulk_message_delete` event instead.

            Parameters
            ------------
            messages: List[:class:`~discord.Message`]
                The messages that have been deleted.
            """

        async def on_raw_message_delete(self, payload: discord.RawMessageDeleteEvent):
            """|coro|
            Called when a message is deleted. Unlike :meth:`on_message_delete`, this is
            called regardless of the message being in the internal message cache or not.

            If the message is found in the message cache,
            it can be accessed via :attr:`~discord.RawMessageDeleteEvent.cached_message`

            Parameters
            ------------
            payload: :class:`~discord.RawMessageDeleteEvent`
                The raw event payload data.
            """

        async def on_raw_bulk_message_delete(self, payload: discord.RawBulkMessageDeleteEvent):
            """|coro|
            Called when a bulk delete is triggered. Unlike :meth:`on_bulk_message_delete`, this is
            called regardless of the messages being in the internal message cache or not.

            If the messages are found in the message cache,
            they can be accessed via :attr:`RawBulkMessageDeleteEvent.cached_messages`

            Parameters
            ------------
            payload: :class:`~discord.RawBulkMessageDeleteEvent`
                The raw event payload data.
            """

        async def on_message_edit(self, before: discord.Message, after: discord.Message):
            """|coro|
            Called when a :class:`~discord.Message` receives an update event. If the message is not found
            in the internal message cache, then these events will not be called.
            Messages might not be in cache if the message is too old
            or the client is participating in high traffic guilds.

            If this occurs increase the :attr:`Client.max_messages` attribute
            or use the :meth:`on_raw_message_edit` event instead.

            The following non-exhaustive cases trigger this event:

            - A message has been pinned or unpinned.
            - The message content has been changed.
            - The message has received an embed.

                - For performance reasons, the embed server does not do this in a "consistent" manner.

            - The message's embeds were suppressed or unsuppressed.
            - A call message has received an update to its participants or ending time.

            Parameters
            ------------
            before: :class:`~discord.Message`
                The previous version of the message.
            after: :class:`~discord.Message`
                The current version of the message.
            """

        async def on_raw_message_edit(self, payload: discord.RawMessageUpdateEvent):
            """|coro|
            Called when a message is edited. Unlike :meth:`on_message_edit`, this is called
            regardless of the state of the internal message cache.

            If the message is found in the message cache,
            it can be accessed via :attr:`~discord.RawMessageUpdateEvent.cached_message`

            Due to the inherently raw nature of this event, the data parameter coincides with
            the raw data given by the `gateway <https://discord.com/developers/docs/topics/gateway#message-update>`_.

            Since the data payload can be partial, care must be taken when accessing stuff in the dictionary.
            One example of a common case of partial data is when the ``'content'`` key is inaccessible. This
            denotes an "embed" only edit, which is an edit in which only the embeds are updated by the Discord
            embed server.

            Parameters
            ------------
            payload: :class:`~discord.RawMessageUpdateEvent`
                The raw event payload data.
            """

        async def on_reaction_add(self, reaction: discord.Reaction, user: Users):
            """|coro|
            Called when a message has a reaction added to it. Similar to :meth:`on_message_edit`,
            if the message is not found in the internal message cache, then this
            event will not be called. Consider using :meth:`on_raw_reaction_add` instead.

            .. note::

                To get the :class:`~discord.Message` being reacted, access it via :attr:`~discord.Reaction.message`.

            Parameters
            ------------
            reaction: :class:`~discord.Reaction`
                The current state of the reaction.
            user: Union[:class:`~discord.Member`, :class:`~discord.User`]
                The user who added the reaction.
            """

        async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
            """|coro|
            Called when a message has a reaction added. Unlike :meth:`on_reaction_add`, this is
            called regardless of the state of the internal message cache.

            Parameters
            ------------
            payload: :class:`~discord.RawReactionActionEvent`
                The raw event payload data.
            """

        async def on_reaction_remove(self, reaction: discord.Reaction, user: Users):
            """|coro|
            Called when a message has a reaction removed from it. Similar to on_message_edit,
            if the message is not found in the internal message cache, then this event
            will not be called.

            .. note::

                To get the message being reacted, access it via :attr:`Reaction.message`.

            Parameters
            ------------
            reaction: :class:`~discord.Reaction`
                The current state of the reaction.
            user: Union[:class:`~discord.Member`, :class:`~discord.User`]
                The user who added the reaction.
            """

        async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
            """|coro|
            Called when a message has a reaction removed. Unlike :meth:`on_reaction_remove`, this is
            called regardless of the state of the internal message cache.

            Parameters
            ------------
            payload: :class:`~discord.RawReactionActionEvent`
                The raw event payload data.
            """

        async def on_reaction_clear(self, message: discord.Message, reactions: List[discord.Reaction]):
            """|coro|
            Called when a message has all its reactions removed from it. Similar to :meth:`on_message_edit`,
            if the message is not found in the internal message cache, then this event
            will not be called. Consider using :meth:`on_raw_reaction_clear` instead.

            Parameters
            ------------
            message: :class:`~discord.Message`
                The message that had its reactions cleared.
            reactions: List[:class:`~discord.Reaction`]
                The reactions that were removed.
            """

        async def on_raw_reaction_clear(self, payload):
            """|coro|
            Called when a message has all its reactions removed. Unlike :meth:`on_reaction_clear`,
            this is called regardless of the state of the internal message cache.

            Parameters
            ------------
            payload: :class:`~discord.RawReactionClearEvent`
                The raw event payload data.
            """

        async def on_reaction_clear_emoji(self, reaction: discord.Reaction):
            """|coro|
            Called when a message has a specific reaction removed from it. Similar to :meth:`on_message_edit`,
            if the message is not found in the internal message cache, then this event
            will not be called. Consider using :meth:`on_raw_reaction_clear_emoji` instead.

            .. versionadded:: 1.3

            Parameters
            ------------
            reaction: :class:`~discord.Reaction`
                The reaction that got cleared.
            """

        async def on_raw_reaction_clear_emoji(self, payload: discord.RawReactionClearEmojiEvent):
            """|coro|
            Called when a message has a specific reaction removed from it.
            Unlike :meth:`on_reaction_clear_emoji` this is called
            regardless of the state of the internal message cache.

            .. versionadded:: 1.3

            Parameters
            ------------
            payload: :class:`~discord.RawReactionClearEmojiEvent`
                The raw event payload data.
            """

        async def on_private_channel_delete(self, channel: discord.abc.PrivateChannel):
            """|coro|
            Called whenever a private channel is deleted.

            Parameters
            ------------
            channel: :class:`~discord.abc.PrivateChannel`
                The private channel that got deleted.
            """

        async def on_private_channel_create(self, channel: discord.abc.PrivateChannel):
            """|coro|
            Called whenever a private channel is created.

            Parameters
            ------------
            channel: :class:`~discord.abc.PrivateChannel`
                The private channel that got created.
            """

        async def on_private_channel_update(self, before: discord.abc.PrivateChannel, after: discord.abc.PrivateChannel):
            """|coro|
            Called whenever a private group DM is updated. e.g. changed name or topic.

            Parameters
            ------------
            before: :class:`~discord.GroupChannel`
                The updated group channel's old info.
            after: :class:`~discord.GroupChannel`
                The updated group channel's new info.
            """

        async def on_private_channel_pins_update(self, channel: discord.abc.PrivateChannel, last_pin: Optional[datetime]):
            """|coro|
            Called whenever a message is pinned or unpinned from a private channel.

            Parameters
            ------------
            channel: :class:`~discord.abc.PrivateChannel`
                The private channel that had its pins updated.
            last_pin: Optional[:class:`~discord.datetime.datetime`]
                The latest message that was pinned as a naive datetime in UTC. Could be ``None``.
            """

        async def on_guild_channel_delete(self, channel: discord.abc.GuildChannel):
            """|coro|
            Called whenever a guild channel is deleted.

            Note that you can get the guild from :attr:`~abc.GuildChannel.guild`.

            Parameters
            ------------
            channel: :class:`~discord.abc.GuildChannel`
                The guild channel that got deleted.
            """

        async def on_guild_channel_create(self, channel: discord.abc.GuildChannel):
            """|coro|
            Called whenever a guild channel is created.

            Note that you can get the guild from :attr:`~abc.GuildChannel.guild`.

            Parameters
            ------------
            channel: :class:`~discord.abc.GuildChannel`
                The guild channel that got created.
            """

        async def on_guild_channel_update(self, before: discord.abc.GuildChannel, after: discord.abc.GuildChannel):
            """|coro|
            Called whenever a guild channel is updated. e.g. changed name, topic, permissions.

            Parameters
            ------------
            before: :class:`~discord.abc.GuildChannel`
                The updated guild channel's old info.
            after: :class:`~discord.abc.GuildChannel`
                The updated guild channel's new info.
            """

        async def on_guild_channel_pins_update(self, channel: discord.abc.GuildChannel, last_pin: Optional[datetime]):
            """|coro|
            Called whenever a message is pinned or unpinned from a guild channel.

            Parameters
            ------------
            channel: :class:`~discord.abc.GuildChannel`
                The guild channel that had its pins updated.
            last_pin: Optional[:class:`~discord.datetime.datetime`]
                The latest message that was pinned as a naive datetime in UTC. Could be ``None``.
            """

        async def on_guild_integrations_update(self, guild: discord.Guild):
            """|coro|
            Called whenever an integration is created, modified, or removed from a guild.

            Parameters
            ------------
            guild: :class:`~discord.Guild`
                The guild that had its integrations updated.
            """

        async def on_webhooks_update(self, channel: discord.abc.GuildChannel):
            """|coro|
            Called whenever a webhook is created, modified, or removed from a guild channel.

            Parameters
            ------------
            channel: :class:`~discord.abc.GuildChannel`
                The channel that had its webhooks updated.
            """

        async def on_member_join(self, member: discord.Member):
            """|coro|
            Called when a :class:`~discord.Member` joins a :class:`~discord.Guild`.

            Parameters
            ------------
            member: :class:`~discord.Member`
                The member who joined.
            """

        async def on_member_remove(self, member: discord.Member):
            """|coro|
            Called when a :class:`~discord.Member` leaves a :class:`~discord.Guild`.

            Parameters
            ------------
            member: :class:`~discord.Member`
                The member who left.
            """

        async def on_member_update(self, before: discord.Member, after: discord.Member):
            """|coro|
            Called when a :class:`~discord.Member` updates their profile.

            This is called when one or more of the following things change:

            - status
            - activity
            - nickname
            - roles

            Parameters
            ------------
            before: :class:`~discord.Member`
                The updated member's old info.
            after: :class:`~discord.Member`
                The updated member's updated info.
            """

        async def on_user_update(self, before: discord.User, after: discord.User):
            """|coro|
            Called when a :class:`~discord.User` updates their profile.

            This is called when one or more of the following things change:

            - avatar
            - username
            - discriminator

            Parameters
            ------------
            before: :class:`~discord.User`
                The updated user's old info.
            after: :class:`~discord.User`
                The updated user's updated info.
            """

        async def on_guild_join(self, guild: discord.Guild):
            """|coro|
            Called when a :class:`~discord.Guild` is either created by the :class:`~discord.Client` or when the
            :class:`~discord.Client` joins a guild.

            Parameters
            ------------
            guild: :class:`~discord.Guild`
                The guild that was joined.
            """

        async def on_guild_remove(self, guild: discord.Guild):
            """|coro|
            Called when a :class:`~discord.Guild` is removed from the :class:`~discord.Client`.

            This happens through, but not limited to, these circumstances:

            - The client got banned.
            - The client got kicked.
            - The client left the guild.
            - The client or the guild owner deleted the guild.

            In order for this event to be invoked then the :class:`~discord.Client` must have
            been part of the guild to begin with. (i.e. it is part of :attr:`Client.guilds`)

            Parameters
            ------------
            guild: :class:`~discord.Guild`
                The guild that got removed.
            """

        async def on_guild_update(self, before: discord.Guild, after: discord.Guild):
            """|coro|
            Called when a :class:`~discord.Guild` updates, for example:

            - Changed name
            - Changed AFK channel
            - Changed AFK timeout
            - etc

            Parameters
            ------------
            before: :class:`~discord.Guild`
                The guild prior to being updated.
            after: :class:`~discord.Guild`
                The guild after being updated.
            """

        async def on_guild_role_create(self, role: discord.Role):
            """|coro|
            Called when a :class:`~discord.Guild` creates or deletes a new :class:`~discord.Role`.

            To get the guild it belongs to, use :attr:`Role.guild`.

            Parameters
            ------------
            role: :class:`~discord.Role`
                The role that was created or deleted.
            """

        async def on_guild_role_delete(self, role: discord.Role):
            """|coro|
            Called when a :class:`~discord.Guild` creates or deletes a new :class:`~discord.Role`.

            To get the guild it belongs to, use :attr:`Role.guild`.

            Parameters
            ------------
            role: :class:`~discord.Role`
                The role that was created or deleted.
            """

        async def on_guild_role_update(self, before: discord.Role, after: discord.Role):
            """|coro|
            Called when a :class:`~discord.Role` is changed guild-wide.

            Parameters
            ------------
            before: :class:`~discord.Role`
                The updated role's old info.
            after: :class:`~discord.Role`
                The updated role's updated info.
            """

        async def on_guild_emojis_update(self, guild: discord.Guild, before: List[discord.Emoji], after: List[discord.Emoji]):
            """|coro|
            Called when a :class:`~discord.Guild` adds or removes :class:`~discord.Emoji`.

            Parameters
            ------------
            guild: :class:`~discord.Guild`
                The guild who got their emojis updated.
            before: Sequence[:class:`~discord.Emoji`]
                A list of emojis before the update.
            after: Sequence[:class:`~discord.Emoji`]
                A list of emojis after the update.
            """

        async def on_guild_available(self, guild: discord.Guild):
            """|coro|
            Called when a guild becomes available. The guild must have
            existed in the :attr:`Client.guilds` cache.

            Parameters
            ------------
            guild: :class:`~discord.Guild`
                The guild that has changed availability.
            """

        async def on_guild_unavailable(self, guild: discord.Guild):
            """|coro|
            Called when a guild becomes unavailable. The guild must have
            existed in the :attr:`Client.guilds` cache.

            Parameters
            ------------
            guild: :class:`~discord.Guild`
                The guild that has changed availability.
            """

        async def on_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
            """|coro|
            Called when a :class:`~discord.Member` changes their :class:`~discord.VoiceState`.

            The following, but not limited to, examples illustrate when this event is called:

            - A member joins a voice channel.
            - A member leaves a voice channel.
            - A member is muted or deafened by their own accord.
            - A member is muted or deafened by a guild administrator.

            Parameters
            ------------
            member: :class:`~discord.Member`
                The member whose voice states changed.
            before: :class:`~discord.VoiceState`
                The voice state prior to the changes.
            after: :class:`~discord.VoiceState`
                The voice state after to the changes.
            """

        async def on_member_ban(self, guild: discord.Guild, user: Users):
            """|coro|
            Called when user gets banned from a :class:`~discord.Guild`.

            Parameters
            ------------
            guild: :class:`~discord.Guild`
                The guild the user got banned from.
            user: Union[:class:`~discord.User`, :class:`~discord.Member`]
                The user that got banned.
                Can be either :class:`~discord.User` or :class:`~discord.Member` depending if
                the user was in the guild or not at the time of removal.
            """

        async def on_member_unban(self, guild: discord.Guild, user: discord.User):
            """|coro|
            Called when a :class:`~discord.User` gets unbanned from a :class:`~discord.Guild`.

            Parameters
            ------------
            guild: :class:`~discord.Guild`
                The guild the user got unbanned from.
            user: :class:`~discord.User`
                The user that got unbanned.
            """

        async def on_invite_create(self, invite: discord.Invite):
            """|coro|
            Called when an :class:`~discord.Invite` is created.
            You must have the :attr:`~Permissions.manage_channels` permission to receive this.

            .. versionadded:: 1.3

            .. note::

                There is a rare possibility that the :attr:`Invite.guild` and :attr:`Invite.channel`
                attributes will be of :class:`~discord.Object` rather than the respective models.

            Parameters
            ------------
            invite: :class:`~discord.Invite`
                The invite that was created.
            """

        async def on_invite_delete(self, invite: discord.Invite):
            """|coro|
            Called when an :class:`~discord.Invite` is deleted.
            You must have the :attr:`~Permissions.manage_channels` permission to receive this.

            .. versionadded:: 1.3

            .. note::

                There is a rare possibility that the :attr:`Invite.guild` and :attr:`Invite.channel`
                attributes will be of :class:`~discord.Object` rather than the respective models.

                Outside of those two attributes, the only other attribute guaranteed to be
                filled by the Discord gateway for this event is :attr:`Invite.code`.

            Parameters
            ------------
            invite: :class:`~discord.Invite`
                The invite that was deleted.
            """

        async def on_group_join(self, channel: discord.GroupChannel, user: discord.User):
            """|coro|
            Called when someone joins or leaves a :class:`~discord.GroupChannel`.

            Parameters
            ------------
            channel: :class:`~discord.GroupChannel`
                The group that the user joined or left.
            user: :class:`~discord.User`
                The user that joined or left.
            """

        async def on_group_remove(self, channel: discord.GroupChannel, user: discord.User):
            """|coro|
            Called when someone joins or leaves a :class:`~discord.GroupChannel`.

            Parameters
            ------------
            channel: :class:`~discord.GroupChannel`
                The group that the user joined or left.
            user: :class:`~discord.User`
                The user that joined or left.
            """

        async def on_relationship_add(self, relationship: discord.Relationship):
            """|coro|
            Called when a :class:`~discord.Relationship` is added or removed from the
            :class:`~discord.ClientUser`.

            Parameters
            ------------
            relationship: :class:`~discord.Relationship`
                The relationship that was added or removed.
            """

        async def on_relationship_remove(self, relationship: discord.Relationship):
            """|coro|
            Called when a :class:`~discord.Relationship` is added or removed from the
            :class:`~discord.ClientUser`.

            Parameters
            ------------
            relationship: :class:`~discord.Relationship`
                The relationship that was added or removed.
            """

        async def on_relationship_update(self, before: discord.Relationship, after: discord.Relationship):
            """Called when a :class:`~discord.Relationship` is updated, e.g. when you
            block a friend or a friendship is accepted.

            Parameters
            ------------
            before: :class:`~discord.Relationship`
                The previous relationship status.
            after: :class:`~discord.Relationship`
                The updated relationship status.
            """


class Bot(Client, commands.Bot):  # FIXME needs to be edited before release
    if TYPE_CHECKING:
        async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
            """|coro|
            An error handler that is called when an error is raised
            inside a command either through user input error, check
            failure, or an error in your own code.

            A default one is provided (:meth:`.Bot.on_command_error`).

            Parameters
            -----------
            ctx: :class:`.Context`
                The invocation context.
            error: :class:`.CommandError` derived
                The error that was raised.
            """

        async def on_command(self, ctx: commands.Context):
            """|coro|
            An event that is called when a command is found and is about to be invoked.

            This event is called regardless of whether the command itself succeeds via
            error or completes.

            Parameters
            -----------
            ctx: :class:`.Context`
                The invocation context.
            """

        async def on_command_completion(self, ctx: commands.Context):
            """|coro|
            An event that is called when a command has completed its invocation.

            This event is called only if the command succeeded, i.e. all checks have
            passed and the user input it correctly.

            Parameters
            -----------
            ctx: :class:`.Context`
                The invocation context."""
