from pyrogram import Client, filters

# --- DIRECT CONFIGURATION ---
# Use numbers for IDs (no quotes) and text for Strings (with quotes)
API_ID = 39677050
API_HASH = "97c25b366220c46967ffddfd4e67e79f"
SESSION_STRING = "BQJdbHoAW6kaRla6YmJuZqDIu2mENl0rNlSRw5O6vcFEPhBFEeUeSwHjkqBju8weyC4UDN38FXvtrbgEQMruQqjJtsuEl0LUsEMw7pyduUhnM5xmAaF18GEG6FIXFjhZMy3lv87dbcMNsuwB0KcxAUcd2rnLoqSkMRCRODpuduC6GBv7FLaw8nBH-izBDeBB4IjHH7GfQeC1LzjLHez_zEHsdf65lX33ZtJDMBpgU4W4fUdJpa7VkqcYzPmtsBsRj_1Quf5lB5coUeuEiMQLV7nYzF_pPQepNb4AuIisKhpVj2tBSVGZ2Ap29-Ll1LocuSZ-zxLkPqxCo9I1gUk-F3MH1EeaBAAAAAFsbMDAAA"
BOT_TOKEN = "8314249733:AAEypq_2wYnD1hYlhfeUDwWsZAWQSDqUYL8"
TARGET_BOT_ID = 8266418198
MY_GC_ID = -5202338316 
# ----------------------------

# This is your Userbot (to read the target bot)
user_app = Client("user_session", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)

# This is your Bot (to send messages to the GC)
bot_app = Client("bot_session", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# 1. Listen for messages in GC and send them to the Target Bot
@user_app.on_message(filters.chat(MY_GC_ID) & filters.text & ~filters.me)
async def forward_to_target(client, message):
    try:
        await user_app.send_message(TARGET_BOT_ID, message.text)
    except Exception as e:
        print(f"Error sending to target: {e}")

# 2. Listen for the Target Bot's reply and make your BOT send it to GC
@user_app.on_message(filters.chat(TARGET_BOT_ID))
async def forward_back_to_gc(client, message):
    try:
        await bot_app.send_message(MY_GC_ID, message.text)
    except Exception as e:
        print(f"Error sending to GC: {e}")

# Start both clients
print("Bot is starting...")
bot_app.start()
user_app.run()
