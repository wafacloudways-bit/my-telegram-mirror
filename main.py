import os
from pyrogram import Client, filters

# Configuration from GitHub Secrets
API_ID = int(os.environ.get("39677050"))
API_HASH = os.environ.get("97c25b366220c46967ffddfd4e67e79f")
SESSION_STRING = os.environ.get("BQJdbHoAW6kaRla6YmJuZqDIu2mENl0rNlSRw5O6vcFEPhBFEeUeSwHjkqBju8weyC4UDN38FXvtrbgEQMruQqjJtsuEl0LUsEMw7pyduUhnM5xmAaF18GEG6FIXFjhZMy3lv87dbcMNsuwB0KcxAUcd2rnLoqSkMRCRODpuduC6GBv7FLaw8nBH-izBDeBB4IjHH7GfQeC1LzjLHez_zEHsdf65lX33ZtJDMBpgU4W4fUdJpa7VkqcYzPmtsBsRj_1Quf5lB5coUeuEiMQLV7nYzF_pPQepNb4AuIisKhpVj2tBSVGZ2Ap29-Ll1LocuSZ-zxLkPqxCo9I1gUk-F3MH1EeaBAAAAAFsbMDAAA")
BOT_TOKEN = os.environ.get("8314249733:AAEypq_2wYnD1hYlhfeUDwWsZAWQSDqUYL8") # Your token from @BotFather
TARGET_BOT_ID = int(os.environ.get("8266418198"))
MY_GC_ID = int(os.environ.get("-5202338316"))

# This is your Userbot (to read the target bot)
user_app = Client("user_session", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

# This is your Bot (to send messages to the GC)
bot_app = Client("bot_session", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# 1. Listen for messages in GC and send them to the Target Bot
@user_app.on_message(filters.chat(MY_GC_ID) & filters.text & ~filters.me)
async def forward_to_target(client, message):
    await user_app.send_message(TARGET_BOT_ID, message.text)

# 2. Listen for the Target Bot's reply and make your BOT send it to GC
@user_app.on_message(filters.chat(TARGET_BOT_ID))
async def forward_back_to_gc(client, message):
    # We use bot_app here so the BOT sends the message
    await bot_app.send_message(MY_GC_ID, message.text)

# Start both clients
bot_app.start()
user_app.run()
