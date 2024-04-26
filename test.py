import telebot
from telebot import types

bot = telebot.TeleBot('7183441722:AAESpFiG34LtKoSNezRf3vM78pbFapYBuX0')

@bot.message_handler(commands=['start'])
def start(message):
    full_name = f'Привет, <u>{message.from_user.first_name} {message.from_user.last_name}</u>, снизу можешь выбрать программу тренировок и узнать их стоимость.'
    bot.send_message(message.chat.id, full_name, parse_mode='html')
    bot.send_message(message.chat.id,f"Чтобы воспользоваться встроенной клавиатурой напишите /help")

@bot.message_handler(commands=['help'])
def keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttonA = types.KeyboardButton('Программа тренировок')
    buttonB = types.KeyboardButton('Стоимость')
    buttonC = types.KeyboardButton('Контакты и адреса')
    markup.row(buttonA, buttonB, buttonC)
    bot.send_message(message.chat.id, '😀', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Программа тренировок')
def workout_program(message):
    # отправка изображения
    with open('workout_program.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)
    # отправка текста
    bot.send_message(message.chat.id, 'Это программа тренировок.')

@bot.message_handler(func=lambda message: message.text == 'Стоимость')
def price(message):
    bot.send_message(message.chat.id, 'Это стоимость.')

@bot.message_handler(func=lambda message: message.text == 'Контакты и адреса')
def contacts(message):
    bot.send_message(message.chat.id, 'Это контакты и адреса.')

bot.polling(none_stop=True)