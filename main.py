import requests
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '8658342011:AAF4LP0xG4cj9VLUspN32kMJR7_4I0ghoEk'
API_KEY = '863bb56ef29bf0f48d3ae70a759a5463'
URL_WEATHER_API = 'https://api.openweathermap.org/data/2.5/weather'
GEOCODER_URL = 'http://api.openweathermap.org/geo/1.0/direct'

GEOCODER_PARAMS = {
   'appid': API_KEY
}

WEATHER_PARAMS = {
   'appid': API_KEY,
   'units': 'metric',
   'lang': 'ru'
}



EMOJI_CODE = {200: '⛈',
              201: '⛈',
              202: '⛈',
              210: '🌩',
              211: '🌩',
              212: '🌩',
              221: '🌩',
              230: '⛈',
              231: '⛈',
              232: '⛈',
              301: '🌧',
              302: '🌧',
              310: '🌧',
              311: '🌧',
              312: '🌧',
              313: '🌧',
              314: '🌧',
              321: '🌧',
              500: '🌧',
              501: '🌧',
              502: '🌧',
              503: '🌧',
              504: '🌧',
              511: '🌧',
              520: '🌧',
              521: '🌧',
              522: '🌧',
              531: '🌧',
              600: '🌨',
              601: '🌨',
              602: '🌨',
              611: '🌨',
              612: '🌨',
              613: '🌨',
              615: '🌨',
              616: '🌨',
              620: '🌨',
              621: '🌨',
              622: '🌨',
              701: '🌫',
              711: '🌫',
              721: '🌫',
              731: '🌫',
              741: '🌫',
              751: '🌫',
              761: '🌫',
              762: '🌫',
              771: '🌫',
              781: '🌫',
              800: '☀',
              801: '🌤',
              802: '☁',
              803: '☁',
              804: '☁'}

bot = telebot.TeleBot(TOKEN)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Получить погоду', request_location=True))
keyboard.add(KeyboardButton('Получить погоду по названию города'))
keyboard.add(KeyboardButton('О проекте'))



def get_weather(lat, lon):

    params = {'lat': lat,
              'lon': lon,
              'lang': 'ru',
              'units': 'metric',
              'appid': API_KEY}
    
    response = requests.get(url=URL_WEATHER_API, params=params).json()
    city_name = response['name']
    description = response['weather'][0]['description']
    code = response['weather'][0]['id']
    temp = response['main']['temp']
    temp_feels_like = response['main']['feels_like']
    humidity = response['main']['humidity']
    emoji = EMOJI_CODE[code]
    message = f'🏙 Погода в: {city_name}\n'
    message += f'{emoji} {description.capitalize()}.\n'
    message += f'🌡 Температура {temp}°C.\n'
    message += f'🌡 Ощущается {temp_feels_like}°C.\n'
    message += f'💧 Влажность {humidity}%.\n'
    return message


@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = 'Отправь мне свое местоположение и я отправлю тебе погоду.'
    bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def send_weather(message):
    lon = message.location.longitude
    lat = message.location.latitude
    result = get_weather(lat, lon)
    bot.send_message(message.chat.id, result, reply_markup=keyboard)



@bot.message_handler(regexp='Получить погоду по названию локации')
def get_city(message:telebot.types.Message):
    msg = bot.send_message(message.chat.id, 'Введи название локации: ')
    bot.register_next_step_handler(msg, get_city_coords_weather)

def get_city_coords_weather(message: telebot.types.Message):
   

    GEOCODER_PARAMS['q'] = message.text
    json = requests.get(GEOCODER_URL, GEOCODER_PARAMS).json()
    lat, lon = json[0]['lat'], json[0]['lon']

    WEATHER_PARAMS['lat'], WEATHER_PARAMS['lon'] = lat, lon
    response = requests.get(URL_WEATHER_API, WEATHER_PARAMS).json()
    city_name = response['name']
    description = response['weather'][0]['description']
    code = response['weather'][0]['id']
    temp = response['main']['temp']
    temp_feels_like = response['main']['feels_like']
    humidity = response['main']['humidity']
    emoji = EMOJI_CODE[code]
    message1 = f'🏙 Погода в: {city_name}\n'
    message1 += f'{emoji} {description.capitalize()}.\n'
    message1 += f'🌡 Температура {temp}°C.\n'
    message1 += f'🌡 Ощущается {temp_feels_like}°C.\n'
    message1 += f'💧 Влажность {humidity}%.\n'
    bot.send_message(message.chat.id, message1)



@bot.message_handler(regexp='О проекте')
def send_about(message):
    text = 'Бот позволяет получить погоду в текущем местоположении!\n'
    text += 'Для получения погоды - отправь боту геопозицию.\n'
    text += 'Погода берется с сайта https://openweathermap.org.\n'
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

print("Бот погоды запущен...")
bot.infinity_polling()








# import math


# class Fraction:
#     def __init__(self, num, den):
#         self.num, self.den = self.get_reduced_fraction(num, den)

#     @staticmethod
#     def get_reduced_fraction(num, den):
#         gcd = math.gcd(num, den)
#         return num // gcd, den // gcd

#     @staticmethod
#     def get_common_denominator(den1, den2):
#         common_den = den1 * den2 // math.gcd(den1, den2)
#         return common_den

#     def __add__(self, other):
#         common_den = self.get_common_denominator(self.den, other.den)
#         num = common_den // self.den * self.num + common_den // other.den * other.num
#         num, den = self.get_reduced_fraction(num, common_den)
#         return Fraction(num, den)

#     def __sub__(self, other):
#        common_den = self.get_common_denominator(self.den, other.den)
#        num = common_den // self.den * self.num - common_den // other.den * other.num
#        num, den = self.get_reduced_fraction(num, common_den)
#        return Fraction(num, den)
    

#     def __mul__(self, other):
#         num = self.num * other.num
#         den = self.den * other.den
#         num, den = self.get_reduced_fraction(num, den)
#         return Fraction(num, den)
    

#     def __truediv__(self, other):
#         num = self.num * other.den
#         den = self.den * other.num
#         num, den = self.get_reduced_fraction(num, den)
#         return Fraction(num, den)
    
#     def __lt__(self, other):
#        common_den = self.get_common_denominator(self.den, other.den)
#        return common_den // self.den * self.num < common_den // other.den * other.num







#     def __repr__(self):
#         return f'{self.num}/{self.den}'



# fr1 = Fraction(1,2)
# fr2 = Fraction(2,3)

# print(fr1+fr2)
# print(fr1-fr2)
# print(fr1*fr2)
# print(fr1/fr2)#1/2*3/1
# print(fr1<fr2)




