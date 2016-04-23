# -*- coding: utf-8 -*-

"""
pytbo.types
~~~~~~~~~~~

This module implements wrapper classes for Telegram Bot API types.

:copyright: (c) 2016 by Alessandro Costa.
:license: Apache2, see LICENSE for more details.

"""

import json

def req_plain_param(name, data, param_class=None):
    if param_class is None:
        return data[name]
    return param_class.from_dict(data[name])

def req_array_param(name, data, param_class):
    return [ param_class.from_dict(p) for p in data[name] ]

def req_array_array_param(name, data, param_class):
    return [ [ param_class.from_dict(p) for p in a ] for a in data[name] ]

def opt_plain_param(name, data, param_class=None):
    if param_class is None:
        return None if name not in data else data[name]
    return None if name not in data else param_class.from_dict(data[name])

def opt_array_param(name, data, param_class):
    return None if name not in data else [ param_class.from_dict(p) for p in data[name] ]

def opt_array_array_param(name, data, param_class):
    return None if name not in data else [ [ param_class.from_dict(p) for p in a ] for a in data[name] ]

class Update(object):
    """
    An incoming update.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#update>`_.
    """

    def __init__(self,
            update_id,
            message=None,
            inline_query=None,
            chosen_inline_result=None,
            callback_query=None):
        self.update_id = update_id
        self.message = message
        self.inline_query = inline_query
        self.chosen_inline_result = chosen_inline_result
        self.callback_query = callback_query

    def from_dict(obj_dict):
        """Builds Update object from Python dict."""
        return Update(
                update_id=req_plain_param('update_id', obj_dict),
                message=opt_plain_param('message', obj_dict, Message),
                inline_query=opt_plain_param('inline_query', obj_dict, InlineQuery),
                chosen_inline_result=opt_plain_param('chosen_inline_result', obj_dict, ChosenInlineResult),
                callback_query=opt_plain_param('callback_query', obj_dict, CallbackQuery)
            )

    def from_json(json_str):
        """Builds Update object from JSON string."""
        jdata = json.loads(json_str)
        return Update.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from Update object."""
        obj_dict = {
            'update_id': self.update_id
        }
        if self.message is not None:
           obj_dict['message'] = self.message.to_dict()
        if self.inline_query is not None:
           obj_dict['inline_query'] = self.inline_query.to_dict()
        if self.chosen_inline_result is not None:
           obj_dict['chosen_inline_result'] = self.chosen_inline_result.to_dict()
        if self.callback_query is not None:
           obj_dict['callback_query'] = self.callback_query.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from Update object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class User(object):
    """
    A Telegram user or bot.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#user>`_.
    """

    def __init__(self,
            id,
            first_name,
            last_name=None,
            username=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def from_dict(obj_dict):
        """Builds User object from Python dict."""
        return User(
                id=req_plain_param('id', obj_dict),
                first_name=req_plain_param('first_name', obj_dict),
                last_name=opt_plain_param('last_name', obj_dict),
                username=opt_plain_param('username', obj_dict)
            )

    def from_json(json_str):
        """Builds User object from JSON string."""
        jdata = json.loads(json_str)
        return User.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from User object."""
        obj_dict = {
            'id': self.id,
            'first_name': self.first_name
        }
        if self.last_name is not None:
           obj_dict['last_name'] = self.last_name
        if self.username is not None:
           obj_dict['username'] = self.username
        return obj_dict

    def to_json(self):
        """Returns JSON string from User object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class Chat(object):
    """
    A chat.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#chat>`_.
    """

    def __init__(self,
            id,
            type,
            title=None,
            username=None,
            first_name=None,
            last_name=None):
        self.id = id
        self.type = type
        self.title = title
        self.username = username
        self.first_name = first_name
        self.last_name = last_name

    def from_dict(obj_dict):
        """Builds Chat object from Python dict."""
        return Chat(
                id=req_plain_param('id', obj_dict),
                type=req_plain_param('type', obj_dict),
                title=opt_plain_param('title', obj_dict),
                username=opt_plain_param('username', obj_dict),
                first_name=opt_plain_param('first_name', obj_dict),
                last_name=opt_plain_param('last_name', obj_dict)
            )

    def from_json(json_str):
        """Builds Chat object from JSON string."""
        jdata = json.loads(json_str)
        return Chat.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from Chat object."""
        obj_dict = {
            'id': self.id,
            'type': self.type
        }
        if self.title is not None:
           obj_dict['title'] = self.title
        if self.username is not None:
           obj_dict['username'] = self.username
        if self.first_name is not None:
           obj_dict['first_name'] = self.first_name
        if self.last_name is not None:
           obj_dict['last_name'] = self.last_name
        return obj_dict

    def to_json(self):
        """Returns JSON string from Chat object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class Message(object):
    """
    A message.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#message>`_.
    """

    def __init__(self,
            message_id,
            date,
            chat,
            sender=None,
            forward_from=None,
            forward_date=None,
            reply_to_message=None,
            text=None,
            entities=None,
            audio=None,
            document=None,
            photo=None,
            sticker=None,
            video=None,
            voice=None,
            caption=None,
            contact=None,
            location=None,
            venue=None,
            new_chat_member=None,
            left_chat_member=None,
            new_chat_title=None,
            new_chat_photo=None,
            delete_chat_photo=None,
            group_chat_created=None,
            supergroup_chat_created=None,
            channel_chat_created=None,
            migrate_to_chat_id=None,
            migrate_from_chat_id=None,
            pinned_message=None):
        self.message_id = message_id
        self.date = date
        self.chat = chat
        self.sender = sender
        self.forward_from = forward_from
        self.forward_date = forward_date
        self.reply_to_message = reply_to_message
        self.text = text
        self.entities = entities
        self.audio = audio
        self.document = document
        self.photo = photo
        self.sticker = sticker
        self.video = video
        self.voice = voice
        self.caption = caption
        self.contact = contact
        self.location = location
        self.venue = venue
        self.new_chat_member = new_chat_member
        self.left_chat_member = left_chat_member
        self.new_chat_title = new_chat_title
        self.new_chat_photo = new_chat_photo
        self.delete_chat_photo = delete_chat_photo
        self.group_chat_created = group_chat_created
        self.supergroup_chat_created = supergroup_chat_created
        self.channel_chat_created = channel_chat_created
        self.migrate_to_chat_id = migrate_to_chat_id
        self.migrate_from_chat_id = migrate_from_chat_id
        self.pinned_message = pinned_message

    def from_dict(obj_dict):
        """Builds Message object from Python dict."""
        return Message(
                message_id=req_plain_param('message_id', obj_dict),
                date=req_plain_param('date', obj_dict),
                chat=req_plain_param('chat', obj_dict, Chat),
                sender=opt_plain_param('from', obj_dict, User),
                forward_from=opt_plain_param('forward_from', obj_dict, User),
                forward_date=opt_plain_param('forward_date', obj_dict),
                reply_to_message=opt_plain_param('reply_to_message', obj_dict, Message),
                text=opt_plain_param('text', obj_dict),
                entities=opt_array_param('entities', obj_dict, MessageEntity),
                audio=opt_plain_param('audio', obj_dict, Audio),
                document=opt_plain_param('document', obj_dict, Document),
                photo=opt_array_param('photo', obj_dict, PhotoSize),
                sticker=opt_plain_param('sticker', obj_dict, Sticker),
                video=opt_plain_param('video', obj_dict, Video),
                voice=opt_plain_param('voice', obj_dict, Voice),
                caption=opt_plain_param('caption', obj_dict),
                contact=opt_plain_param('contact', obj_dict, Contact),
                location=opt_plain_param('location', obj_dict, Location),
                venue=opt_plain_param('venue', obj_dict, Venue),
                new_chat_member=opt_plain_param('new_chat_member', obj_dict, User),
                left_chat_member=opt_plain_param('left_chat_member', obj_dict, User),
                new_chat_title=opt_plain_param('new_chat_title', obj_dict),
                new_chat_photo=opt_array_param('new_chat_photo', obj_dict, PhotoSize),
                delete_chat_photo=opt_plain_param('delete_chat_photo', obj_dict),
                group_chat_created=opt_plain_param('group_chat_created', obj_dict),
                supergroup_chat_created=opt_plain_param('supergroup_chat_created', obj_dict),
                channel_chat_created=opt_plain_param('channel_chat_created', obj_dict),
                migrate_to_chat_id=opt_plain_param('migrate_to_chat_id', obj_dict),
                migrate_from_chat_id=opt_plain_param('migrate_from_chat_id', obj_dict),
                pinned_message=opt_plain_param('pinned_message', obj_dict, Message)
            )

    def from_json(json_str):
        """Builds Message object from JSON string."""
        jdata = json.loads(json_str)
        return Message.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from Message object."""
        obj_dict = {
            'message_id': self.message_id,
            'date': self.date,
            'chat': self.chat.to_dict()
        }
        if self.sender is not None:
           obj_dict['from'] = self.sender.to_dict()
        if self.forward_from is not None:
           obj_dict['forward_from'] = self.forward_from.to_dict()
        if self.forward_date is not None:
           obj_dict['forward_date'] = self.forward_date
        if self.reply_to_message is not None:
           obj_dict['reply_to_message'] = self.reply_to_message.to_dict()
        if self.text is not None:
           obj_dict['text'] = self.text
        if self.entities is not None:
           obj_dict['entities'] = [ e.to_dict() for e in self.entities ]
        if self.audio is not None:
           obj_dict['audio'] = self.audio.to_dict()
        if self.document is not None:
           obj_dict['document'] = self.document.to_dict()
        if self.photo is not None:
           obj_dict['photo'] = [ e.to_dict() for e in self.photo ]
        if self.sticker is not None:
           obj_dict['sticker'] = self.sticker.to_dict()
        if self.video is not None:
           obj_dict['video'] = self.video.to_dict()
        if self.voice is not None:
           obj_dict['voice'] = self.voice.to_dict()
        if self.caption is not None:
           obj_dict['caption'] = self.caption
        if self.contact is not None:
           obj_dict['contact'] = self.contact.to_dict()
        if self.location is not None:
           obj_dict['location'] = self.location.to_dict()
        if self.venue is not None:
           obj_dict['venue'] = self.venue.to_dict()
        if self.new_chat_member is not None:
           obj_dict['new_chat_member'] = self.new_chat_member.to_dict()
        if self.left_chat_member is not None:
           obj_dict['left_chat_member'] = self.left_chat_member.to_dict()
        if self.new_chat_title is not None:
           obj_dict['new_chat_title'] = self.new_chat_title
        if self.new_chat_photo is not None:
           obj_dict['new_chat_photo'] = [ e.to_dict() for e in self.new_chat_photo ]
        if self.delete_chat_photo is not None:
           obj_dict['delete_chat_photo'] = self.delete_chat_photo
        if self.group_chat_created is not None:
           obj_dict['group_chat_created'] = self.group_chat_created
        if self.supergroup_chat_created is not None:
           obj_dict['supergroup_chat_created'] = self.supergroup_chat_created
        if self.channel_chat_created is not None:
           obj_dict['channel_chat_created'] = self.channel_chat_created
        if self.migrate_to_chat_id is not None:
           obj_dict['migrate_to_chat_id'] = self.migrate_to_chat_id
        if self.migrate_from_chat_id is not None:
           obj_dict['migrate_from_chat_id'] = self.migrate_from_chat_id
        if self.pinned_message is not None:
           obj_dict['pinned_message'] = self.pinned_message.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from Message object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class MessageEntity(object):
    """
    A special entity in a text message (hashtag, username, URL, ...).

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#messageentity>`_.
    """

    def __init__(self,
            type,
            offset,
            length,
            url=None):
        self.type = type
        self.offset = offset
        self.length = length
        self.url = url

    def from_dict(obj_dict):
        """Builds MessageEntity object from Python dict."""
        return MessageEntity(
                type=req_plain_param('type', obj_dict),
                offset=req_plain_param('offset', obj_dict),
                length=req_plain_param('length', obj_dict),
                url=opt_plain_param('url', obj_dict)
            )

    def from_json(json_str):
        """Builds MessageEntity object from JSON string."""
        jdata = json.loads(json_str)
        return MessageEntity.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from MessageEntity object."""
        obj_dict = {
            'type': self.type,
            'offset': self.offset,
            'length': self.length
        }
        if self.url is not None:
           obj_dict['url'] = self.url
        return obj_dict

    def to_json(self):
        """Returns JSON string from MessageEntity object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class PhotoSize(object):
    """
    This object represents one size of a photo or a file / sticker thumbnail.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#photosize>`_.
    """

    def __init__(self,
            file_id,
            width,
            height,
            file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.file_size = file_size

    def from_dict(obj_dict):
        """Builds PhotoSize object from Python dict."""
        return PhotoSize(
                file_id=req_plain_param('file_id', obj_dict),
                width=req_plain_param('width', obj_dict),
                height=req_plain_param('height', obj_dict),
                file_size=opt_plain_param('file_size', obj_dict)
            )

    def from_json(json_str):
        """Builds PhotoSize object from JSON string."""
        jdata = json.loads(json_str)
        return PhotoSize.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from PhotoSize object."""
        obj_dict = {
            'file_id': self.file_id,
            'width': self.width,
            'height': self.height
        }
        if self.file_size is not None:
           obj_dict['file_size'] = self.file_size
        return obj_dict

    def to_json(self):
        """Returns JSON string from PhotoSize object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class Audio(object):
    """
    An audio file to be treated as music by the Telegram clients.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#audio>`_.
    """

    def __init__(self,
            file_id,
            duration,
            performer=None,
            title=None,
            mime_type=None,
            file_size=None):
        self.file_id = file_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.mime_type = mime_type
        self.file_size = file_size

    def from_dict(obj_dict):
        """Builds Audio object from Python dict."""
        return Audio(
                file_id=req_plain_param('file_id', obj_dict),
                duration=req_plain_param('duration', obj_dict),
                performer=opt_plain_param('performer', obj_dict),
                title=opt_plain_param('title', obj_dict),
                mime_type=opt_plain_param('mime_type', obj_dict),
                file_size=opt_plain_param('file_size', obj_dict)
            )

    def from_json(json_str):
        """Builds Audio object from JSON string."""
        jdata = json.loads(json_str)
        return Audio.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from Audio object."""
        obj_dict = {
            'file_id': self.file_id,
            'duration': self.duration
        }
        if self.performer is not None:
           obj_dict['performer'] = self.performer
        if self.title is not None:
           obj_dict['title'] = self.title
        if self.mime_type is not None:
           obj_dict['mime_type'] = self.mime_type
        if self.file_size is not None:
           obj_dict['file_size'] = self.file_size
        return obj_dict

    def to_json(self):
        """Returns JSON string from Audio object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class Document(object):
    """
    A general file (as opposed to photos, voice messages and audio files).

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#document>`_.
    """

    def __init__(self,
            file_id,
            thumb=None,
            file_name=None,
            mime_type=None,
            file_size=None):
        self.file_id = file_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size

    def from_dict(obj_dict):
        """Builds Document object from Python dict."""
        return Document(
                file_id=req_plain_param('file_id', obj_dict),
                thumb=opt_plain_param('thumb', obj_dict, PhotoSize),
                file_name=opt_plain_param('file_name', obj_dict),
                mime_type=opt_plain_param('mime_type', obj_dict),
                file_size=opt_plain_param('file_size', obj_dict)
            )

    def from_json(json_str):
        """Builds Document object from JSON string."""
        jdata = json.loads(json_str)
        return Document.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from Document object."""
        obj_dict = {
            'file_id': self.file_id
        }
        if self.thumb is not None:
           obj_dict['thumb'] = self.thumb.to_dict()
        if self.file_name is not None:
           obj_dict['file_name'] = self.file_name
        if self.mime_type is not None:
           obj_dict['mime_type'] = self.mime_type
        if self.file_size is not None:
           obj_dict['file_size'] = self.file_size
        return obj_dict

    def to_json(self):
        """Returns JSON string from Document object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class Sticker(object):
    """
    A sticker.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#sticker>`_.
    """

    def __init__(self,
            file_id,
            width,
            height,
            thumb=None,
            file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.thumb = thumb
        self.file_size = file_size

    def from_dict(obj_dict):
        """Builds Sticker object from Python dict."""
        return Sticker(
                file_id=req_plain_param('file_id', obj_dict),
                width=req_plain_param('width', obj_dict),
                height=req_plain_param('height', obj_dict),
                thumb=opt_plain_param('thumb', obj_dict, PhotoSize),
                file_size=opt_plain_param('file_size', obj_dict)
            )

    def from_json(json_str):
        """Builds Sticker object from JSON string."""
        jdata = json.loads(json_str)
        return Sticker.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from Sticker object."""
        obj_dict = {
            'file_id': self.file_id,
            'width': self.width,
            'height': self.height
        }
        if self.thumb is not None:
           obj_dict['thumb'] = self.thumb.to_dict()
        if self.file_size is not None:
           obj_dict['file_size'] = self.file_size
        return obj_dict

    def to_json(self):
        """Returns JSON string from Sticker object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class Video(object):
    """
    A video file.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#video>`_.
    """

    def __init__(self,
            file_id,
            width,
            height,
            duration,
            thumb=None,
            mime_type=None,
            file_size=None):
        self.file_id = file_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = thumb
        self.mime_type = mime_type
        self.file_size = file_size

    def from_dict(obj_dict):
        """Builds Video object from Python dict."""
        return Video(
                file_id=req_plain_param('file_id', obj_dict),
                width=req_plain_param('width', obj_dict),
                height=req_plain_param('height', obj_dict),
                duration=req_plain_param('duration', obj_dict),
                thumb=opt_plain_param('thumb', obj_dict, PhotoSize),
                mime_type=opt_plain_param('mime_type', obj_dict),
                file_size=opt_plain_param('file_size', obj_dict)
            )

    def from_json(json_str):
        """Builds Video object from JSON string."""
        jdata = json.loads(json_str)
        return Video.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from Video object."""
        obj_dict = {
            'file_id': self.file_id,
            'width': self.width,
            'height': self.height,
            'duration': self.duration
        }
        if self.thumb is not None:
           obj_dict['thumb'] = self.thumb.to_dict()
        if self.mime_type is not None:
           obj_dict['mime_type'] = self.mime_type
        if self.file_size is not None:
           obj_dict['file_size'] = self.file_size
        return obj_dict

    def to_json(self):
        """Returns JSON string from Video object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class Voice(object):
    """
    A voice note.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#voice>`_.
    """

    def __init__(self,
            file_id,
            duration,
            mime_type=None,
            file_size=None):
        self.file_id = file_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size

    def from_dict(obj_dict):
        """Builds Voice object from Python dict."""
        return Voice(
                file_id=req_plain_param('file_id', obj_dict),
                duration=req_plain_param('duration', obj_dict),
                mime_type=opt_plain_param('mime_type', obj_dict),
                file_size=opt_plain_param('file_size', obj_dict)
            )

    def from_json(json_str):
        """Builds Voice object from JSON string."""
        jdata = json.loads(json_str)
        return Voice.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from Voice object."""
        obj_dict = {
            'file_id': self.file_id,
            'duration': self.duration
        }
        if self.mime_type is not None:
           obj_dict['mime_type'] = self.mime_type
        if self.file_size is not None:
           obj_dict['file_size'] = self.file_size
        return obj_dict

    def to_json(self):
        """Returns JSON string from Voice object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class Contact(object):
    """
    A phone contact.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#contact>`_.
    """

    def __init__(self,
            phone_number,
            first_name,
            last_name=None,
            user_id=None):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id

    def from_dict(obj_dict):
        """Builds Contact object from Python dict."""
        return Contact(
                phone_number=req_plain_param('phone_number', obj_dict),
                first_name=req_plain_param('first_name', obj_dict),
                last_name=opt_plain_param('last_name', obj_dict),
                user_id=opt_plain_param('user_id', obj_dict)
            )

    def from_json(json_str):
        """Builds Contact object from JSON string."""
        jdata = json.loads(json_str)
        return Contact.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from Contact object."""
        obj_dict = {
            'phone_number': self.phone_number,
            'first_name': self.first_name
        }
        if self.last_name is not None:
           obj_dict['last_name'] = self.last_name
        if self.user_id is not None:
           obj_dict['user_id'] = self.user_id
        return obj_dict

    def to_json(self):
        """Returns JSON string from Contact object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class Location(object):
    """
    A point on the map.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#location>`_.
    """

    def __init__(self,
            longitude,
            latitude):
        self.longitude = longitude
        self.latitude = latitude

    def from_dict(obj_dict):
        """Builds Location object from Python dict."""
        return Location(
                longitude=req_plain_param('longitude', obj_dict),
                latitude=req_plain_param('latitude', obj_dict)
            )

    def from_json(json_str):
        """Builds Location object from JSON string."""
        jdata = json.loads(json_str)
        return Location.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from Location object."""
        obj_dict = {
            'longitude': self.longitude,
            'latitude': self.latitude
        }
        return obj_dict

    def to_json(self):
        """Returns JSON string from Location object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class Venue(object):
    """
    A venue.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#venue>`_.
    """

    def __init__(self,
            location,
            title,
            address,
            foursquare_id=None):
        self.location = location
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id

    def from_dict(obj_dict):
        """Builds Venue object from Python dict."""
        return Venue(
                location=req_plain_param('location', obj_dict, Location),
                title=req_plain_param('title', obj_dict),
                address=req_plain_param('address', obj_dict),
                foursquare_id=opt_plain_param('foursquare_id', obj_dict)
            )

    def from_json(json_str):
        """Builds Venue object from JSON string."""
        jdata = json.loads(json_str)
        return Venue.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from Venue object."""
        obj_dict = {
            'location': self.location.to_dict(),
            'title': self.title,
            'address': self.address
        }
        if self.foursquare_id is not None:
           obj_dict['foursquare_id'] = self.foursquare_id
        return obj_dict

    def to_json(self):
        """Returns JSON string from Venue object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class UserProfilePhotos(object):
    """
    A user's profile pictures.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#userprofilephotos>`_.
    """

    def __init__(self,
            total_count,
            photos):
        self.total_count = total_count
        self.photos = photos

    def from_dict(obj_dict):
        """Builds UserProfilePhotos object from Python dict."""
        return UserProfilePhotos(
                total_count=req_plain_param('total_count', obj_dict),
                photos=req_array_array_param('photos', obj_dict, PhotoSize)
            )

    def from_json(json_str):
        """Builds UserProfilePhotos object from JSON string."""
        jdata = json.loads(json_str)
        return UserProfilePhotos.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from UserProfilePhotos object."""
        obj_dict = {
            'total_count': self.total_count,
            'photos': [ [ e.to_dict() for e in a ] for a in self.photos ]
        }
        return obj_dict

    def to_json(self):
        """Returns JSON string from UserProfilePhotos object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class File(object):
    """
    A file ready to be downloaded.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#file>`_.
    """

    def __init__(self,
            file_id,
            file_size=None,
            file_path=None):
        self.file_id = file_id
        self.file_size = file_size
        self.file_path = file_path

    def from_dict(obj_dict):
        """Builds File object from Python dict."""
        return File(
                file_id=req_plain_param('file_id', obj_dict),
                file_size=opt_plain_param('file_size', obj_dict),
                file_path=opt_plain_param('file_path', obj_dict)
            )

    def from_json(json_str):
        """Builds File object from JSON string."""
        jdata = json.loads(json_str)
        return File.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from File object."""
        obj_dict = {
            'file_id': self.file_id
        }
        if self.file_size is not None:
           obj_dict['file_size'] = self.file_size
        if self.file_path is not None:
           obj_dict['file_path'] = self.file_path
        return obj_dict

    def to_json(self):
        """Returns JSON string from File object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class ReplyKeyboardMarkup(object):
    """
    A custom keyboard with reply options (see Introduction to bots for details and examples).

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#replykeyboardmarkup>`_.
    """

    def __init__(self,
            keyboard,
            resize_keyboard=None,
            one_time_keyboard=None,
            selective=None):
        self.keyboard = keyboard
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective

    def from_dict(obj_dict):
        """Builds ReplyKeyboardMarkup object from Python dict."""
        return ReplyKeyboardMarkup(
                keyboard=req_array_array_param('keyboard', obj_dict, KeyboardButton),
                resize_keyboard=opt_plain_param('resize_keyboard', obj_dict),
                one_time_keyboard=opt_plain_param('one_time_keyboard', obj_dict),
                selective=opt_plain_param('selective', obj_dict)
            )

    def from_json(json_str):
        """Builds ReplyKeyboardMarkup object from JSON string."""
        jdata = json.loads(json_str)
        return ReplyKeyboardMarkup.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from ReplyKeyboardMarkup object."""
        obj_dict = {
            'keyboard': [ [ e.to_dict() for e in a ] for a in self.keyboard ]
        }
        if self.resize_keyboard is not None:
           obj_dict['resize_keyboard'] = self.resize_keyboard
        if self.one_time_keyboard is not None:
           obj_dict['one_time_keyboard'] = self.one_time_keyboard
        if self.selective is not None:
           obj_dict['selective'] = self.selective
        return obj_dict

    def to_json(self):
        """Returns JSON string from ReplyKeyboardMarkup object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class KeyboardButton(object):
    """
    A button of the reply keyboard. Optional fields are mutually exclusive.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#keyboardbutton>`_.
    """

    def __init__(self,
            text,
            request_contact=None,
            request_location=None):
        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location

    def from_dict(obj_dict):
        """Builds KeyboardButton object from Python dict."""
        return KeyboardButton(
                text=req_plain_param('text', obj_dict),
                request_contact=opt_plain_param('request_contact', obj_dict),
                request_location=opt_plain_param('request_location', obj_dict)
            )

    def from_json(json_str):
        """Builds KeyboardButton object from JSON string."""
        jdata = json.loads(json_str)
        return KeyboardButton.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from KeyboardButton object."""
        obj_dict = {
            'text': self.text
        }
        if self.request_contact is not None:
           obj_dict['request_contact'] = self.request_contact
        if self.request_location is not None:
           obj_dict['request_location'] = self.request_location
        return obj_dict

    def to_json(self):
        """Returns JSON string from KeyboardButton object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class ReplyKeyboardHide(object):
    """
    Upon receiving a message with this object, Telegram clients will hide the current custom keyboard and display the default letter-keyboard.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#replykeyboardhide>`_.
    """

    def __init__(self,
            selective=None):
        self.hide_keyboard = True
        self.selective = selective

    def from_dict(obj_dict):
        """Builds ReplyKeyboardHide object from Python dict."""
        return ReplyKeyboardHide(
                selective=opt_plain_param('selective', obj_dict)
            )

    def from_json(json_str):
        """Builds ReplyKeyboardHide object from JSON string."""
        jdata = json.loads(json_str)
        return ReplyKeyboardHide.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from ReplyKeyboardHide object."""
        obj_dict = {
            'hide_keyboard': self.hide_keyboard
        }
        if self.selective is not None:
           obj_dict['selective'] = self.selective
        return obj_dict

    def to_json(self):
        """Returns JSON string from ReplyKeyboardHide object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineKeyboardMarkup(object):
    """
    An inline keyboard that appears right next to the message it belongs to.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinekeyboardmarkup>`_.
    """

    def __init__(self,
            inline_keyboard):
        self.inline_keyboard = inline_keyboard

    def from_dict(obj_dict):
        """Builds InlineKeyboardMarkup object from Python dict."""
        return InlineKeyboardMarkup(
                inline_keyboard=req_array_array_param('inline_keyboard', obj_dict, InlineKeyboardButton)
            )

    def from_json(json_str):
        """Builds InlineKeyboardMarkup object from JSON string."""
        jdata = json.loads(json_str)
        return InlineKeyboardMarkup.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineKeyboardMarkup object."""
        obj_dict = {
            'inline_keyboard': [ [ e.to_dict() for e in a ] for a in self.inline_keyboard ]
        }
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineKeyboardMarkup object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineKeyboardButton(object):
    """
    This object represents one button of an inline keyboard. You must use exactly one of the optional fields.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinekeyboardbutton>`_.
    """

    def __init__(self,
            text,
            url=None,
            callback_data=None,
            switch_inline_query=None):
        self.text = text
        self.url = url
        self.callback_data = callback_data
        self.switch_inline_query = switch_inline_query

    def from_dict(obj_dict):
        """Builds InlineKeyboardButton object from Python dict."""
        return InlineKeyboardButton(
                text=req_plain_param('text', obj_dict),
                url=opt_plain_param('url', obj_dict),
                callback_data=opt_plain_param('callback_data', obj_dict),
                switch_inline_query=opt_plain_param('switch_inline_query', obj_dict)
            )

    def from_json(json_str):
        """Builds InlineKeyboardButton object from JSON string."""
        jdata = json.loads(json_str)
        return InlineKeyboardButton.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineKeyboardButton object."""
        obj_dict = {
            'text': self.text
        }
        if self.url is not None:
           obj_dict['url'] = self.url
        if self.callback_data is not None:
           obj_dict['callback_data'] = self.callback_data
        if self.switch_inline_query is not None:
           obj_dict['switch_inline_query'] = self.switch_inline_query
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineKeyboardButton object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class CallbackQuery(object):
    """
    An incoming callback query from a callback button in an inline keyboard.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#callbackquery>`_.
    """

    def __init__(self,
            id,
            sender,
            message=None,
            inline_message_id=None,
            data=None):
        self.id = id
        self.sender = sender
        self.message = message
        self.inline_message_id = inline_message_id
        self.data = data

    def from_dict(obj_dict):
        """Builds CallbackQuery object from Python dict."""
        return CallbackQuery(
                id=req_plain_param('id', obj_dict),
                sender=req_plain_param('from', obj_dict, User),
                message=opt_plain_param('message', obj_dict, Message),
                inline_message_id=opt_plain_param('inline_message_id', obj_dict),
                data=opt_plain_param('data', obj_dict)
            )

    def from_json(json_str):
        """Builds CallbackQuery object from JSON string."""
        jdata = json.loads(json_str)
        return CallbackQuery.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from CallbackQuery object."""
        obj_dict = {
            'id': self.id,
            'from': self.sender.to_dict()
        }
        if self.message is not None:
           obj_dict['message'] = self.message.to_dict()
        if self.inline_message_id is not None:
           obj_dict['inline_message_id'] = self.inline_message_id
        if self.data is not None:
           obj_dict['data'] = self.data
        return obj_dict

    def to_json(self):
        """Returns JSON string from CallbackQuery object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class ForceReply(object):
    """
    Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot‘s message and tapped ’Reply').

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#forcereply>`_.
    """

    def __init__(self,
            selective=None):
        self.force_reply = True
        self.selective = selective

    def from_dict(obj_dict):
        """Builds ForceReply object from Python dict."""
        return ForceReply(
                selective=opt_plain_param('selective', obj_dict)
            )

    def from_json(json_str):
        """Builds ForceReply object from JSON string."""
        jdata = json.loads(json_str)
        return ForceReply.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from ForceReply object."""
        obj_dict = {
            'force_reply': self.force_reply
        }
        if self.selective is not None:
           obj_dict['selective'] = self.selective
        return obj_dict

    def to_json(self):
        """Returns JSON string from ForceReply object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQuery(object):
    """
    An incoming inline query.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequery>`_.
    """

    def __init__(self,
            id,
            sender,
            query,
            offset,
            location=None):
        self.id = id
        self.sender = sender
        self.location = location
        self.query = query
        self.offset = offset

    def from_dict(obj_dict):
        """Builds InlineQuery object from Python dict."""
        return InlineQuery(
                id=req_plain_param('id', obj_dict),
                sender=req_plain_param('from', obj_dict, User),
                query=req_plain_param('query', obj_dict),
                offset=req_plain_param('offset', obj_dict),
                location=opt_plain_param('location', obj_dict, Location)
            )

    def from_json(json_str):
        """Builds InlineQuery object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQuery.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQuery object."""
        obj_dict = {
            'id': self.id,
            'from': self.sender.to_dict(),
            'query': self.query,
            'offset': self.offset
        }
        if self.location is not None:
           obj_dict['location'] = self.location.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQuery object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultArticle(object):
    """
    An inline query result containing a link to an article or web page.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultarticle>`_.
    """

    def __init__(self,
            id,
            title,
            input_message_content,
            reply_markup=None,
            url=None,
            hide_url=None,
            description=None,
            thumb_url=None,
            thumb_width=None,
            thumb_height=None):
        self.type = 'article'
        self.id = id
        self.title = title
        self.input_message_content = input_message_content
        self.reply_markup = reply_markup
        self.url = url
        self.hide_url = hide_url
        self.description = description
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height

    def from_dict(obj_dict):
        """Builds InlineQueryResultArticle object from Python dict."""
        return InlineQueryResultArticle(
                id=req_plain_param('id', obj_dict),
                title=req_plain_param('title', obj_dict),
                input_message_content=req_plain_param('input_message_content', obj_dict, InputMessageContent),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                url=opt_plain_param('url', obj_dict),
                hide_url=opt_plain_param('hide_url', obj_dict),
                description=opt_plain_param('description', obj_dict),
                thumb_url=opt_plain_param('thumb_url', obj_dict),
                thumb_width=opt_plain_param('thumb_width', obj_dict),
                thumb_height=opt_plain_param('thumb_height', obj_dict)
            )

    def from_json(json_str):
        """Builds InlineQueryResultArticle object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultArticle.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultArticle object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'title': self.title,
            'input_message_content': self.input_message_content.to_dict()
        }
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.url is not None:
           obj_dict['url'] = self.url
        if self.hide_url is not None:
           obj_dict['hide_url'] = self.hide_url
        if self.description is not None:
           obj_dict['description'] = self.description
        if self.thumb_url is not None:
           obj_dict['thumb_url'] = self.thumb_url
        if self.thumb_width is not None:
           obj_dict['thumb_width'] = self.thumb_width
        if self.thumb_height is not None:
           obj_dict['thumb_height'] = self.thumb_height
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultArticle object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultPhoto(object):
    """
    An inline query result containing a link to a photo.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultphoto>`_.
    """

    def __init__(self,
            id,
            photo_url,
            thumb_url,
            photo_width=None,
            photo_height=None,
            title=None,
            description=None,
            caption=None,
            reply_markup=None,
            input_message_content=None):
        self.type = 'photo'
        self.id = id
        self.photo_url = photo_url
        self.thumb_url = thumb_url
        self.photo_width = photo_width
        self.photo_height = photo_height
        self.title = title
        self.description = description
        self.caption = caption
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def from_dict(obj_dict):
        """Builds InlineQueryResultPhoto object from Python dict."""
        return InlineQueryResultPhoto(
                id=req_plain_param('id', obj_dict),
                photo_url=req_plain_param('photo_url', obj_dict),
                thumb_url=req_plain_param('thumb_url', obj_dict),
                photo_width=opt_plain_param('photo_width', obj_dict),
                photo_height=opt_plain_param('photo_height', obj_dict),
                title=opt_plain_param('title', obj_dict),
                description=opt_plain_param('description', obj_dict),
                caption=opt_plain_param('caption', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent)
            )

    def from_json(json_str):
        """Builds InlineQueryResultPhoto object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultPhoto.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultPhoto object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'photo_url': self.photo_url,
            'thumb_url': self.thumb_url
        }
        if self.photo_width is not None:
           obj_dict['photo_width'] = self.photo_width
        if self.photo_height is not None:
           obj_dict['photo_height'] = self.photo_height
        if self.title is not None:
           obj_dict['title'] = self.title
        if self.description is not None:
           obj_dict['description'] = self.description
        if self.caption is not None:
           obj_dict['caption'] = self.caption
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultPhoto object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultGif(object):
    """
    An inline query result containing a link to an animated GIF file.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultgif>`_.
    """

    def __init__(self,
            id,
            gif_url,
            thumb_url,
            gif_width=None,
            gif_height=None,
            title=None,
            caption=None,
            reply_markup=None,
            input_message_content=None):
        self.type = 'gif'
        self.id = id
        self.gif_url = gif_url
        self.gif_width = gif_width
        self.gif_height = gif_height
        self.thumb_url = thumb_url
        self.title = title
        self.caption = caption
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def from_dict(obj_dict):
        """Builds InlineQueryResultGif object from Python dict."""
        return InlineQueryResultGif(
                id=req_plain_param('id', obj_dict),
                gif_url=req_plain_param('gif_url', obj_dict),
                thumb_url=req_plain_param('thumb_url', obj_dict),
                gif_width=opt_plain_param('gif_width', obj_dict),
                gif_height=opt_plain_param('gif_height', obj_dict),
                title=opt_plain_param('title', obj_dict),
                caption=opt_plain_param('caption', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent)
            )

    def from_json(json_str):
        """Builds InlineQueryResultGif object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultGif.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultGif object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'gif_url': self.gif_url,
            'thumb_url': self.thumb_url
        }
        if self.gif_width is not None:
           obj_dict['gif_width'] = self.gif_width
        if self.gif_height is not None:
           obj_dict['gif_height'] = self.gif_height
        if self.title is not None:
           obj_dict['title'] = self.title
        if self.caption is not None:
           obj_dict['caption'] = self.caption
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultGif object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultMpeg4Gif(object):
    """
    An inline query result containing a link to a video animation (H.264/MPEG-4 AVC video without sound).

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultmpeg4gif>`_.
    """

    def __init__(self,
            id,
            mpeg4_url,
            thumb_url,
            mpeg4_width=None,
            mpeg4_height=None,
            title=None,
            caption=None,
            reply_markup=None,
            input_message_content=None):
        self.type = 'mpeg4_gif'
        self.id = id
        self.mpeg4_url = mpeg4_url
        self.mpeg4_width = mpeg4_width
        self.mpeg4_height = mpeg4_height
        self.thumb_url = thumb_url
        self.title = title
        self.caption = caption
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def from_dict(obj_dict):
        """Builds InlineQueryResultMpeg4Gif object from Python dict."""
        return InlineQueryResultMpeg4Gif(
                id=req_plain_param('id', obj_dict),
                mpeg4_url=req_plain_param('mpeg4_url', obj_dict),
                thumb_url=req_plain_param('thumb_url', obj_dict),
                mpeg4_width=opt_plain_param('mpeg4_width', obj_dict),
                mpeg4_height=opt_plain_param('mpeg4_height', obj_dict),
                title=opt_plain_param('title', obj_dict),
                caption=opt_plain_param('caption', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent)
            )

    def from_json(json_str):
        """Builds InlineQueryResultMpeg4Gif object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultMpeg4Gif.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultMpeg4Gif object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'mpeg4_url': self.mpeg4_url,
            'thumb_url': self.thumb_url
        }
        if self.mpeg4_width is not None:
           obj_dict['mpeg4_width'] = self.mpeg4_width
        if self.mpeg4_height is not None:
           obj_dict['mpeg4_height'] = self.mpeg4_height
        if self.title is not None:
           obj_dict['title'] = self.title
        if self.caption is not None:
           obj_dict['caption'] = self.caption
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultMpeg4Gif object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultVideo(object):
    """
    An inline query result containing a link to a page containing an embedded video player or a video file.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultvideo>`_.
    """

    def __init__(self,
            id,
            video_url,
            mime_type,
            thumb_url,
            title,
            caption=None,
            video_width=None,
            video_height=None,
            video_duration=None,
            description=None,
            reply_markup=None,
            input_message_content=None):
        self.type = 'video'
        self.id = id
        self.video_url = video_url
        self.mime_type = mime_type
        self.thumb_url = thumb_url
        self.title = title
        self.caption = caption
        self.video_width = video_width
        self.video_height = video_height
        self.video_duration = video_duration
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def from_dict(obj_dict):
        """Builds InlineQueryResultVideo object from Python dict."""
        return InlineQueryResultVideo(
                id=req_plain_param('id', obj_dict),
                video_url=req_plain_param('video_url', obj_dict),
                mime_type=req_plain_param('mime_type', obj_dict),
                thumb_url=req_plain_param('thumb_url', obj_dict),
                title=req_plain_param('title', obj_dict),
                caption=opt_plain_param('caption', obj_dict),
                video_width=opt_plain_param('video_width', obj_dict),
                video_height=opt_plain_param('video_height', obj_dict),
                video_duration=opt_plain_param('video_duration', obj_dict),
                description=opt_plain_param('description', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent)
            )

    def from_json(json_str):
        """Builds InlineQueryResultVideo object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultVideo.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultVideo object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'video_url': self.video_url,
            'mime_type': self.mime_type,
            'thumb_url': self.thumb_url,
            'title': self.title
        }
        if self.caption is not None:
           obj_dict['caption'] = self.caption
        if self.video_width is not None:
           obj_dict['video_width'] = self.video_width
        if self.video_height is not None:
           obj_dict['video_height'] = self.video_height
        if self.video_duration is not None:
           obj_dict['video_duration'] = self.video_duration
        if self.description is not None:
           obj_dict['description'] = self.description
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultVideo object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultAudio(object):
    """
    An inline query result containing a link to an mp3 audio file. By default, this audio file will be sent by the user.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultaudio>`_.
    """

    def __init__(self,
            id,
            audio_url,
            title,
            performer=None,
            audio_duration=None,
            reply_markup=None,
            input_message_content=None):
        self.type = 'audio'
        self.id = id
        self.audio_url = audio_url
        self.title = title
        self.performer = performer
        self.audio_duration = audio_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def from_dict(obj_dict):
        """Builds InlineQueryResultAudio object from Python dict."""
        return InlineQueryResultAudio(
                id=req_plain_param('id', obj_dict),
                audio_url=req_plain_param('audio_url', obj_dict),
                title=req_plain_param('title', obj_dict),
                performer=opt_plain_param('performer', obj_dict),
                audio_duration=opt_plain_param('audio_duration', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent)
            )

    def from_json(json_str):
        """Builds InlineQueryResultAudio object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultAudio.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultAudio object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'audio_url': self.audio_url,
            'title': self.title
        }
        if self.performer is not None:
           obj_dict['performer'] = self.performer
        if self.audio_duration is not None:
           obj_dict['audio_duration'] = self.audio_duration
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultAudio object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultVoice(object):
    """
    An inline query result containing a link to a voice recording in an .ogg container encoded with OPUS.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultvoice>`_.
    """

    def __init__(self,
            id,
            voice_url,
            title,
            performer=None,
            voice_duration=None,
            reply_markup=None,
            input_message_content=None):
        self.type = 'voice'
        self.id = id
        self.voice_url = voice_url
        self.title = title
        self.performer = performer
        self.voice_duration = voice_duration
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def from_dict(obj_dict):
        """Builds InlineQueryResultVoice object from Python dict."""
        return InlineQueryResultVoice(
                id=req_plain_param('id', obj_dict),
                voice_url=req_plain_param('voice_url', obj_dict),
                title=req_plain_param('title', obj_dict),
                performer=opt_plain_param('performer', obj_dict),
                voice_duration=opt_plain_param('voice_duration', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent)
            )

    def from_json(json_str):
        """Builds InlineQueryResultVoice object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultVoice.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultVoice object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'voice_url': self.voice_url,
            'title': self.title
        }
        if self.performer is not None:
           obj_dict['performer'] = self.performer
        if self.voice_duration is not None:
           obj_dict['voice_duration'] = self.voice_duration
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultVoice object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultDocument(object):
    """
    An inline query result containing a link to a file.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultdocument>`_.
    """

    def __init__(self,
            id,
            title,
            document_url,
            mime_type,
            caption=None,
            description=None,
            reply_markup=None,
            input_message_content=None,
            thumb_url=None,
            thumb_width=None,
            thumb_height=None):
        self.type = 'document'
        self.id = id
        self.title = title
        self.caption = caption
        self.document_url = document_url
        self.mime_type = mime_type
        self.description = description
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height

    def from_dict(obj_dict):
        """Builds InlineQueryResultDocument object from Python dict."""
        return InlineQueryResultDocument(
                id=req_plain_param('id', obj_dict),
                title=req_plain_param('title', obj_dict),
                document_url=req_plain_param('document_url', obj_dict),
                mime_type=req_plain_param('mime_type', obj_dict),
                caption=opt_plain_param('caption', obj_dict),
                description=opt_plain_param('description', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent),
                thumb_url=opt_plain_param('thumb_url', obj_dict),
                thumb_width=opt_plain_param('thumb_width', obj_dict),
                thumb_height=opt_plain_param('thumb_height', obj_dict)
            )

    def from_json(json_str):
        """Builds InlineQueryResultDocument object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultDocument.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultDocument object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'title': self.title,
            'document_url': self.document_url,
            'mime_type': self.mime_type
        }
        if self.caption is not None:
           obj_dict['caption'] = self.caption
        if self.description is not None:
           obj_dict['description'] = self.description
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        if self.thumb_url is not None:
           obj_dict['thumb_url'] = self.thumb_url
        if self.thumb_width is not None:
           obj_dict['thumb_width'] = self.thumb_width
        if self.thumb_height is not None:
           obj_dict['thumb_height'] = self.thumb_height
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultDocument object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultLocation(object):
    """
    An inline query result containing a location on a map.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultlocation>`_.
    """

    def __init__(self,
            id,
            latitude,
            longitude,
            title,
            reply_markup=None,
            input_message_content=None,
            thumb_url=None,
            thumb_width=None,
            thumb_height=None):
        self.type = 'location'
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height

    def from_dict(obj_dict):
        """Builds InlineQueryResultLocation object from Python dict."""
        return InlineQueryResultLocation(
                id=req_plain_param('id', obj_dict),
                latitude=req_plain_param('latitude', obj_dict),
                longitude=req_plain_param('longitude', obj_dict),
                title=req_plain_param('title', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent),
                thumb_url=opt_plain_param('thumb_url', obj_dict),
                thumb_width=opt_plain_param('thumb_width', obj_dict),
                thumb_height=opt_plain_param('thumb_height', obj_dict)
            )

    def from_json(json_str):
        """Builds InlineQueryResultLocation object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultLocation.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultLocation object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'title': self.title
        }
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        if self.thumb_url is not None:
           obj_dict['thumb_url'] = self.thumb_url
        if self.thumb_width is not None:
           obj_dict['thumb_width'] = self.thumb_width
        if self.thumb_height is not None:
           obj_dict['thumb_height'] = self.thumb_height
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultLocation object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultVenue(object):
    """
    An inline query result containing a venue.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultvenue>`_.
    """

    def __init__(self,
            id,
            latitude,
            longitude,
            title,
            address,
            foursquare_id=None,
            reply_markup=None,
            input_message_content=None,
            thumb_url=None,
            thumb_width=None,
            thumb_height=None):
        self.type = 'venue'
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height

    def from_dict(obj_dict):
        """Builds InlineQueryResultVenue object from Python dict."""
        return InlineQueryResultVenue(
                id=req_plain_param('id', obj_dict),
                latitude=req_plain_param('latitude', obj_dict),
                longitude=req_plain_param('longitude', obj_dict),
                title=req_plain_param('title', obj_dict),
                address=req_plain_param('address', obj_dict),
                foursquare_id=opt_plain_param('foursquare_id', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent),
                thumb_url=opt_plain_param('thumb_url', obj_dict),
                thumb_width=opt_plain_param('thumb_width', obj_dict),
                thumb_height=opt_plain_param('thumb_height', obj_dict)
            )

    def from_json(json_str):
        """Builds InlineQueryResultVenue object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultVenue.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultVenue object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'title': self.title,
            'address': self.address
        }
        if self.foursquare_id is not None:
           obj_dict['foursquare_id'] = self.foursquare_id
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        if self.thumb_url is not None:
           obj_dict['thumb_url'] = self.thumb_url
        if self.thumb_width is not None:
           obj_dict['thumb_width'] = self.thumb_width
        if self.thumb_height is not None:
           obj_dict['thumb_height'] = self.thumb_height
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultVenue object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultContact(object):
    """
    An inline query result containing a contact with a phone number.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultcontact>`_.
    """

    def __init__(self,
            id,
            phone_number,
            first_name,
            last_name=None,
            reply_markup=None,
            input_message_content=None,
            thumb_url=None,
            thumb_width=None,
            thumb_height=None):
        self.type = 'contact'
        self.id = id
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content
        self.thumb_url = thumb_url
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height

    def from_dict(obj_dict):
        """Builds InlineQueryResultContact object from Python dict."""
        return InlineQueryResultContact(
                id=req_plain_param('id', obj_dict),
                phone_number=req_plain_param('phone_number', obj_dict),
                first_name=req_plain_param('first_name', obj_dict),
                last_name=opt_plain_param('last_name', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent),
                thumb_url=opt_plain_param('thumb_url', obj_dict),
                thumb_width=opt_plain_param('thumb_width', obj_dict),
                thumb_height=opt_plain_param('thumb_height', obj_dict)
            )

    def from_json(json_str):
        """Builds InlineQueryResultContact object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultContact.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultContact object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'phone_number': self.phone_number,
            'first_name': self.first_name
        }
        if self.last_name is not None:
           obj_dict['last_name'] = self.last_name
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        if self.thumb_url is not None:
           obj_dict['thumb_url'] = self.thumb_url
        if self.thumb_width is not None:
           obj_dict['thumb_width'] = self.thumb_width
        if self.thumb_height is not None:
           obj_dict['thumb_height'] = self.thumb_height
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultContact object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultCachedPhoto(object):
    """
    An inline query result containing a link to a photo stored on the Telegram servers.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultcachedphoto>`_.
    """

    def __init__(self,
            id,
            photo_file_id,
            title=None,
            description=None,
            caption=None,
            reply_markup=None,
            input_message_content=None):
        self.type = 'photo'
        self.id = id
        self.photo_file_id = photo_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def from_dict(obj_dict):
        """Builds InlineQueryResultCachedPhoto object from Python dict."""
        return InlineQueryResultCachedPhoto(
                id=req_plain_param('id', obj_dict),
                photo_file_id=req_plain_param('photo_file_id', obj_dict),
                title=opt_plain_param('title', obj_dict),
                description=opt_plain_param('description', obj_dict),
                caption=opt_plain_param('caption', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent)
            )

    def from_json(json_str):
        """Builds InlineQueryResultCachedPhoto object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultCachedPhoto.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultCachedPhoto object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'photo_file_id': self.photo_file_id
        }
        if self.title is not None:
           obj_dict['title'] = self.title
        if self.description is not None:
           obj_dict['description'] = self.description
        if self.caption is not None:
           obj_dict['caption'] = self.caption
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultCachedPhoto object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultCachedGif(object):
    """
    An inline query result containing a link to an animated GIF file stored on the Telegram servers.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultcachedgif>`_.
    """

    def __init__(self,
            id,
            gif_file_id,
            title=None,
            caption=None,
            reply_markup=None,
            input_message_content=None):
        self.type = 'gif'
        self.id = id
        self.gif_file_id = gif_file_id
        self.title = title
        self.caption = caption
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def from_dict(obj_dict):
        """Builds InlineQueryResultCachedGif object from Python dict."""
        return InlineQueryResultCachedGif(
                id=req_plain_param('id', obj_dict),
                gif_file_id=req_plain_param('gif_file_id', obj_dict),
                title=opt_plain_param('title', obj_dict),
                caption=opt_plain_param('caption', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent)
            )

    def from_json(json_str):
        """Builds InlineQueryResultCachedGif object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultCachedGif.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultCachedGif object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'gif_file_id': self.gif_file_id
        }
        if self.title is not None:
           obj_dict['title'] = self.title
        if self.caption is not None:
           obj_dict['caption'] = self.caption
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultCachedGif object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultCachedMpeg4Gif(object):
    """
    An inline query result containing a link to a video animation (H.264/MPEG-4 AVC video without sound) stored on the Telegram servers.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultcachedmpeg4gif>`_.
    """

    def __init__(self,
            id,
            mpeg4_file_id,
            title=None,
            caption=None,
            reply_markup=None,
            input_message_content=None):
        self.type = 'mpeg4_gif'
        self.id = id
        self.mpeg4_file_id = mpeg4_file_id
        self.title = title
        self.caption = caption
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def from_dict(obj_dict):
        """Builds InlineQueryResultCachedMpeg4Gif object from Python dict."""
        return InlineQueryResultCachedMpeg4Gif(
                id=req_plain_param('id', obj_dict),
                mpeg4_file_id=req_plain_param('mpeg4_file_id', obj_dict),
                title=opt_plain_param('title', obj_dict),
                caption=opt_plain_param('caption', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent)
            )

    def from_json(json_str):
        """Builds InlineQueryResultCachedMpeg4Gif object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultCachedMpeg4Gif.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultCachedMpeg4Gif object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'mpeg4_file_id': self.mpeg4_file_id
        }
        if self.title is not None:
           obj_dict['title'] = self.title
        if self.caption is not None:
           obj_dict['caption'] = self.caption
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultCachedMpeg4Gif object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultCachedSticker(object):
    """
    An inline query result containing a link to a sticker stored on the Telegram servers.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultcachedsticker>`_.
    """

    def __init__(self,
            id,
            sticker_file_id,
            reply_markup=None,
            input_message_content=None):
        self.type = 'sticker'
        self.id = id
        self.sticker_file_id = sticker_file_id
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def from_dict(obj_dict):
        """Builds InlineQueryResultCachedSticker object from Python dict."""
        return InlineQueryResultCachedSticker(
                id=req_plain_param('id', obj_dict),
                sticker_file_id=req_plain_param('sticker_file_id', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent)
            )

    def from_json(json_str):
        """Builds InlineQueryResultCachedSticker object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultCachedSticker.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultCachedSticker object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'sticker_file_id': self.sticker_file_id
        }
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultCachedSticker object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultCachedDocument(object):
    """
    An inline query result containing a link to a file stored on the Telegram servers.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultcacheddocument>`_.
    """

    def __init__(self,
            id,
            title,
            document_file_id,
            description=None,
            caption=None,
            reply_markup=None,
            input_message_content=None):
        self.type = 'document'
        self.id = id
        self.title = title
        self.document_file_id = document_file_id
        self.description = description
        self.caption = caption
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def from_dict(obj_dict):
        """Builds InlineQueryResultCachedDocument object from Python dict."""
        return InlineQueryResultCachedDocument(
                id=req_plain_param('id', obj_dict),
                title=req_plain_param('title', obj_dict),
                document_file_id=req_plain_param('document_file_id', obj_dict),
                description=opt_plain_param('description', obj_dict),
                caption=opt_plain_param('caption', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent)
            )

    def from_json(json_str):
        """Builds InlineQueryResultCachedDocument object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultCachedDocument.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultCachedDocument object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'title': self.title,
            'document_file_id': self.document_file_id
        }
        if self.description is not None:
           obj_dict['description'] = self.description
        if self.caption is not None:
           obj_dict['caption'] = self.caption
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultCachedDocument object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultCachedVideo(object):
    """
    An inline query result containing a link to a video file stored on the Telegram servers.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultcachedvideo>`_.
    """

    def __init__(self,
            id,
            video_file_id,
            title,
            description=None,
            caption=None,
            reply_markup=None,
            input_message_content=None):
        self.type = 'video'
        self.id = id
        self.video_file_id = video_file_id
        self.title = title
        self.description = description
        self.caption = caption
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def from_dict(obj_dict):
        """Builds InlineQueryResultCachedVideo object from Python dict."""
        return InlineQueryResultCachedVideo(
                id=req_plain_param('id', obj_dict),
                video_file_id=req_plain_param('video_file_id', obj_dict),
                title=req_plain_param('title', obj_dict),
                description=opt_plain_param('description', obj_dict),
                caption=opt_plain_param('caption', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent)
            )

    def from_json(json_str):
        """Builds InlineQueryResultCachedVideo object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultCachedVideo.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultCachedVideo object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'video_file_id': self.video_file_id,
            'title': self.title
        }
        if self.description is not None:
           obj_dict['description'] = self.description
        if self.caption is not None:
           obj_dict['caption'] = self.caption
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultCachedVideo object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultCachedVoice(object):
    """
    An inline query result containing a link to a voice message stored on the Telegram servers.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultcachedvoice>`_.
    """

    def __init__(self,
            id,
            voice_file_id,
            title,
            reply_markup=None,
            input_message_content=None):
        self.type = 'voice'
        self.id = id
        self.voice_file_id = voice_file_id
        self.title = title
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def from_dict(obj_dict):
        """Builds InlineQueryResultCachedVoice object from Python dict."""
        return InlineQueryResultCachedVoice(
                id=req_plain_param('id', obj_dict),
                voice_file_id=req_plain_param('voice_file_id', obj_dict),
                title=req_plain_param('title', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent)
            )

    def from_json(json_str):
        """Builds InlineQueryResultCachedVoice object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultCachedVoice.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultCachedVoice object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'voice_file_id': self.voice_file_id,
            'title': self.title
        }
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultCachedVoice object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InlineQueryResultCachedAudio(object):
    """
    An inline query result containing a link to an mp3 audio file stored on the Telegram servers.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inlinequeryresultcachedaudio>`_.
    """

    def __init__(self,
            id,
            audio_file_id,
            reply_markup=None,
            input_message_content=None):
        self.type = 'audio'
        self.id = id
        self.audio_file_id = audio_file_id
        self.reply_markup = reply_markup
        self.input_message_content = input_message_content

    def from_dict(obj_dict):
        """Builds InlineQueryResultCachedAudio object from Python dict."""
        return InlineQueryResultCachedAudio(
                id=req_plain_param('id', obj_dict),
                audio_file_id=req_plain_param('audio_file_id', obj_dict),
                reply_markup=opt_plain_param('reply_markup', obj_dict, InlineKeyboardMarkup),
                input_message_content=opt_plain_param('input_message_content', obj_dict, InputMessageContent)
            )

    def from_json(json_str):
        """Builds InlineQueryResultCachedAudio object from JSON string."""
        jdata = json.loads(json_str)
        return InlineQueryResultCachedAudio.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InlineQueryResultCachedAudio object."""
        obj_dict = {
            'type': self.type,
            'id': self.id,
            'audio_file_id': self.audio_file_id
        }
        if self.reply_markup is not None:
           obj_dict['reply_markup'] = self.reply_markup.to_dict()
        if self.input_message_content is not None:
           obj_dict['input_message_content'] = self.input_message_content.to_dict()
        return obj_dict

    def to_json(self):
        """Returns JSON string from InlineQueryResultCachedAudio object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InputTextMessageContent(object):
    """
    The content of a text message to be sent as the result of an inline query.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inputtextmessagecontent>`_.
    """

    def __init__(self,
            message_text,
            parse_mode=None,
            disable_web_page_preview=None):
        self.message_text = message_text
        self.parse_mode = parse_mode
        self.disable_web_page_preview = disable_web_page_preview

    def from_dict(obj_dict):
        """Builds InputTextMessageContent object from Python dict."""
        return InputTextMessageContent(
                message_text=req_plain_param('message_text', obj_dict),
                parse_mode=opt_plain_param('parse_mode', obj_dict),
                disable_web_page_preview=opt_plain_param('disable_web_page_preview', obj_dict)
            )

    def from_json(json_str):
        """Builds InputTextMessageContent object from JSON string."""
        jdata = json.loads(json_str)
        return InputTextMessageContent.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InputTextMessageContent object."""
        obj_dict = {
            'message_text': self.message_text
        }
        if self.parse_mode is not None:
           obj_dict['parse_mode'] = self.parse_mode
        if self.disable_web_page_preview is not None:
           obj_dict['disable_web_page_preview'] = self.disable_web_page_preview
        return obj_dict

    def to_json(self):
        """Returns JSON string from InputTextMessageContent object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InputLocationMessageContent(object):
    """
    The content of a location message to be sent as the result of an inline query.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inputlocationmessagecontent>`_.
    """

    def __init__(self,
            latitude,
            longitude):
        self.latitude = latitude
        self.longitude = longitude

    def from_dict(obj_dict):
        """Builds InputLocationMessageContent object from Python dict."""
        return InputLocationMessageContent(
                latitude=req_plain_param('latitude', obj_dict),
                longitude=req_plain_param('longitude', obj_dict)
            )

    def from_json(json_str):
        """Builds InputLocationMessageContent object from JSON string."""
        jdata = json.loads(json_str)
        return InputLocationMessageContent.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InputLocationMessageContent object."""
        obj_dict = {
            'latitude': self.latitude,
            'longitude': self.longitude
        }
        return obj_dict

    def to_json(self):
        """Returns JSON string from InputLocationMessageContent object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InputVenueMessageContent(object):
    """
    The che content of a venue message to be sent as the result of an inline query.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inputvenuemessagecontent>`_.
    """

    def __init__(self,
            latitude,
            longitude,
            title,
            address,
            foursquare_id=None):
        self.latitude = latitude
        self.longitude = longitude
        self.title = title
        self.address = address
        self.foursquare_id = foursquare_id

    def from_dict(obj_dict):
        """Builds InputVenueMessageContent object from Python dict."""
        return InputVenueMessageContent(
                latitude=req_plain_param('latitude', obj_dict),
                longitude=req_plain_param('longitude', obj_dict),
                title=req_plain_param('title', obj_dict),
                address=req_plain_param('address', obj_dict),
                foursquare_id=opt_plain_param('foursquare_id', obj_dict)
            )

    def from_json(json_str):
        """Builds InputVenueMessageContent object from JSON string."""
        jdata = json.loads(json_str)
        return InputVenueMessageContent.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InputVenueMessageContent object."""
        obj_dict = {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'title': self.title,
            'address': self.address
        }
        if self.foursquare_id is not None:
           obj_dict['foursquare_id'] = self.foursquare_id
        return obj_dict

    def to_json(self):
        """Returns JSON string from InputVenueMessageContent object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class InputContactMessageContent(object):
    """
    The content of a contact message to be sent as the result of an inline query.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#inputcontactmessagecontent>`_.
    """

    def __init__(self,
            phone_number,
            first_name,
            last_name=None):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name

    def from_dict(obj_dict):
        """Builds InputContactMessageContent object from Python dict."""
        return InputContactMessageContent(
                phone_number=req_plain_param('phone_number', obj_dict),
                first_name=req_plain_param('first_name', obj_dict),
                last_name=opt_plain_param('last_name', obj_dict)
            )

    def from_json(json_str):
        """Builds InputContactMessageContent object from JSON string."""
        jdata = json.loads(json_str)
        return InputContactMessageContent.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from InputContactMessageContent object."""
        obj_dict = {
            'phone_number': self.phone_number,
            'first_name': self.first_name
        }
        if self.last_name is not None:
           obj_dict['last_name'] = self.last_name
        return obj_dict

    def to_json(self):
        """Returns JSON string from InputContactMessageContent object."""
        return json.dumps(self.to_dict(), separators=(',',':'))

