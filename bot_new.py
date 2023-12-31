letter_dict = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TS',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ы': 'Y',
    'Ъ': 'IE',
    'Э': 'E',
    'Ю': 'IU',
    'Я': 'IA'
}

import logging
import os
from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Пиши слова капсом слитно, пожалуйста:)'
    logging.info(f"{user_name=} {user_id=} sent message: {message.text}")
    await message.reply(text)


@dp.message_handler()
async def send_transliterate(message: types.Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    text = ''.join([letter_dict[i] for i in str(message.text).upper()])
    logging.info(f'{user_name} {user_id} sent message:{text}')    
    await bot.send_message(user_id, text)


if __name__ == '__main__':
    executor.start_polling(dp)

   
