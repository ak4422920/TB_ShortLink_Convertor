import os
import re

id_pattern = re.compile(r'^(\d+)$')

API_ID = int(os.getenv("API_ID", 29171167))
API_HASH = os.getenv("API_HASH", "7ea2149629e445936619f06a3c0dc716")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
BASE_URL = os.getenv("BASE_URL", "tricky-dede-akad-e2b2d353.koyeb.app")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "Cineoriginals")
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "Cineoriginals")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://akre:akre@cluster0.gtpo3kw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
AUTH_CHANNELS = os.getenv("AUTH_CHANNEL", "-100****, -100****")
AUTH_CHANNELS = [int(channel_id) for channel_id in AUTH_CHANNELS.split(",")]
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-100****"))
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.getenv("ADMINS", "123456").split(",")]

START_TXT = '''<b>Hᴇʟʟᴏ {}, I Aᴍ Sʜᴏʀᴛɴᴇʀ Bᴏᴛ!.
๏ I ᴄᴀɴ Cᴏɴᴠᴇʀᴛ ʏᴏᴜʀ ʟɪɴᴋs ᴛᴏ Sʜᴏʀᴛ ʟɪɴᴋs ᴜsɪɴɢ ʏᴏᴜʀ ᴀᴩɪ.
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ Hᴇʟᴩ Mᴇɴᴜ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.
๏ Uᴘᴅᴀᴛᴇs - ⁂ @tamilan_botsz</b>'''
HELP_TXT = '''Sᴇɴᴅ ᴍᴇ ᴀɴʏ ʟɪɴᴋ ɪ ᴡɪʟʟ ᴄᴏɴᴠᴇʀᴛ ɪᴛ ᴛᴏ sʜᴏʀᴛ ʟɪɴᴋ ᴜsɪɴɢ ʏᴏᴜʀ ᴀᴘɪ
ʏᴏᴜ ᴄᴀɴ sʜᴀʀᴇ ᴛʜᴀᴛ ʟɪɴᴋ ᴀɴᴅ ᴇᴀʀɴ ᴍᴏɴᴇʏ.
sᴇɴᴅ /set_shortner ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ - Uᴘᴅᴀᴛᴇs - ⍟ @cineoriginals'''
ABOUT_TXT = '''<b>╔════❰ Tʙ Sʜᴏʀᴛɴᴇʀ Bᴏᴛ ❱═══❍
║ ┏━━━━━━━━━❥
║ ┣ Mʏ ɴᴀᴍᴇ -> {}
║ ┣ Mʏ Oᴡɴᴇʀ -> @Sharathitsisme & @iSmartBoii_Ujjwal
║ ┣ Uᴘᴅᴀᴛᴇꜱ -> <a href="tg://tamilan_botsz">••Bᴏᴛs••</a>
║ ┣ 𝖲ᴜᴘᴘᴏʀᴛ -> <a href="tg://tamilanbotsz_support"> Bᴏᴛs Sᴜᴩᴩᴏʀᴛ</a>
║ ┣ ๏ Cʜᴇᴄᴋ ʜᴇʟᴘ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ.
║ ┗━━━━━━━━━❥
╚═════❰ @ ❱═════❍</b>'''
