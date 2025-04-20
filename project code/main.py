import telebot
from telebot import types

bot_token = ''
bot = telebot.TeleBot(bot_token)

dorm_info = {
    'Общежитие №1': {
        'address': '1127018, г. Москва, 2-й Вышеславцев пер, д. 17',
        'places': 528,
        'map_link': 'https://yandex.ru/maps/-/CBFKm-HolC'
    },
    'Общежитие №2': {
        'address': '127055, г. Москва, ул Образцова, д. 22 ',
        'places': 885,
        'map_link': 'https://yandex.ru/maps/-/CBB0QCDoLC'
    },
    'Комплекс общежитий №3': {
        'address': '129323, г. Москва, ул. Снежная, д. 16, к. 3, к. 4, к. 5',
        'places': '757 (корпус 3) + 755 (корпус 4)',
        'map_link': 'https://yandex.ru/maps/-/CGXRmK3d'
    },
    'Общежитие №4': {
        'address': '127322, г. Москва, Огородный проезд, д. 25/20',
        'places': 859,
        'map_link': 'https://yandex.ru/maps/-/CBFKqRglGD'
    },
    'Общежитие №5': {
        'address': '129301, г. Москва, ул Космонавтов, д. 11',
        'places': 931,
        'map_link': 'https://yandex.ru/maps/-/CBFKq6eMSB'
    },
    'Общежитие №8': {
        'address': '129347, г. Москва, ул Палехская, д. 145',
        'places': 76,
        'map_link': 'https://yandex.ru/maps/-/CBFKqOURlB'
    },
    'Общежитие "Кратово"': {
        'address': '140130, Московская область, Раменский район, пос. Кратово, ул. Симбирская, д. 13',
        'places': 0,
        'map_link': 'https://yandex.ru/maps/-/CCvfUGOx'
    },
    'Общежитие "Люблино"': {
        'address': '109382, г. Москва, ул Люблинская, д. 88, стр. 4',
        'places': 146,
        'map_link': 'https://yandex.ru/maps/-/CGuh7NiF'
    },
    'Общежитие Российской открытой академии транспорта': {
        'address': '125315, г. Москва, 3-й Балтийский пер, д. 4, к. 5',
        'places': 418,
        'map_link': 'https://yandex.ru/maps/-/CGuh7H~-'
    },
    'Общежитие Российской академии путей сообщения': {
        'address': '127018, г. Москва, Октябрьский пер, д. 7',
        'places': 161,
        'map_link': 'https://yandex.ru/maps/-/CGulAR05'
    },
    'Общежитие "Дмитровское"': {
        'address': '127015, г. Москва, ул. Бутырская, д. 79, подъезд 2',
        'places': 135,
        'map_link': 'https://yandex.ru/maps/-/CCU47OQN~C'
    },
    'Общежитие "Судостроительное"': {
        'address': '115407, г. Москва, ул. Судостроительная, д. 32, корпус 2',
        'places': 232,
        'map_link': 'https://yandex.ru/maps/-/CCUaMJHpwC'
    },
    'Общежитие "Южнопортовое"': {
        'address': '115432, г. Москва, ул. 2-й Южнопортовый проезд, д. 5, корпус 2',
        'places': 211,
        'map_link': 'https://yandex.ru/maps/-/CCUaqKH7lB'
    }
}


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет, это бот для начального знакомства с нашим любимым вузом РУТ МИИТ! Выбери пункт, '
                          'который тебе интересен!')
    show_main_menu(message)


def show_main_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton('Общежития')
    button2 = types.KeyboardButton('Факультеты')
    button3 = types.KeyboardButton('Кафедры')
    button4 = types.KeyboardButton('Инфраструктура вуза')
    button5 = types.KeyboardButton('План вуза')

    markup.add(button1, button2, button3, button4, button5)
    bot.send_message(message.chat.id, "Выберите кнопку:", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == 'Общежития':
        show_dormitory_menu(message)

    elif message.text in dorm_info:
        dorm = dorm_info[message.text]
        response = (
            f"Адрес: {dorm['address']}\n"
            f"Количество мест: {dorm['places']}\n"
            f"Ссылка на местоположение на карте: {dorm['map_link']}"
        )
        bot.send_message(message.chat.id, response)

        show_dormitory_menu(message)

    elif message.text == 'Инфраструктура вуза':
        bot.send_photo(message.chat.id, 'https://static.tildacdn.com/tild3730-3336-4666-b836-313963653961/karta.png')

    elif message.text == 'План вуза':
        bot.send_photo(message.chat.id, 'https://yandex.ru/images/search?pos=15&from=tabbar&img_url=https%3A%2F%2Fsun9-37.userapi.com%2Fimpf%2Fle2KUHf4mlgxZt_5cua669NS9DNkxIisWf-AKg%2FI6XWN3pPGAY.jpg%3Fsize%3D873x873%26quality%3D96%26sign%3D2cabc4e9a557d2ad407f3b4db28793b0%26c_uniq_tag%3Df_u59uIJYjxaZvLcnBPJKV7vPRbQsOf8rJPd12LuDKI%26type%3Dalbum&text=%D0%BF%D0%BB%D0%B0%D0%BD+%D0%B2%D1%83%D0%B7%D0%B0+%D1%80%D1%83%D1%82+%D0%BC%D0%B8%D0%B8%D1%82&rpt=simage&lr=213')

    elif message.text == 'Кафедры':
        show_cafedra_menu(message)

    elif message.text == 'Назад':
        show_main_menu(message)


def show_dormitory_menu(message):
    markup1 = types.ReplyKeyboardMarkup(row_width=2)
    buttons = [types.KeyboardButton(dorm_name) for dorm_name in dorm_info.keys()]
    back_button = types.KeyboardButton('Назад')
    markup1.add(*buttons)
    markup1.add(back_button)
    bot.send_message(message.chat.id, "Выберите общежитие или нажмите кнопку 'Назад':", reply_markup=markup1)


def show_cafedra_menu(message):
    markup1 = types.ReplyKeyboardMarkup(row_width=2)
    buttons = ['Кафедра ЦТУТП', 'Кафедра ВССиИБ', 'Кафедра ЖДСТУ', 'Кафедра ЛиУТС', 'Кафедра ЛТСТ', 'Кафедра УТБиИС',
               'Кафедра УЭРиБТ', 'Кафедра ХиИЭ']
    back_button = types.KeyboardButton('Назад')
    markup1.add(*buttons)
    markup1.add(back_button)
    bot.send_message(message.chat.id, "Выберите кафедру или нажмите кнопку 'Назад':", reply_markup=markup1)


bot.polling(none_stop=True)
