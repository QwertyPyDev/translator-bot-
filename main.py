from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator, LANGUAGES

from config import TOKEN_API


bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot=bot)
translator = Translator()

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, text='''Привет, я переводчик с Русского на Английский а также наоборот.
Просто напишите любой текст на одном из двух языков, и я автоматически перевожу на другой😉''')

@dp.message_handler(content_types=['text'])
async def translate(message: types.Message) -> None:
    lang = translator.detect(message.text).lang
    dest_lang = 'en' if lang == 'ru' else 'ru'
    translated_text = translator.translate(message.text, dest=dest_lang).text
    await message.reply(translated_text)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)