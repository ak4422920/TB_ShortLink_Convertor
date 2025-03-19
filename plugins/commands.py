from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import db
from configs import *
from utilities import short_link, save_data


@Client.on_message(filters.command('start') & filters.private)
async def start_handler(c, m):
    try:
        user_id = m.from_user.id
        user_mention = m.from_user.mention

        if not await db.is_present(user_id):
            await db.add_user(user_id)
            await c.send_message(LOG_CHANNEL, LOG_TEXT.format(user_id, user_mention))

        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("About", callback_data="about"),
             InlineKeyboardButton("Help", callback_data="help")],
            [InlineKeyboardButton("Developer", url="https://youtube.com/@techifybots")]
        ])

        await m.reply_text(
            START_TXT.format(user_mention),
            reply_markup=keyboard
        )
    except Exception as e:
        print(f"Error in start_handler: {e}")


@Client.on_message(filters.command('shortlink') & filters.private)
async def save_shortlink(c, m):
    if len(m.command) < 3:
        await m.reply_text(
            "<b>🕊️ Incomplete Command:\n\n"
            "Provide a shortener URL & API key along with the command.\n\n"
            "Example: <code>/shortlink example.com api_key</code>\n"
            "⚡ Updates - @TechifyBots</b>"
        )
        return    

    usr = m.from_user
    shortener_url = m.command[1]
    api_key = m.command[2]

    # Validate the URL format
    if not shortener_url.startswith(("http://", "https://")):
        shortener_url = f"https://{shortener_url}"  # Ensure proper formatting

    try:
        elg = await save_data(shortener_url, api_key, uid=usr.id)
        if elg:
            short_url = await db.get_value('shortner', uid=usr.id)
            short_api = await db.get_value('api', uid=usr.id)
            await m.reply_text(
                f"📍 Shortener has been set successfully!\n\n"
                f"Shortener URL - `{short_url}`\n"
                f"Shortener API - `{short_api}`\n"
                "⚡ Updates - @TechifyBots"
            )
        else:
            await m.reply_text("🌶️ Error:\n\nInvalid Shortlink API or URL. Please check again!")
    except Exception as e:
        await m.reply_text(f"⚠️ An error occurred while saving the shortener: {e}")


@Client.on_message(filters.command('remove') & filters.private)
async def remove(c, m):
    usr = m.from_user
    short_url = await db.get_value('shortner', uid=usr.id)

    if not short_url:
        await m.reply_text("😂 You haven't set any shortener yet. What do you want to remove?")
        return

    try:
        await db.delete_value('shortner', uid=usr.id)
        await db.delete_value('api', uid=usr.id)
        await m.reply_text("✅ Successfully removed your shortener settings.")
    except Exception as e:
        await m.reply_text(f"⚠️ An error occurred while removing the shortener: {e}")

@Client.on_message(filters.text | filters.caption & ~filters.command(['start', 'shortlink', 'remove', 'users', 'broadcast']) & (filters.private | filters.channel))
async def shorten_link(c, m):
    txt = m.text or m.caption
    if not any(proto in txt for proto in ["http://", "https://"]):
        await m.reply_text("❌ Please send a valid link that starts with http:// or https://.")
        return

    try:
        words = txt.split()
        for i, word in enumerate(words):
            if word.startswith(("http://", "https://")):
                short = await short_link(link=word, uid=m.from_user.id if m.from_user else None)
                words[i] = short
                break

        new_text = " ".join(words)

        if m.chat.type == "private":
            await m.reply_text(f"✅ Here is your shortened link:\n\n<code>{short}</code>")
        elif m.caption:
            await m.edit_caption(new_text)
        else:
            await m.edit_text(new_text)

    except Exception as e:
        await m.reply_text(f"⚠️ Error shortening link: {e}")