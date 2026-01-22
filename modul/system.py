import time
from datetime import datetime
from config import SILENT_START, SILENT_END

last_reply = {}
responded = set()

def is_silent():
    h = datetime.now().hour
    return SILENT_START <= h < SILENT_END

def can_reply(chat_id, cd):
    now = time.time()
    if chat_id not in last_reply:
        last_reply[chat_id] = now
        return True
    if now - last_reply[chat_id] >= cd:
        last_reply[chat_id] = now
        return True
    return False
