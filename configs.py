import os
import re

id_pattern = re.compile(r'^(\d+)$')

API_ID = int(os.getenv("API_ID", "29171167"))
API_HASH = os.getenv("API_HASH", "7ea2149629e445936619f06a3c0dc716")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
BASE_URL = os.getenv("BASE_URL", "tricky-dede-akad-e2b2d353.koyeb.app")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://akre:akre@cluster0.gtpo3kw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1002247400551"))
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.getenv("ADMINS", "7251898668 1255023013").split(",")]

START_TXT = '''<b>{},

๏ I ᴄᴀɴ Cᴏɴᴠᴇʀᴛ ʏᴏᴜʀ ʟɪɴᴋs ᴛᴏ Sʜᴏʀᴛ ʟɪɴᴋs ᴜsɪɴɢ ʏᴏᴜʀ ᴀᴩɪ.

๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ Hᴇʟᴩ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.

๏ By - @TechifyBots</b>'''

LOG_TEXT = '''<b>#NewUser
    
ID - <code>{}</code>

Name - {}</b>'''

HELP_TXT = '''Send Shortener URL & API along with the command.

Ex: <code>/shortlink example.com api</code>

Now send me any link I will convet that link into your connected Shortener

If you want to remove your Shortener then use <code>/remove</code> command.'''

FORCE_SUBSCRIBE_TEXT = '''<b>{}, Tᴏ ᴜsᴇ ᴛʜᴇ ʙᴏᴛ ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ғɪʀsᴛ. Tʜᴇ ʙᴏᴛ ᴡɪʟʟ ɴᴏᴛ ᴘʀᴏᴄᴇss ᴀɴʏ ʀᴇǫᴜᴇsᴛs ᴡɪᴛʜᴏᴜᴛ ᴊᴏɪɴɪɴɢ.

बॉट का उपयोग करने के लिए आपको पहले हमारे चैनल में Join होना होगा। बॉट बिना शामिल हुए किसी भी Request को Process नहीं करेगा।</b>'''

ABOUT_TXT = '''<b>╔════❰ ShortLink Bot ❱═══❍
║ ┏━━━━━━━━━❥
║ ┣ Mʏ ɴᴀᴍᴇ -> {}
║ ┣ Mʏ Oᴡɴᴇʀ -> @CallOwnerBot
║ ┣ Uᴘᴅᴀᴛᴇꜱ -> @TechifyBots
║ ┣ 𝖲ᴜᴘᴘᴏʀᴛ -> @TechifySupport
║ ┣ ๏ Cʜᴇᴄᴋ ʜᴇʟᴘ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ.
║ ┗━━━━━━━━━❥
╚═════❰ @ ❱═════❍</b>'''
