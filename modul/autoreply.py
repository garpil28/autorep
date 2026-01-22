import random
from modules.ai import ai_generate
from modules.system import *
from modules.utils import fake_typing
from config import COOLDOWN, FORWARD_TO

PRIVATE_MSG = [
    "👤 Saya sedang tidak aktif sekarang.",
    "📩 Pesan kamu sudah masuk.",
    "🙋 Lagi AFK sebentar."
]

GROUP_MSG = [
    "💬 Auto reply aktif.",
    "⚡ Saya sedang AFK.",
    "🖤 Pesan diterima."
]

CHANNEL_MSG = [
    "📢 Pesan channel diterima.",
    "👁️ Saya sedang offline."
]

EMJ = ["🔥","💀","⚡","💬","👁️","🖤"]

async def auto_reply(client, event, ai_mode=False):
    chat = event.chat_id

    if is_silent():
        return

    if not can_reply(chat, COOLDOWN):
        return

    await fake_typing(client, event)

    if ai_mode:
        msg = await ai_generate(event.text)
    else:
        if event.is_private:
            msg = random.choice(PRIVATE_MSG)
        elif event.is_group:
            msg = random.choice(GROUP_MSG)
        else:
            msg = random.choice(CHANNEL_MSG)

    try:
        await event.reply(msg)
        responded.add(chat)
    except:
        pass

    try:
        await event.react(random.choice(EMJ))
    except:
        pass

    if FORWARD_TO:
        try:
            await client.send_message(FORWARD_TO, f"[Forward] {event.text}")
        except:
            pass

    try:
        with open("logs/chatlog.txt", "a", encoding="utf8") as f:
            f.write(f"{chat}: {event.text}\n")
    except:
        pass
