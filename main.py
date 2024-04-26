import requests
from bs4 import BeautifulSoup
from UrlFunction import get_url
import asyncio
import telebot
from telebot import types
from save_img import save_function_main
from langdetect import detect


bot = telebot.TeleBot('7183441722:AAESpFiG34LtKoSNezRf3vM78pbFapYBuX0')
images = []
save_helper = False
check_number = False


@bot.message_handler(commands=['go'])
def start(message):
    full_name = f'Привет, <u>{message.from_user.first_name} {message.from_user.last_name}</u>, я бот для помощи с домашней работой, выбери предмет. Помощь /help'
    bot.send_message(message.chat.id, full_name, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttonA = types.KeyboardButton('Алгебра')
    buttonB = types.KeyboardButton('Русский')
    buttonC = types.KeyboardButton('Англиский')
    buttonD = types.KeyboardButton('Биология')
    buttonE = types.KeyboardButton('Химия')
    buttonF = types.KeyboardButton('Геометрия')
    buttonG = types.KeyboardButton('Литература')
    markup.row(buttonA, buttonB, buttonC, buttonD, buttonE, buttonF, buttonG)
    bot.send_message(message.chat.id, '👇', reply_markup=markup)

@bot.message_handler(commands=['help'])
def start(message):
    full_name = f'Привет, <u>{message.from_user.first_name}</u>, я бот для помощи с домашней работой, что случилось?'
    bot.send_message(message.chat.id, full_name, parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttonA = types.KeyboardButton('Проблемы с вводом данных?')
    buttonB = types.KeyboardButton('Написать о проблеме разработчикам.')
    buttonC = types.KeyboardButton('Как вернуться на предыдущее действие?')
    markup.row(buttonA, buttonB, buttonC)
    bot.send_message(message.chat.id, '😢', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Проблемы с вводом данных?')
def problem_input(message):
    bot.send_message(message.chat.id, 'Вот такой ввод в обычных предмметах(Алгебра, Английский, Русский)')
    bot.send_photo(message.chat.id, photo=open('Problem_input_photo.png', 'rb'))
    bot.send_message(message.chat.id, 'А вот такой ввод в сложных предмметах(Геометрия, Химия)')
    bot.send_photo(message.chat.id, photo=open('Problem_input_photo_2.png', 'rb'))

@bot.message_handler(func=lambda message: message.text == 'Как вернуться на предыдущее действие?')
def problem_input(message):
    bot.send_message(message.chat.id, 'К сожалению это еще не проработанно поэтому просто напишите /go и введите данные заново(')

@bot.message_handler(func=lambda message: message.text == 'Написать о проблеме разработчикам.')
def problem_input(message):
    bot.send_message(message.chat.id, 'https://t.me/vessentness')
    bot.send_message(message.chat.id, 'https://t.me/dmitriy9461')


@bot.message_handler(func=lambda message: message.text == 'Алгебра')
def algebra(message):
    global subject_help
    subject_help = 1
    bot.send_message(message.chat.id, 'Отлично, алгебра. Введи номер своего класса. Помощь /help')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttonA = types.KeyboardButton('7 класс')
    buttonB = types.KeyboardButton('8 класс')
    buttonC = types.KeyboardButton('9 класс')
    markup.row(buttonA, buttonB, buttonC)
    bot.send_message(message.chat.id, '👇', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Русский')
def russkii(message):
    global subject_help
    subject_help = 2
    bot.send_message(message.chat.id, 'Отлично, русский. Введи номер своего класса. Помощь /help')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttonA = types.KeyboardButton('7 класс')
    buttonB = types.KeyboardButton('8 класс')
    buttonC = types.KeyboardButton('9 класс')
    markup.row(buttonA, buttonB, buttonC)
    bot.send_message(message.chat.id, '👇', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Англиский')
def english(message):
    global subject_help
    subject_help = 3
    bot.send_message(message.chat.id, 'Отлично, англиский. Введи номер своего класса. Помощь /help')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttonA = types.KeyboardButton('7 класс')
    buttonB = types.KeyboardButton('8 класс')
    buttonC = types.KeyboardButton('9 класс')
    markup.row(buttonA, buttonB, buttonC)
    bot.send_message(message.chat.id, '👇', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Биология')
def biology(message):
    global subject_help
    subject_help = 4
    bot.send_message(message.chat.id, 'Отлично, биология. Введи номер своего класса. Помощь /help')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttonA = types.KeyboardButton('7 класс')
    buttonB = types.KeyboardButton('8 класс')
    buttonC = types.KeyboardButton('9 класс')
    markup.row(buttonA, buttonB, buttonC)
    bot.send_message(message.chat.id, '👇', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Химия')
def chemistri(message):
    global subject_help
    subject_help = 5
    bot.send_message(message.chat.id, 'Отлично, химия. Введи номер своего класса. Помощь /help')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttonA = types.KeyboardButton('7 класс')
    buttonB = types.KeyboardButton('8 класс')
    buttonC = types.KeyboardButton('9 класс')
    markup.row(buttonA, buttonB, buttonC)
    bot.send_message(message.chat.id, '👇', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Геометрия')
def geometry(message):
    global subject_help
    subject_help = 6
    bot.send_message(message.chat.id, 'Отлично, геометрия. Введи номер своего класса. Помощь /help')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttonA = types.KeyboardButton('7 класс')
    buttonB = types.KeyboardButton('8 класс')
    buttonC = types.KeyboardButton('9 класс')
    markup.row(buttonA, buttonB, buttonC)
    bot.send_message(message.chat.id, '👇', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Литература')
def literatura(message):
    global subject_help
    subject_help = 7
    bot.send_message(message.chat.id, 'Отлично, литература. Введи номер своего класса. Помощь /help')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttonA = types.KeyboardButton('7 класс')
    buttonB = types.KeyboardButton('8 класс')
    buttonC = types.KeyboardButton('9 класс')
    markup.row(buttonA, buttonB, buttonC)
    bot.send_message(message.chat.id, '👇', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == '9 класс')
def data(message):
    global number_of_class
    number_of_class = '9'
    if subject_help != 5 and subject_help != 6 and subject_help != 7:
        bot.send_message(message.chat.id, 'Отлично, 9 класс. Введи номер задания')
    elif subject_help == 5:
        bot.send_message(message.chat.id, 'Отлично, 9 класс. Введи номер задания, номер параграфа и тип задания после(вопросы, подумай ответь выполни, тестовые вопросы). Помощь /help')
    elif subject_help == 6:
        bot.send_message(message.chat.id, 'Отлично, 9 класс. Введи номер задания и номер главы')
    elif subject_help == 7:
        bot.send_message(message.chat.id, 'Отлично, 9 класс. Введи номер задания и номер части учебника.')


@bot.message_handler(func=lambda message: message.text == '7 класс')
def data(message):
    global number_of_class
    number_of_class = '7'
    print(subject_help)
    if subject_help != 5 and subject_help != 6 and subject_help != 7:
        bot.send_message(message.chat.id, 'Отлично, 7 класс. Введи номер задания')
    if subject_help == 5:
        bot.send_message(message.chat.id,
                         'Химии 7 класса нет((. Помощь /help')
    if subject_help == 6:
        bot.send_message(message.chat.id, 'Отлично, 7 класс. Введи номер задания и номер главы')
    if subject_help == 7:
        bot.send_message(message.chat.id, 'Отлично, 9 класс. Введи номер задания и номер части учебника.')

@bot.message_handler(func=lambda message: message.text == '8 класс')
def data(message):
    global number_of_class
    number_of_class = '8'
    if subject_help != 5 and subject_help != 6 and subject_help != 7:
        bot.send_message(message.chat.id, 'Отлично, 8 класс. Введи номер задания')
    if subject_help == 5:
        bot.send_message(message.chat.id,
                         'Отлично, 8 класс. Введи номер параграфа. Помощь /help')
    if subject_help == 6:
        bot.send_message(message.chat.id, 'Отлично, 8 класс. Введи номер задания и номер главы. Помощь /help')
    if subject_help == 7:
        bot.send_message(message.chat.id, 'Отлично, 9 класс. Введи номер задания и номер части учебника.')



@bot.message_handler(func=lambda message: 'тестовые' in message.text or 'вопросы' in message.text or 'подумай' in message.text or ('1' in message.text or '2' in message.text or '3' in message.text or
                     '4' in message.text or '5' in message.text or '6' in message.text or '7' in message.text or '8' in message.text or '9' in message.text or '0' in message.text) and subject_help and number_of_class)
def echo_message(message):
    print(True)
    global images
    global subject_help
    global number_of_class
    if subject_help == 1:
        user_response = message.text
        predmet = 'algebra'
        main_url = asyncio.run(get_url(predmet, user_response, number_of_class))
        page = requests.get(main_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        image_tags = soup.find_all('img', src=True)
        much = 0
        images = []
        for tag in image_tags:
            if '/attachments/images/tasks/' in tag['src']:
                much += 1
                print('Найдено изображение:', f"https:{tag['src']}")
                images.append(f"https:{tag['src']}")
        if images:
            for i in images:
                print(i)
                bot.send_photo(message.chat.id, photo=i)
        else:
            bot.send_message(message.chat.id, 'Изображение не найдено или оно платное( Помощь /help или поопробуй ввести данные заново /go')
        subject_help = 0

    if subject_help == 2:
        user_response = message.text
        predmet = 'russkii_yazik'
        main_url = asyncio.run(get_url(predmet, user_response, number_of_class))
        page = requests.get(main_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        image_tags = soup.find_all('img', src=True)
        much = 0
        images = []
        for tag in image_tags:
            if '/attachments/images/tasks/' in tag['src']:
                much += 1
                print('Найдено изображение:', f"https:{tag['src']}")
                images.append(f"https:{tag['src']}")
        if images:
            for i in images:
                print(i)
                bot.send_photo(message.chat.id, photo=i)
        else:
            bot.send_message(message.chat.id, 'Изображение не найдено или оно платное( Помощь /help или поопробуй ввести данные заново /go')
        subject_help = 0

    if subject_help == 3:
        user_response = message.text
        predmet = 'english'
        main_url = asyncio.run(get_url(predmet, user_response, number_of_class))
        page = requests.get(main_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        image_tags = soup.find_all('img', src=True)
        much = 0
        images = []
        for tag in image_tags:
            if '/attachments/images/tasks/' in tag['src']:
                much += 1
                print('Найдено изображение:', f"https:{tag['src']}")
                images.append(f"https:{tag['src']}")
        if images:
            for i in images:
                print(i)
                bot.send_photo(message.chat.id, photo=i)
        else:
            bot.send_message(message.chat.id, 'Изображение не найдено или оно платное( Помощь /help или поопробуй ввести данные заново /go')
        subject_help = 0

    if subject_help == 4:
        user_response = message.text
        predmet = 'biologiya'
        main_url = asyncio.run(get_url(predmet, user_response, number_of_class))
        page = requests.get(main_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        image_tags = soup.find_all('img', src=True)
        much = 0
        images = []
        for tag in image_tags:
            if '/attachments/images/tasks/' in tag['src']:
                much += 1
                print('Найдено изображение:', f"https:{tag['src']}")
                images.append(f"https:{tag['src']}")
        if images:
            for i in images:
                print(i)
                bot.send_photo(message.chat.id, photo=i)
        else:
            bot.send_message(message.chat.id, 'Изображение не найдено или оно платное( Помощь /help или поопробуй ввести данные заново /go')
        subject_help = 0

    if subject_help == 5:
        user_response = message.text.split()
        print(user_response)
        predmet = 'himiya'
        if number_of_class == '9':
            paragraph = user_response[1]
            type = user_response[2]
            main_url = asyncio.run(get_url(predmet, user_response[0], number_of_class, paragraph, type))
            page = requests.get(main_url)
            soup = BeautifulSoup(page.content, 'html.parser')

            image_tags = soup.find_all('img', src=True)
            much = 0
            images = []
            for tag in image_tags:
                if '/attachments/images/tasks/' in tag['src']:
                    much += 1
                    print('Найдено изображение:', f"https:{tag['src']}")
                    images.append(f"https:{tag['src']}")
            if images:
                for i in images:
                    print(i)
                    bot.send_photo(message.chat.id, photo=i)
            else:
                bot.send_message(message.chat.id,
                                 'Изображение не найдено или оно платное( Помощь /help или поопробуй ввести данные заново /go')

            subject_help = 0
        else:
            paragraph = 1
            type = 1
            main_url = asyncio.run(get_url(predmet, user_response[0], number_of_class, paragraph, type))
            page = requests.get(main_url)
            soup = BeautifulSoup(page.content, 'html.parser')

            image_tags = soup.find_all('img', src=True)
            much = 0
            images = []
            for tag in image_tags:
                if '/attachments/images/tasks/' in tag['src']:
                    much += 1
                    print('Найдено изображение:', f"https:{tag['src']}")
                    images.append(f"https:{tag['src']}")
            if images:
                for i in images:
                    print(i)
                    bot.send_photo(message.chat.id, photo=i)
            else:
                bot.send_message(message.chat.id, 'Изображение не найдено или оно платное( Помощь /help или поопробуй ввести данные заново /go')

            subject_help = 0

    if subject_help == 6:
        user_response = message.text.split()
        predmet = 'geometria'
        if len(user_response) == 2:
            chapter = user_response[1]
        else:
            chapter = 1
        bal = 1
        bal2 = 2
        main_url = asyncio.run(get_url(predmet, user_response[0], number_of_class, bal, bal2, chapter))
        page = requests.get(main_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        image_tags = soup.find_all('img', src=True)
        much = 0
        images = []
        for tag in image_tags:
            if '/attachments/images/tasks/' in tag['src']:
                much += 1
                print('Найдено изображение:', f"https:{tag['src']}")
                images.append(f"https:{tag['src']}")
        if images:
            for i in images:
                print(i)
                bot.send_photo(message.chat.id, photo=i)
        else:
            bot.send_message(message.chat.id, 'Изображение не найдено или оно платное( Помощь /help или поопробуй ввести данные заново /go')
        subject_help = 0

    if subject_help == 7:
        user_response = message.text.split()
        predmet = 'literatura'
        chapter = user_response[1]
        bal = 1
        bal2 = 2
        main_url = asyncio.run(get_url(predmet, user_response[0], number_of_class, bal, bal2, chapter))
        page = requests.get(main_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        image_tags = soup.find_all('img', src=True)
        much = 0
        images = []
        for tag in image_tags:
            if '/attachments/images/tasks/' in tag['src']:
                much += 1
                print('Найдено изображение:', f"https:{tag['src']}")
                images.append(f"https:{tag['src']}")
        if images:
            for i in images:
                print(i)
                bot.send_photo(message.chat.id, photo=i)
        else:
            bot.send_message(message.chat.id, 'Изображение не найдено или оно платное( Помощь /help или поопробуй ввести данные заново /go')
        subject_help = 0

    bot.send_message(message.chat.id, 'Сохранить фото?')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttonA = types.KeyboardButton('Да')
    buttonB = types.KeyboardButton('Нет')
    markup.row(buttonA, buttonB)
    bot.send_message(message.chat.id, '👇', reply_markup=markup)
    message.text = ''

@bot.message_handler(func=lambda message: message.text == 'Да')
def save(message):
    global save_helper
    save_helper = True
    bot.send_message(message.chat.id, 'Какое фото сохранить?')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    score = 0
    change1 = {
        '1': 'первое',
        '2': 'второе',
        '3': 'третье',
        '4': 'четвертое',
        '5': 'пятое',
        '6': 'шестое',
        '7': 'седьмое',
        '8': 'восьмое',
        '9': 'девятое',
        '10': 'десятое',
        '11': 'одиннадцатое',
        '12': 'двенадцатое',
        '13': 'тринадцатое',
        '14': 'четырнадцатое',
        '15': 'пятнадцатое',
        '16': 'шестнадцатое',
        '17': 'семнадцатое',
        '18': 'восемнадцатое',
        '19': 'девятнадцатое',
        '20': 'двадцатое',
        '21': 'двадцать первое',
        '22': 'двадцать второе',
        '23': 'двадцать третье',
        '24': 'двадцать четвертое',
        '25': 'двадцать пятое'
    }
    for i in images:
        score += 1
        for number, string in change1.items():
            if score == int(number):
                name = types.KeyboardButton(f"{string} фото")
        markup.row(name)
    bot.send_message(message.chat.id, '👇', reply_markup=markup)



@bot.message_handler(func=lambda message: message.text == 'Нет')
def save(message):
    global images
    global save_helper
    bot.send_message(message.chat.id, 'Окей. /go')
    images = []
    message.text = ''
    save_helper = False

@bot.message_handler(func=lambda message: save_helper == True)
def go_save_function(message):
    global images
    global save_helper
    change1 = {
        '1': 'первое',
        '2': 'второе',
        '3': 'третье',
        '4': 'четвертое',
        '5': 'пятое',
        '6': 'шестое',
        '7': 'седьмое',
        '8': 'восьмое',
        '9': 'девятое',
        '10': 'десятое',
        '11': 'одиннадцатое',
        '12': 'двенадцатое',
        '13': 'тринадцатое',
        '14': 'четырнадцатое',
        '15': 'пятнадцатое',
        '16': 'шестнадцатое',
        '17': 'семнадцатое',
        '18': 'восемнадцатое',
        '19': 'девятнадцатое',
        '20': 'двадцатое',
        '21': 'двадцать первое',
        '22': 'двадцать второе',
        '23': 'двадцать третье',
        '24': 'двадцать четвертое',
        '25': 'двадцать пятое'
    }
    for number, string in change1.items():
        if message.text.split()[0] == string:
            res = number
            print(message.text)
    check = asyncio.run(save_function_main(images, res))
    if check == True:
        bot.send_message(message.chat.id, 'Фото успешно сохранено!')
        bot.send_message(message.chat.id, '✔️ ')
    images = []
    message.text = ''
bot.polling(none_stop=True)

