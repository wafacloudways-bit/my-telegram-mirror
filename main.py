from pyrogram import Client, filters
import asyncio

# --- DIRECT CONFIGURATION ---
API_ID = 39677050
API_HASH = "97c25b366220c46967ffddfd4e67e79f"
SESSION_STRING = "BQJdbHoAW6kaRla6YmJuZqDIu2mENl0rNlSRw5O6vcFEPhBFEeUeSwHjkqBju8weyC4UDN38FXvtrbgEQMruQqjJtsuEl0LUsEMw7pyduUhnM5xmAaF18GEG6FIXFjhZMy3lv87dbcMNsuwB0KcxAUcd2rnLoqSkMRCRODpuduC6GBv7FLaw8nBH-izBDeBB4IjHH7GfQeC1LzjLHez_zEHsdf65lX33ZtJDMBpgU4W4fUdJpa7VkqcYzPmtsBsRj_1Quf5lB5coUeuEiMQLV7nYzF_pPQepNb4AuIisKhpVj2tBSVGZ2Ap29-Ll1LocuSZ-zxLkPqxCo9I1gUk-F3MH1EeaBAAAAAFsbMDAAA"
BOT_TOKEN = "8314249733:AAEypq_2wYnD1hYlhfeUDwWsZAWQSDqUYL8"

# GET THE CORRECT IDs
TARGET_BOT_ID = 8266418198
MY_GC_ID = -1003392975167  # Updated from your screenshot
# ----------------------------

user_app = Client("user_session", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING)
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

async def main():
    print("Starting clients...")
    await user_app.start()
    await bot_app.start()
    
    # FORCE RESOLVE PEER IDs
    print("Resolving IDs...")
    try:
        await user_app.get_chat(MY_GC_ID)
        await bot_app.get_chat(MY_GC_ID)
        print("Successfully connected to Group Chat!")
    except Exception as e:
        print(f"FAILED to find Group: {e}. Is your bot/user inside the GC?")
        
    print("Bot is now listening for messages!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