class ChosenInlineResult(object):
    """
    The result of an inline query that was chosen by the user and sent to their chat partner.

    For more details read the `Telegram docs <https://core.telegram.org/bots/api#choseninlineresult>`_.
    """

    def __init__(self,
            result_id,
            sender,
            query,
            location=None,
            inline_message_id=None):
        self.result_id = result_id
        self.sender = sender
        self.location = location
        self.inline_message_id = inline_message_id
        self.query = query

    def from_dict(obj_dict):
        """Builds ChosenInlineResult object from Python dict."""
        return ChosenInlineResult(
                result_id=req_plain_param('result_id', obj_dict),
                sender=req_plain_param('from', obj_dict, User),
                query=req_plain_param('query', obj_dict),
                location=opt_plain_param('location', obj_dict, Location),
                inline_message_id=opt_plain_param('inline_message_id', obj_dict)
            )

    def from_json(json_str):
        """Builds ChosenInlineResult object from JSON string."""
        jdata = json.loads(json_str)
        return ChosenInlineResult.from_dict(jdata)

    def to_dict(self):
        """Returns Python dict from ChosenInlineResult object."""
        obj_dict = {
            'result_id': self.result_id,
            'from': self.sender.to_dict(),
            'query': self.query
        }
        if self.location is not None:
           obj_dict['location'] = self.location.to_dict()
        if self.inline_message_id is not None:
           obj_dict['inline_message_id'] = self.inline_message_id
        return obj_dict

    def to_json(self):
        """Returns JSON string from ChosenInlineResult object."""
        return json.dumps(self.to_dict(), separators=(',',':'))
