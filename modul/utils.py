import asyncio, random
from telethon import functions, types

async def fake_typing(client, event):
    try:
        await client(functions.messages.SetTypingRequest(
            peer=event.chat_id,
            action=types.SendMessageTypingAction()
        ))
        await asyncio.sleep(random.uniform(0.5, 1.2))
    except:
        pass
