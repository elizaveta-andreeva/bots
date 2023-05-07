import datetime
import time

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command_reply(message: types.Message):
    await message.reply("Hello! Send me message!")


@dp.message_handler(commands=['help'])
async def help_command_reply(message: types.Message):
    await message.reply("Send me message!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    filename = ".\\" + str(msg.from_user.username) + ".txt"
    msg_time = datetime.datetime.now()
    reply = "You sent: " + msg.text + ". I don't like it. Try again!"
    with open(filename, "a") as file:
        bot_reply_time = datetime.datetime.now()
        log_info = "User {}: {} - {}\n".format(msg.from_user.username, msg.text, msg_time) + "Bot: {} - {}\n".format(
            reply, bot_reply_time)
        file.write(log_info)
    await bot.send_message(msg.from_user.id, reply)


if __name__ == '__main__':
    executor.start_polling(dp)
