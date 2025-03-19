import os
import time
import asyncio
import datetime
from configs import ADMINS
from .database import db
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked, PeerIdInvalid

@Client.on_message(filters.command("stats") & filters.user(ADMIN))
async def get_stats(c, m):
    mr = await m.reply('**𝙰𝙲𝙲𝙴𝚂𝚂𝙸𝙽𝙶 𝙳𝙴𝚃𝙰𝙸𝙻𝚂.....**')
    users = await db.total_users_count()
    new_text = f"<b>◉ ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{users}</code></b>"

    if getattr(mr, "text", None) != new_text:
        await mr.edit(text=new_text)

@Client.on_message(filters.command("broadcast") & filters.user(ADMIN) & filters.reply)
async def broadcast_handler(c, m):
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_message
    sts_msg = await m.reply_text("Broadcast started!")
    done, failed, success = 0, 0, 0
    start_time = time.time()
    total_users = await db.total_users_count()

    async for user in all_users:
        sts = await send_msg(c, user['id'], broadcast_msg)
        if sts == 200:
            success += 1
        else:
            failed += 1
        if sts == 400:
            await db.delete_user(user['id'])
        done += 1
        if not done % 20:
            await sts_msg.edit(f"Broadcast in progress:\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nFailed: {failed}")

    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await sts_msg.edit(f"Broadcast Completed:\nCompleted in `{completed_in}`.\n\nTotal Users {total_users}\nCompleted: {done} / {total_users}\nSuccess: {success}\nFailed: {failed}")

async def send_msg(c, user_id, message):
    try:
        await message.copy(chat_id=int(user_id))
        return 200
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return await send_msg(c, user_id, message)
    except InputUserDeactivated:
        await db.delete_user(int(user_id))
        print(f"{user_id} : deactivated")
        return 400
    except UserIsBlocked:
        await db.delete_user(int(user_id))
        print(f"{user_id} : blocked the bot")
        return 400
    except PeerIdInvalid:
        await db.delete_user(int(user_id))
        print(f"{user_id} : user id invalid")
        return 400
    except Exception as e:
        print(f"{user_id} : {e}")
        return 500
