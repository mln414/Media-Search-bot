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
**Hello {mention}** 👋

**I'm RED X Bot 2.0** 🤖 **I Can Find You Any Movie, TV Series or Game Instantly** 🔍 **Follow the Steps**🔻

❐ First of All Join RED X News & Updates Channel.
❐ Click 'Tap to Search' to Use the Bot's Inline Method to Find a Movie.
❐ To Find TV Series & Games, Use the Main Menu.
❐ Ignore 'Want to create your own b...' Message. It's Irrelevant.


**මම තමයි RED X Bot 2.0**🤖 **ඔබට අවශ්‍ය ඕනෑම චිත්‍රපටයක්, කතාමාලාවක් හෝ වීඩියෝ ක්‍රීඩාවක් සොයා දෙන්න මට පුලුවන්** 🔍 **පහත පියවර අනුගමනය කරන්න**🔻

❐ ඉස්සෙල්ලම RED X News & Updates චැනල් එකට එකතු වෙන්න.
❐ 'Tap to Search' කියන එක ඔබල චිත්‍රපට ලබා ගත හැක.
❐ කතාමාලා සහ පරිගණක ක්‍රීඩා ලබා ගැනීමට ප්‍රධාන මෙනුව භාවිතා කරන්න.
❐ 'Want to create your own b...' කියන මැසේජ් එක ගනන් ගන්න එපා. ඒකෙන් වැඩක් නැහැ.
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = """
**🇱🇰 RED X Bot 2.0 🇱🇰**

**You Can Find Any Movie, TV Series or Game By Using Me ♥️**

**Bot:** **@redx414bot** 🤖
**Updates Channel:** **@redx_414_news** 🔰
**Admin:** **@RedX14** 👨‍💻
"""

INVITE_MSG = environ.get('INVITE_MSG', """
**You Haven't Join Our Channel**‼️ **Click On RED X News & Updates to Connect With Us** ♥️

**ඔයා අපේ චැනල් එකට එකතු වෙලා නෑ**‼️ **RED X News & Updates කියන එක ඔබල චැනල් එකට සෙට් වෙන්න** ♥️""")
