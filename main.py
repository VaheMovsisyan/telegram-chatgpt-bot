import logging
import os
import openai
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

# 💡 Читаем переменные по их ИМЕНАМ
TELEGRAM_TOKEN = os.environ.get("7891979481:AAF7baXkYDAiWxYsOh9NWRe3Sl1WO5lww0A")
OPENAI_API_KEY = os.environ.get("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")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)
openai.api_key = OPENAI_API_KEY

logging.basicConfig(level=logging.INFO)

@dp.message_handler()
async def handle_message(message: Message):
    user_input = message.text
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Можно заменить на "gpt-3.5-turbo"
            messages=[{"role": "user", "content": user_input}],
            max_tokens=1000,
        )
        answer = response['choices'][0]['message']['content']
        await message.answer(answer)
    except Exception as e:
        await message.answer("Произошла ошибка: " + str(e))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
