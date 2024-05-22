import logging

from pyrogram import Client
from pyrogram.types import Message


logging.basicConfig(level=logging.INFO)
bot = Client("bot", bot_token="6512323989:AAGWIkh4Z2O86edPTiqlO9_VFuz_fQy2IFY", api_id=27079123, api_hash="e8c46803022703d503c35ab49ee419af")

@bot.on_message()
async def main(bot: Client, msg: Message):
    await msg.reply("test")
    match msg.text.lower():
        case "шлюха":
            await msg.reply(text="ты че ахуел")

        case "привет":
            await msg.reply("добро пожаловать")

        case "пока":
            await msg.reply("динаху")

        case "сам":
            await msg.reply("динаху")

        case "сука":
            await msg.reply("бро,не матерись пж")

        case "пидорас":
            await msg.reply("бро,не матерись пж")

        case "гондон":
            await msg.reply("бро,не матерись пж")

        case "немец":
            await msg.reply("бро,не матерись пж")

bot.run()