from modules.system import responded
from config import *

AUTO = True
AI = False

async def run_commands(event):
    global AUTO, AI, COOLDOWN

    cmd = event.raw_text.lower()

    if cmd.startswith(".autorep on"):
        AUTO = True
        return await event.reply("✅ Auto Reply AKTIF.")

    if cmd.startswith(".autorep off"):
        AUTO = False
        return await event.reply("❌ Auto Reply MATI.")

    if cmd.startswith(".mode ai on"):
        AI = True
        return await event.reply("🤖 Mode AI ON.")

    if cmd.startswith(".mode ai off"):
        AI = False
        return await event.reply("🛑 Mode AI OFF.")

    if cmd.startswith(".delay"):
        try:
            COOLDOWN = int(cmd.split(" ")[1])
            return await event.reply(f"⏱️ Delay diatur ke {COOLDOWN} detik.")
        except:
            return await event.reply("Format salah. Contoh: `.delay 5`")

    if cmd.startswith(".list on"):
        if not responded:
            return await event.reply("⚠️ Tidak ada chat aktif.")
        txt = "📜 Chat aktif:\n" + "\n".join([f"- `{x}`" for x in responded])
        return await event.reply(txt)

    return None
