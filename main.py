from telethon import TelegramClient, events
from modules.autoreply import auto_reply
from modules.commands import run_commands, AUTO, AI
from config import API_ID, API_HASH

client = TelegramClient("session", API_ID, API_HASH)

@client.on(events.NewMessage)
async def handler(event):
    # Commands dulu
    if event.raw_text.startswith("."):
        return await run_commands(event)

    # Auto reply
    if AUTO:
        await auto_reply(client, event, AI)

print("🔥 PROFESSIONAL USERBOT RUNNING…")
client.start()
client.run_until_disconnected()
