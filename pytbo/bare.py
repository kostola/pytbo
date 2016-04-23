# -*- coding: utf-8 -*-

"""
pytbo.bare
~~~~~~~~~~

This module implements a bare Telegram Bot, which is just a wrapper to the Telegram Bots API.

:copyright: (c) 2016 by Alessandro Costa.
:license: Apache2, see LICENSE for more details.

"""

import json
import mimetypes
import os
import requests
from requests_toolbelt import MultipartEncoder

from .errors import BotNotFoundError, ApiResponseError, MalformedResponseError
from .types import ( Audio, CallbackQuery, Chat, ChosenInlineResult, Contact, Document, File, ForceReply,
                     InlineKeyboardButton, InlineKeyboardMarkup, InlineQuery, InlineQueryResultArticle,
                     InlineQueryResultAudio, InlineQueryResultCachedAudio, InlineQueryResultCachedDocument,
                     InlineQueryResultCachedGif, InlineQueryResultCachedMpeg4Gif, InlineQueryResultCachedPhoto,
                     InlineQueryResultCachedVideo, InlineQueryResultCachedVoice, InlineQueryResultContact,
                     InlineQueryResultDocument, InlineQueryResultGif, InlineQueryResultLocation,
                     InlineQueryResultMpeg4Gif, InlineQueryResultPhoto, InlineQueryResultVenue,
                     InlineQueryResultVideo, InlineQueryResultVoice, InputContactMessageContent,
                     InputLocationMessageContent, InputTextMessageContent, InputVenueMessageContent,
                     KeyboardButton, Location, Message, MessageEntity, PhotoSize, ReplyKeyboardHide,
                     ReplyKeyboardMarkup, Sticker, Update, User, UserProfilePhotos, Venue, Video, Voice )

