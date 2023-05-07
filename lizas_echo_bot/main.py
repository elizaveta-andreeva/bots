from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = "6053183832:AAEk8wUJyEIgkiSBock2aFiv_F8eAIRv0KE"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command_reply(message: types.Message):
    await message.reply("Hello! Send me message!")


@dp.message_handler(commands=['help'])
async def help_command_reply(message: types.Message):
    await message.reply("Send me message and i will send it back!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
