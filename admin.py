from pyrogram import Client, filters
from pyrogram.types import Message
from config import ADMINS
from database.mongodb import ban_user, unban_user, get_banned_users, get_total_users, get_all_users

# ✅ Only admin filter
admin_filter = filters.user(ADMINS)

@Client.on_message(filters.command("ban") & admin_filter)
async def ban_command(bot, message: Message):
    if len(message.command) < 2:
        return await message.reply("🚫 Usage: /ban <user_id>")
    
    user_id = int(message.command[1])
    await ban_user(user_id)
    await message.reply(f"❌ User `{user_id}` banned.")

@Client.on_message(filters.command("unban") & admin_filter)
async def unban_command(bot, message: Message):
    if len(message.command) < 2:
        return await message.reply("✅ Usage: /unban <user_id>")
    
    user_id = int(message.command[1])
    await unban_user(user_id)
    await message.reply(f"✅ User `{user_id}` unbanned.")

@Client.on_message(filters.command("stats") & admin_filter)
async def stats_command(bot, message: Message):
    total = await get_total_users()
    banned = await get_banned_users()
    await message.reply(f"📊 Stats:\n👥 Total Users: `{total}`\n⛔ Banned Users: `{banned}`")

@Client.on_message(filters.command("users") & admin_filter)
async def users_list(bot, message: Message):
    users = await get_all_users()
    text = "👥 Users:\n" + "\n".join([f"`{u['user_id']}` - {u['name']}" for u in users[:50]])  # Show first 50 users
    await message.reply(text or "No users found.")
