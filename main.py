import logging
import os
import openai
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

# Чтение переменных окружения, переданных через Render
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)
openai.api_key = OPENAI_API_KEY

logging.basicConfig(level=logging.INFO)

@dp.message_handler()
async def handle_message(message: Message):
    user_input = message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # или "gpt-3.5-turbo"
            messages=[{"role": "user", "content": user_input}],
            max_tokens=1000,
        )
        answer = response['choices'][0]['message']['content']
        await message.answer(answer)
    except Exception as e:
        await message.answer("Произошла ошибка: " + str(e))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