class BareBot(object):
    def __init__(self, token):
        self.token = token
        bot_user = self.getMe()
        self.id = bot_user.id
        self.username = bot_user.username

    def __base_url_for(self, method):
        return "https://api.telegram.org/bot%s/%s" % (self.token, method)

    def __handle_object_response(self, response, method, return_class):
        result = self.__handle_response(response, method)
        return return_class.from_dict(result)

    def __handle_array_response(self, response, method, return_class):
        result = self.__handle_response(response, method)
        return [ return_class.from_dict(obj) for obj in result ]

    def __handle_response(self, response, method):
        try:
            rdata = json.loads(response.text)
        except json.decoder.JSONDecodeError:
            raise MalformedResponseError("failed to parse '%s' response" % (method))
        if 'ok' not in rdata:
            raise MalformedResponseError("'%s' returned a malformed JSON" % (method))
        if not rdata['ok']:
            raise ApiResponseError(method, rdata['error_code'], rdata['description'])
        if 'result' not in rdata:
            raise MalformedResponseError("'%s' returned a malformed JSON" % (method))
        return rdata['result']

    def __input_file_tuple(self, filepath):
        guessed_mime_type = mimetypes.MimeTypes().guess_type(filepath)[0]
        filetype = 'application/octet-stream' if guessed_mime_type is None else guessed_mime_type
        return (os.path.basename(filepath), open(filepath, 'rb'), filetype)

    def getMe(self):
        """
        A simple method for testing your bot's auth token. Requires no parameters.
        Returns basic information about the bot in form of a User object.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#getme>`_.
        """

        r = requests.get(self.__base_url_for('getMe'))
        try:
            return self.__handle_object_response(r, 'getMe', User)
        except MalformedResponseError:
            raise BotNotFoundError()

    def getUpdates(self,
            offset=None,
            limit=None,
            timeout=None):
        """
        Use this method to receive incoming updates using long polling (wiki).
        An Array of Update objects is returned.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#getupdates>`_.
        """

        p = {}
        if offset is not None:
            p['offset'] = offset
        if limit is not None:
            p['limit'] = limit
        if timeout is not None:
            p['timeout'] = timeout
        r = requests.get(self.__base_url_for('getUpdates'), params=p)
        return self.__handle_array_response(r, 'getUpdates', Update)

    def setWebhook(self,
            url,
            certificate=None):
        """
        Use this method to specify a url and receive incoming updates via an outgoing webhook.
        Whenever there is an update for the bot, we will send an HTTPS POST request to the specified url, containing a JSON-serialized Update.
        In case of an unsuccessful request, we will give up after a reasonable amount of attempts.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#setwebhook>`_.
        """

        p = {
            'url': url
        }
        if certificate is not None:
            p['certificate'] = self.__input_file_tuple(certificate)
        r = None
        if certificate is not None:
            m = MultipartEncoder(p)
            r = requests.post(self.__base_url_for('setWebhook'), data=m, headers={'Content-Type': m.content_type})
        else:
            r = requests.get(self.__base_url_for('setWebhook'), params=p)
        return self.__handle_response(r, 'setWebhook')

    def unsetWebhook(self):
        """
        Use this method to unset the webhook.
        This is required to be able to receive updates again with the getUpdates method.
        """

        r = requests.get(self.__base_url_for('setWebhook'))
        return self.__handle_response(r, 'unsetWebhook')

    def sendMessage(self,
            chat_id,
            text,
            parse_mode=None,
            disable_web_page_preview=None,
            disable_notification=None,
            reply_to_message_id=None,
            reply_markup=None):
        """
        Use this method to send text messages.
        On success, the sent Message is returned.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#sendmessage>`_.
        """

        p = {
            'chat_id': chat_id,
            'text': text
        }
        if parse_mode is not None:
            p['parse_mode'] = parse_mode
        if disable_web_page_preview is not None:
            p['disable_web_page_preview'] = disable_web_page_preview
        if disable_notification is not None:
            p['disable_notification'] = disable_notification
        if reply_to_message_id is not None:
            p['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            p['reply_markup'] = reply_markup.to_json()
        r = requests.get(self.__base_url_for('sendMessage'), params=p)
        return self.__handle_object_response(r, 'sendMessage', Message)

    def forwardMessage(self,
            chat_id,
            from_chat_id,
            message_id,
            disable_notification=None):
        """
        Use this method to forward messages of any kind.
        On success, the sent Message is returned.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#forwardmessage>`_.
        """

        p = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id
        }
        if disable_notification is not None:
            p['disable_notification'] = disable_notification
        r = requests.get(self.__base_url_for('forwardMessage'), params=p)
        return self.__handle_object_response(r, 'forwardMessage', Message)

    def sendPhoto(self,
            chat_id,
            photo_id=None,
            photo_file=None,
            caption=None,
            disable_notification=None,
            reply_to_message_id=None,
            reply_markup=None):
        """
        Use this method to send photos.
        On success, the sent Message is returned.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#sendphoto>`_.
        """

        p = {
            'chat_id': chat_id
        }
        if photo_file is not None:
            p['photo'] = self.__input_file_tuple(photo_file)
        elif photo_id is not None:
            p['photo'] = photo_id
        else:
            raise ApiRequestError('photo_id and photo_file cannot be both None')
        if caption is not None:
            p['caption'] = caption
        if disable_notification is not None:
            p['disable_notification'] = disable_notification
        if reply_to_message_id is not None:
            p['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            p['reply_markup'] = reply_markup.to_json()
        r = None
        if photo_file is not None:
            m = MultipartEncoder(p)
            r = requests.post(self.__base_url_for('sendPhoto'), data=m, headers={'Content-Type': m.content_type})
        else:
            r = requests.get(self.__base_url_for('sendPhoto'), params=p)
        return self.__handle_object_response(r, 'sendPhoto', Message)

    def sendAudio(self,
            chat_id,
            audio_id=None,
            audio_file=None,
            duration=None,
            performer=None,
            title=None,
            disable_notification=None,
            reply_to_message_id=None,
            reply_markup=None):
        """
        Use this method to send audio files, if you want Telegram clients to display them in the music player.
        Your audio must be in the .mp3 format. On success, the sent Message is returned.
        Bots can currently send audio files of up to 50 MB in size, this limit may be changed in the future.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#sendaudio>`_.
        """

        p = {
            'chat_id': chat_id
        }
        if audio_file is not None:
            p['audio'] = self.__input_file_tuple(audio_file)
        elif audio_id is not None:
            p['audio'] = audio_id
        else:
            raise ApiRequestError('audio_id and audio_file cannot be both None')
        if duration is not None:
            p['duration'] = duration
        if performer is not None:
            p['performer'] = performer
        if title is not None:
            p['title'] = title
        if disable_notification is not None:
            p['disable_notification'] = disable_notification
        if reply_to_message_id is not None:
            p['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            p['reply_markup'] = reply_markup.to_json()
        r = None
        if audio_file is not None:
            m = MultipartEncoder(p)
            r = requests.post(self.__base_url_for('sendAudio'), data=m, headers={'Content-Type': m.content_type})
        else:
            r = requests.get(self.__base_url_for('sendAudio'), params=p)
        return self.__handle_object_response(r, 'sendAudio', Message)

    def sendDocument(self,
            chat_id,
            document_id=None,
            document_file=None,
            caption=None,
            disable_notification=None,
            reply_to_message_id=None,
            reply_markup=None):
        """
        Use this method to send general files. On success, the sent Message is returned.
        Bots can currently send files of any type of up to 50 MB in size, this limit may be changed in the future.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#senddocument>`_.
        """

        p = {
            'chat_id': chat_id
        }
        if document_file is not None:
            p['document'] = self.__input_file_tuple(document_file)
        elif document_id is not None:
            p['document'] = document_id
        else:
            raise ApiRequestError('document_id and document_file cannot be both None')
        if caption is not None:
            p['caption'] = caption
        if disable_notification is not None:
            p['disable_notification'] = disable_notification
        if reply_to_message_id is not None:
            p['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            p['reply_markup'] = reply_markup.to_json()
        r = None
        if document_file is not None:
            m = MultipartEncoder(p)
            r = requests.post(self.__base_url_for('sendDocument'), data=m, headers={'Content-Type': m.content_type})
        else:
            r = requests.get(self.__base_url_for('sendDocument'), params=p)
        return self.__handle_object_response(r, 'sendDocument', Message)

    def sendSticker(self,
            chat_id,
            sticker_id=None,
            sticker_file=None,
            disable_notification=None,
            reply_to_message_id=None,
            reply_markup=None):
        """
        Use this method to send .webp stickers. On success, the sent Message is returned.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#sendsticker>`_.
        """

        p = {
            'chat_id': chat_id
        }
        if sticker_file is not None:
            p['sticker'] = self.__input_file_tuple(sticker_file)
        elif sticker_id is not None:
            p['sticker'] = sticker_id
        else:
            raise ApiRequestError('sticker_id and sticker_file cannot be both None')
        if disable_notification is not None:
            p['disable_notification'] = disable_notification
        if reply_to_message_id is not None:
            p['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            p['reply_markup'] = reply_markup.to_json()
        r = None
        if sticker_file is not None:
            m = MultipartEncoder(p)
            r = requests.post(self.__base_url_for('sendSticker'), data=m, headers={'Content-Type': m.content_type})
        else:
            r = requests.get(self.__base_url_for('sendSticker'), params=p)
        return self.__handle_object_response(r, 'sendSticker', Message)

    def sendVideo(self,
            chat_id,
            video_id=None,
            video_file=None,
            duration=None,
            width=None,
            height=None,
            caption=None,
            disable_notification=None,
            reply_to_message_id=None,
            reply_markup=None):
        """
        Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document).
        On success, the sent Message is returned.
        Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#sendvideo>`_.
        """

        p = {
            'chat_id': chat_id
        }
        if video_file is not None:
            p['video'] = self.__input_file_tuple(video_file)
        elif video_id is not None:
            p['video'] = video_id
        else:
            raise ApiRequestError('video_id and video_file cannot be both None')
        if duration is not None:
            p['duration'] = duration
        if width is not None:
            p['width'] = width
        if height is not None:
            p['height'] = height
        if caption is not None:
            p['caption'] = caption
        if disable_notification is not None:
            p['disable_notification'] = disable_notification
        if reply_to_message_id is not None:
            p['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            p['reply_markup'] = reply_markup.to_json()
        r = None
        if video_file is not None:
            m = MultipartEncoder(p)
            r = requests.post(self.__base_url_for('sendVideo'), data=m, headers={'Content-Type': m.content_type})
        else:
            r = requests.get(self.__base_url_for('sendVideo'), params=p)
        return self.__handle_object_response(r, 'sendVideo', Message)

    def sendVoice(self,
            chat_id,
            voice_id=None,
            voice_file=None,
            duration=None,
            disable_notification=None,
            reply_to_message_id=None,
            reply_markup=None):
        """
        Use this method to send audio files, if you want Telegram clients to display the file as a playable voice message.
        For this to work, your audio must be in an .ogg file encoded with OPUS (other formats may be sent as Audio or Document).
        On success, the sent Message is returned. Bots can currently send voice messages of up to 50 MB in size, this limit may be changed in the future.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#sendvoice>`_.
        """

        p = {
            'chat_id': chat_id
        }
        if voice_file is not None:
            p['voice'] = self.__input_file_tuple(voice_file)
        elif voice_id is not None:
            p['voice'] = voice_id
        else:
            raise ApiRequestError('voice_id and voice_file cannot be both None')
        if duration is not None:
            p['duration'] = duration
        if disable_notification is not None:
            p['disable_notification'] = disable_notification
        if reply_to_message_id is not None:
            p['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            p['reply_markup'] = reply_markup.to_json()
        r = None
        if voice_file is not None:
            m = MultipartEncoder(p)
            r = requests.post(self.__base_url_for('sendVoice'), data=m, headers={'Content-Type': m.content_type})
        else:
            r = requests.get(self.__base_url_for('sendVoice'), params=p)
        return self.__handle_object_response(r, 'sendVoice', Message)

    def sendLocation(self,
            chat_id,
            latitude,
            longitude,
            disable_notification=None,
            reply_to_message_id=None,
            reply_markup=None):
        """
        Use this method to send point on the map. On success, the sent Message is returned.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#sendlocation>`_.
        """

        p = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude
        }
        if disable_notification is not None:
            p['disable_notification'] = disable_notification
        if reply_to_message_id is not None:
            p['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            p['reply_markup'] = reply_markup.to_json()
        r = requests.get(self.__base_url_for('sendLocation'), params=p)
        return self.__handle_object_response(r, 'sendLocation', Message)

    def sendVenue(self,
            chat_id,
            latitude,
            longitude,
            title,
            address,
            foursquare_id=None,
            disable_notification=None,
            reply_to_message_id=None,
            reply_markup=None):
        """
        Use this method to send information about a venue. On success, the sent Message is returned.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#sendvenue>`_.
        """

        p = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude,
            'title': title,
            'address': address
        }
        if foursquare_id is not None:
            p['foursquare_id'] = foursquare_id
        if disable_notification is not None:
            p['disable_notification'] = disable_notification
        if reply_to_message_id is not None:
            p['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            p['reply_markup'] = reply_markup.to_json()
        r = requests.get(self.__base_url_for('sendVenue'), params=p)
        return self.__handle_object_response(r, 'sendVenue', Message)

    def sendContact(self,
            chat_id,
            phone_number,
            first_name,
            last_name=None,
            disable_notification=None,
            reply_to_message_id=None,
            reply_markup=None):
        """
        Use this method to send phone contacts. On success, the sent Message is returned.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#sendcontact>`_.
        """

        p = {
            'chat_id': chat_id,
            'phone_number': phone_number,
            'first_name': first_name
        }
        if last_name is not None:
            p['last_name'] = last_name
        if disable_notification is not None:
            p['disable_notification'] = disable_notification
        if reply_to_message_id is not None:
            p['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            p['reply_markup'] = reply_markup.to_json()
        r = requests.get(self.__base_url_for('sendContact'), params=p)
        return self.__handle_object_response(r, 'sendContact', Message)

    def sendChatAction(self,
            chat_id,
            action):
        """
        Use this method when you need to tell the user that something is happening on the bot's side.
        The status is set for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status).

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#sendchataction>`_.
        """

        p = {
            'chat_id': chat_id,
            'action': action
        }
        r = requests.get(self.__base_url_for('sendChatAction'), params=p)
        return self.__handle_response(r, 'sendChatAction')

    def getUserProfilePhotos(self,
            user_id,
            offset=None,
            limit=None):
        """
        Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#getuserprofilephotos>`_.
        """

        p = {
            'user_id': user_id
        }
        if offset is not None:
            p['offset'] = offset
        if limit is not None:
            p['limit'] = limit
        r = requests.get(self.__base_url_for('getUserProfilePhotos'), params=p)
        return self.__handle_object_response(r, 'getUserProfilePhotos', UserProfilePhotos)

    def getFile(self,
            file_id):
        """
        Use this method to get basic info about a file and prepare it for downloading.
        For the moment, bots can download files of up to 20MB in size. On success, a File object is returned.
        The file can then be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>, where <file_path> is taken from the response.
        It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile again.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#getfile>`_.
        """

        p = {
            'file_id': file_id
        }
        r = requests.get(self.__base_url_for('getFile'), params=p)
        return self.__handle_object_response(r, 'getFile', File)

    def kickChatMember(self,
            chat_id,
            user_id):
        """
        Use this method to kick a user from a group or a supergroup.
        In the case of supergroups, the user will not be able to return to the group on their own using invite links, etc., unless unbanned first.
        The bot must be an administrator in the group for this to work. Returns True on success.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#kickchatmember>`_.
        """

        p = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        r = requests.get(self.__base_url_for('kickChatMember'), params=p)
        return self.__handle_response(r, 'kickChatMember')

    def unbanChatMember(self,
            chat_id,
            user_id):
        """
        Use this method to unban a previously kicked user in a supergroup.
        The user will not return to the group automatically, but will be able to join via link, etc.
        The bot must be an administrator in the group for this to work. Returns True on success.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#unbanchatmember>`_.
        """

        p = {
            'chat_id': chat_id,
            'user_id': user_id
        }
        r = requests.get(self.__base_url_for('unbanChatMember'), params=p)
        return self.__handle_response(r, 'unbanChatMember')

    def answerCallbackQuery(self,
            callback_query_id,
            text=None,
            show_alert=None):
        """
        Use this method to send answers to callback queries sent from inline keyboards.
        The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, True is returned.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#answercallbackquery>`_.
        """

        p = {
            'callback_query_id': callback_query_id
        }
        if text is not None:
            p['text'] = text
        if show_alert is not None:
            p['show_alert'] = show_alert
        r = requests.get(self.__base_url_for('answerCallbackQuery'), params=p)
        return self.__handle_response(r, 'answerCallbackQuery')

    def editMessageText(self,
            text,
            chat_id=None,
            message_id=None,
            inline_message_id=None,
            parse_mode=None,
            disable_web_page_preview=None,
            reply_markup=None):
        """
        Use this method to edit text messages sent by the bot or via the bot (for inline bots).
        On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#editmessagetext>`_.
        """

        p = {
            'text': text
        }
        if chat_id is not None:
            p['chat_id'] = chat_id
        if message_id is not None:
            p['message_id'] = json.dumps(message_id, separators=(',',':'))
        if inline_message_id is not None:
            p['inline_message_id'] = inline_message_id
        if parse_mode is not None:
            p['parse_mode'] = parse_mode
        if disable_web_page_preview is not None:
            p['disable_web_page_preview'] = disable_web_page_preview
        if reply_markup is not None:
            p['reply_markup'] = reply_markup.to_json()
        r = requests.get(self.__base_url_for('editMessageText'), params=p)
        return self.__handle_response(r, 'editMessageText')

    def editMessageCaption(self,
            chat_id=None,
            message_id=None,
            inline_message_id=None,
            caption=None,
            reply_markup=None):
        """
        Use this method to edit captions of messages sent by the bot or via the bot (for inline bots).
        On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#editmessagecaption>`_.
        """

        p = {}
        if chat_id is not None:
            p['chat_id'] = chat_id
        if message_id is not None:
            p['message_id'] = json.dumps(message_id, separators=(',',':'))
        if inline_message_id is not None:
            p['inline_message_id'] = inline_message_id
        if caption is not None:
            p['caption'] = caption
        if reply_markup is not None:
            p['reply_markup'] = reply_markup.to_json()
        r = requests.get(self.__base_url_for('editMessageCaption'), params=p)
        return self.__handle_response(r, 'editMessageCaption')

    def editMessageReplyMarkup(self,
            chat_id=None,
            message_id=None,
            inline_message_id=None,
            reply_markup=None):
        """
        Use this method to edit only the reply markup of messages sent by the bot or via the bot (for inline bots).
         On success, if edited message is sent by the bot, the edited Message is returned, otherwise True is returned.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#editmessagereplymarkup>`_.
        """

        p = {}
        if chat_id is not None:
            p['chat_id'] = chat_id
        if message_id is not None:
            p['message_id'] = json.dumps(message_id, separators=(',',':'))
        if inline_message_id is not None:
            p['inline_message_id'] = inline_message_id
        if reply_markup is not None:
            p['reply_markup'] = reply_markup.to_json()
        r = requests.get(self.__base_url_for('editMessageReplyMarkup'), params=p)
        return self.__handle_response(r, 'editMessageReplyMarkup')

    def answerInlineQuery(self,
            inline_query_id,
            results,
            cache_time=None,
            is_personal=None,
            next_offset=None,
            switch_pm_text=None,
            switch_pm_parameter=None):
        """
        Use this method to send answers to an inline query.
        On success, True is returned. No more than 50 results per query are allowed.

        For more details read the `Telegram docs <https://core.telegram.org/bots/api#answerinlinequery>`_.
        """

        p = {
            'inline_query_id': inline_query_id,
            'results': json.dumps([ e.to_dict() for e in results ], separators=(',',':'))
        }
        if cache_time is not None:
            p['cache_time'] = cache_time
        if is_personal is not None:
            p['is_personal'] = is_personal
        if next_offset is not None:
            p['next_offset'] = next_offset
        if switch_pm_text is not None:
            p['switch_pm_text'] = switch_pm_text
        if switch_pm_parameter is not None:
            p['switch_pm_parameter'] = switch_pm_parameter
        r = requests.get(self.__base_url_for('answerInlineQuery'), params=p)
        return self.__handle_response(r, 'answerInlineQuery')
