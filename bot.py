import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton

from telebot.util import quick_markup

TOKEN = '8658342011:AAF4LP0xG4cj9VLUspN32kMJR7_4I0ghoEk'

bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True )
keyboard.add(telebot.types.KeyboardButton('Котика!'))

# markup = quick_markup({
#     'Котика': {'url': 'https://cataas.com/cat'},
# }, row_width=1)


@bot.message_handler(commands=['start'])
def send_welcome(message: telebot.types.Message):
     bot.send_message(message.chat.id, 'Йоу, здарова, меня зовут Зубенко Михаил, <<мафиозник>>', reply_markup=keyboard)

@bot.message_handler(commands=['help'])
def pupu(message: telebot.types.Message):
     bot.send_message(message.chat.id, 'Пу-пу-пу')


@bot.message_handler(regexp=r'Котика\.*')
def hello(message: telebot.types.Message):
     bot.send_photo(message.chat.id, 'https://cataas.com/cat')


@bot.message_handler(content_types=['text'])
def echo_message(message: telebot.types.Message):
     bot.send_message(message.chat.id, message.text)


print('Бот запущен...')
bot.infinity_polling()


# import telebot

# TOKEN = '8661181134:AAHjjm8QpkOBWLqpAffGNaUZQGt9e7DD3e0'

# bot = telebot.TeleBot(TOKEN)

# keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True )
# keyboard.add(telebot.types.KeyboardButton('Hello'))
# keyboard.add(telebot.types.KeyboardButton('Bye'))


# @bot.message_handler(commands=['start'])
# def send_welcome(message: telebot.types.Message):
#      bot.send_message(message.chat.id, 'Привет, я Саня Плюш, <<художница>>', reply_markup=keyboard)

# @bot.message_handler(commands=['help'])
# def pupu(message: telebot.types.Message):
#      bot.send_message(message.chat.id, 'Плюшка Рей топ')



# @bot.message_handler(content_types=['text'])
# def echo_message(message: telebot.types.Message):
#      bot.send_message(message.chat.id, message.text)

# print('Бот запущен...')
# bot.infinity_polling()
