import os
from dotenv import load_dotenv

load_dotenv('config.env', override=True)

class Config:
    TELEGRAM_API = os.getenv("TELEGRAM_API", "26494161")
    TELEGRAM_HASH = os.getenv("TELEGRAM_HASH", "55da841f877d16a3a806169f3c5153d3")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    DUMP_CHAT_ID = int(os.getenv("DUMP_CHAT_ID", "-1002030723564"))
    FSUB_ID = int(os.getenv("FSUB_ID", "-1002237630219"))
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", None)
    SPLIT_SIZE_USER = 4241280205  # 4GB+
    SPLIT_SIZE_BOT = 2093796556  # 2GB
    ARIA_SECRET = os.getenv("ARIA_SECRET", "")
    ARIA_HOST = os.getenv("ARIA_HOST", "http://localhost")
    ARIA_PORT = int(os.getenv("ARIA_PORT", 6800))
    VALID_DOMAINS = [
        'terabox.com', 'nephobox.com', '4funbox.com', 'mirrobox.com',
        'momerybox.com', 'teraboxapp.com', '1024tera.com', 'terabox.app',
        'gibibox.com', 'goaibox.com', 'terasharelink.com', 
        'teraboxlink.com', 'terafileshare.com'
    ]
