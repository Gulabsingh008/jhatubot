import os
import logging

# Telegram API
API_ID = os.environ.get('TELEGRAM_API', '26494161')
API_HASH = os.environ.get('TELEGRAM_HASH', '55da841f877d16a3a806169f3c5153d3')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '7758524025:AAEVf_OePVQ-6hhM1GfvRlqX3QZIqDOivtw')

# Chat IDs
DUMP_CHAT_ID = int(os.environ.get('DUMP_CHAT_ID', '-1002030723564'))
FSUB_ID = int(os.environ.get('FSUB_ID', '-1002237630219'))

# User Session
USER_SESSION_STRING = os.environ.get('USER_SESSION_STRING', '')
if not USER_SESSION_STRING:
    logging.info("USER_SESSION_STRING is empty! Bot will split Files in 2Gb...")
    USER_SESSION_STRING = None

# Split Size (depends on session string)
SPLIT_SIZE = 4241280205 if USER_SESSION_STRING else 2093796556

# Valid Domains
VALID_DOMAINS = [
    'terabox.com', 'nephobox.com', '4funbox.com', 'mirrobox.com', 
    'momerybox.com', 'teraboxapp.com', '1024tera.com', 
    'terabox.app', 'gibibox.com', 'goaibox.com', 'terasharelink.com', 
    'teraboxlink.com', 'terafileshare.com'
]
