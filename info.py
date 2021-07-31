import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**✦You Must Join Our Channel to Search a Movie😇

✧(Movie Search කිරීමට නම් ඔයා අපේ Channel එකට Join වෙලා තිබීම අත්‍යවශ්‍ය වේ😇)

✦You Will Recieve a Message Saying '❌Unsupported Message type.'😒 Just Ignore It😌

✧(ඔයාලට '❌Unsupported Message type.' කියල Error එකක් පෙන්නයි😒 ඒක එච්චර ගනන් ගන්න එපා😌)

✦Click the Search Button Below to Find the Movie You Want😊

✧(ඔයාට අවශ්‍ය Movie එක ලබා ගැනීමට Search Button එක Click කරන්න😊)**
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = """
**🇱🇰 RED X Bot 🇱🇰** 

'You Can Get Movies, TV Series & Games By Using This Bot😊' 

Bot : {username}😍 
Update Channel : @redx414news 
Developer : @RedX14
"""

INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
