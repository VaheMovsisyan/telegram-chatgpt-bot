import logging
import os
import openai
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

# Загружаем переменные окружения (должны быть установлены в Render)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Настраиваем бота
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

# Настраиваем OpenAI
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Логирование
logging.basicConfig(level=logging.INFO)

# Обработчик всех входящих сообщений
@dp.message_handler()
async def handle_message(message: Message):
    user_input = message.text
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # или gpt-3.5-turbo, если хочешь
            messages=[{"role": "user", "content": user_input}],
            max_tokens=1000,
        )
        answer = response.choices[0].message.content
        await message.answer(answer)
    except Exception as e:
        await message.answer("Произошла ошибка: " + str(e))

# Запуск
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
