import telebot
import os
from dotenv import load_dotenv
from telebot import types

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

site = 'https://glavnyy-sayt-shkoly.com'
site_btn = 'Наш Сайт'

CLASSES = {
    'Класс 5': 'class_5',
    'Класс 6': 'class_6',
    'Класс 7': 'class_7',
    'Класс 8': 'class_8',
    'Класс 9': 'class_9',
    'Класс 10': 'class_10',
    'Класс 11': 'class_11',
}

SUBJECTS = {
    'class_5': {
        'Английский Язык (5)': 'https://example.com/ang5',
        'Биология (5)': 'https://example.com/bio5',
        'География (5)': 'https://example.com/geo5',
        'ИЗО (5)': 'https://example.com/izo5',
        'Информатика (5)': 'https://example.com/inf5',
        'История (5)': 'https://example.com/his5',
        'Литература (5)': 'https://example.com/lit5',
        'Математика (5)': 'https://example.com/math5',
        'Музыка (5)': 'https://example.com/muzyka5',
        'Немецкий язык (5)': 'https://example.com/nem5',
        'Русский язык (5)': 'https://example.com/rus5',
        'Технология (5)': 'https://example.com/tech5',
        'Узбекский язык (5)': 'https://example.com/uzb5',
        'Физкультура (5)': 'https://example.com/fiz5',
        'Французский язык (5)': 'https://example.com/fran5',
    },
    'class_6': {
        'Английский Язык (6)': 'https://example.com/ang6',
        'Биология (6)': 'https://example.com/bio6',
        'География (6)': 'https://example.com/geo6',
        'ИЗО (6)': 'https://example.com/izo6',
        'Информатика (6)': 'https://example.com/inf6',
        'История (6)': 'https://example.com/his6',
        'Литература (6)': 'https://example.com/lit6',
        'Математика (6)': 'https://example.com/math6',
        'Музыка (6)': 'https://example.com/muzyka6',
        'Немецкий язык (6)': 'https://example.com/nem6',
        'Русский язык (6)': 'https://example.com/rus6',
        'Технология (6)': 'https://example.com/tech6',
        'Узбекский язык (6)': 'https://example.com/uzb6',
        'Физкультура (6)': 'https://example.com/fiz6',
        'Французский язык (6)': 'https://example.com/fran6',
    },
    'class_7': {
        'Английский Язык (7)': 'https://example.com/ang7',
        'Биология (7)': 'https://example.com/bio7',
        'География (7)': 'https://example.com/geo7',
        'ИЗО (7)': 'https://example.com/izo7',
        'Информатика (7)': 'https://example.com/inf7',
        'История (7)': 'https://example.com/his7',
        'Литература (7)': 'https://example.com/lit7',
        'Алгебра (7)': 'https://example.com/alg7',
        'Геометрия (7)': 'https://example.com/geom7',
        'Физика (7)': 'https://example.com/fizika7',
        'Музыка (7)': 'https://example.com/muzyka7',
        'Немецкий язык (7)': 'https://example.com/nem7',
        'Русский язык (7)': 'https://example.com/rus7',
        'Технология (7)': 'https://example.com/tech7',
        'Узбекский язык (7)': 'https://example.com/uzb7',
        'Физкультура (7)': 'https://example.com/fiz7',
        'Французский язык (7)': 'https://example.com/fran7',
        'Химия (7)': 'https://example.com/ximia7',
    },
    'class_8': {
        'Алгебра (8)': 'https://example.com/alg8',
        'Английский язык (8)': 'https://example.com/ang8',
        'Биология (8)': 'https://example.com/bio8',
        'Воспитание (8)': 'https://example.com/vosp8',
        'Всемирная история (8)': 'https://example.com/vsemir8',
        'География (8)': 'https://example.com/geo8',
        'Геометрия (8)': 'https://example.com/geom8',
        'Информатика (8)': 'https://example.com/inf8',
        'История Узбекистана (8)': 'https://example.com/uzbhis8',
        'Литература (8)': 'https://example.com/lit8',
        'Немецкий язык (8)': 'https://example.com/nem8',
        'ОГП (8)': 'https://example.com/ogp8',
        'Русский язык (8)': 'https://example.com/rus8',
        'Технология (8)': 'https://example.com/tech8',
        'Узбекский язык (8)': 'https://example.com/uzb8',
        'Физика (8)': 'https://example.com/fizika8',
        'Физкультура (8)': 'https://example.com/fizkultura8',
        'Французский язык (8)': 'https://example.com/fran8',
        'Химия (8)': 'https://example.com/ximia8',
        'Черчение (8)': 'https://example.com/cherch8',
        'Экономика (8)': 'https://example.com/econ8'
    },
    'class_9': {
        'Алгебра (9)': 'https://example.com/alg9',
        'Английский язык (9)': 'https://example.com/ang9',
        'Биология (9)': 'https://example.com/bio9',
        'Воспитание (9)': 'https://example.com/vosp9',
        'Всемирная история (9)': 'https://example.com/vsemir9',
        'География (9)': 'https://example.com/geo9',
        'Геометрия (9)': 'https://example.com/geom9',
        'Информатика (9)': 'https://example.com/inf9',
        'История Узбекистана (9)': 'https://example.com/uzbhis9',
        'Литература (9)': 'https://example.com/lit9',
        'Немецкий язык (9)': 'https://example.com/nem9',
        'ОГП (9)': 'https://example.com/ogp9',
        'Основы конституционного права (9)': 'https://example.com/konst9',
        'Русский язык (9)': 'https://example.com/rus9',
        'Технология (9)': 'https://example.com/tech9',
        'Узбекский язык (9)': 'https://example.com/uzb9',
        'Физика (9)': 'https://example.com/fizika9',
        'Физкультура (9)': 'https://example.com/fizkultura9',
        'Французский язык (9)': 'https://example.com/fran9',
        'Химия (9)': 'https://example.com/ximia9',
        'Черчение (9)': 'https://example.com/cherch9',
        'Экономика (9)': 'https://example.com/econ9'
    },
    'class_10': {
        'Алгебра (10)': 'https://example.com/alg10',
        'Английский язык (10)': 'https://example.com/ang10',
        'Биология (10)': 'https://example.com/bio10',
        'Воспитание (10)': 'https://example.com/vosp10',
        'Всемирная история (10)': 'https://example.com/vsemir10',
        'География (10)': 'https://example.com/geo10',
        'Геометрия (10)': 'https://example.com/geom10',
        'Информатика (10)': 'https://example.com/inf10',
        'История Узбекистана (10)': 'https://example.com/uzbhis10',
        'Литература (10)': 'https://example.com/lit10',
        'НДП (10)': 'https://example.com/ndp10',
        'Немецкий язык (10)': 'https://example.com/nem10',
        'ОГП (10)': 'https://example.com/ogp10',
        'Русский язык (10)': 'https://example.com/rus10',
        'Узбекский язык (10)': 'https://example.com/uzb10',
        'Физика (10)': 'https://example.com/fizika10',
        'Физкультура (10)': 'https://example.com/fizkultura10',
        'Французский язык (10)': 'https://example.com/fran10',
        'Химия (10)': 'https://example.com/ximia10'
    },
    'class_11': {
        'Алгебра (11)': 'https://example.com/alg11',
        'Английский язык (11)': 'https://example.com/ang11',
        'Астрономия (11)': 'https://example.com/ast11',
        'Биология (11)': 'https://example.com/bio11',
        'Воспитание (11)': 'https://example.com/vosp11',
        'Всемирная история (11)': 'https://example.com/vsemir11',
        'Геометрия (11)': 'https://example.com/geom11',
        'Информатика (11)': 'https://example.com/inf11',
        'История Узбекистана (11)': 'https://example.com/uzbhis11',
        'Литература (11)': 'https://example.com/lit11',
        'НДП (11)': 'https://example.com/ndp11',
        'Немецкий язык (11)': 'https://example.com/nem11',
        'Предпринимательство (11)': 'https://example.com/predpr11',
        'Русский язык (11)': 'https://example.com/rus11',
        'Узбекский язык (11)': 'https://example.com/uzb11',
        'Физика (11)': 'https://example.com/fizika11',
        'Физкультура (11)': 'https://example.com/fizkultura11',
        'Французский язык (11)': 'https://example.com/fran11',
        'Химия (11)': 'https://example.com/ximia11'
    },
}

classes_name = {name: key for name, key in CLASSES.items()}


def create_classes_reply_keyboard():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=False)

    buttons = [types.KeyboardButton(text=name) for name in CLASSES.keys()]

    for i in range(0, len(buttons), 2):
        if i + 1 < len(buttons):
            markup.row(buttons[i], buttons[i + 1])
        else:
            markup.add(buttons[i])

    markup.add(types.KeyboardButton(text=site_btn))

    return markup


def create_subjects_keyboard(class_key):
    markup = types.InlineKeyboardMarkup()
    subjects_dict = SUBJECTS.get(class_key, {})

    markup.add(types.InlineKeyboardButton(text="Наш Главный Сайт", url=site))

    buttons = [types.InlineKeyboardButton(text=name, url=url) for name, url in subjects_dict.items()]

    for i in range(0, len(buttons), 2):
        if i + 1 < len(buttons):
            markup.row(buttons[i], buttons[i + 1])
        else:
            markup.add(buttons[i])

    markup.add(types.InlineKeyboardButton(text="Сменить класс", callback_data='show_classes'))
    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
    classes_reply_markup = create_classes_reply_keyboard()

    welcome_text = f" Приветствуем, {message.from_user.first_name}! \n\n Выберите свой класс или перейдите на сайт с помощью кнопок ниже:"

    bot.send_message(
        message.chat.id,
        welcome_text,
        reply_markup=classes_reply_markup,
        parse_mode='Markdown'
    )


@bot.callback_query_handler(func=lambda call: call.data == 'ignore')
def ignore_callback(call):
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == 'show_classes')
def callback_show_classes(call):
    bot.answer_callback_query(call.id)
    classes_reply_markup = create_classes_reply_keyboard()
    menu_text = "Выберите свой класс:"

    try:
        bot.edit_message_text(menu_text, call.message.chat.id, call.message.message_id, parse_mode='Markdown')
    except telebot.apihelper.ApiTelegramException as e:
        if "message is not modified" in str(e):
            pass
        else:
             bot.send_message(call.message.chat.id, menu_text, parse_mode='Markdown')

    bot.send_message(call.message.chat.id, "⬇️ Клавиатура обновлена ⬇", reply_markup=classes_reply_markup)


@bot.message_handler(func=lambda message: message.text == site_btn)
def handle_website_selection(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="➡️ Перейти на Главный Сайт", url=site))

    bot.send_message(
        message.chat.id,
        "Нажмите кнопку ниже, чтобы перейти на сайт:",
        reply_markup=markup
    )


@bot.message_handler(func=lambda message: message.text in classes_name)
def handle_class_selection(message):
    class_name = message.text
    class_key = classes_name[class_name]
    subjects_markup = create_subjects_keyboard(class_key)

    menu_text = f"Выбран {class_name}. Теперь выберите предмет."

    bot.send_message(
        message.chat.id,
        menu_text,
        reply_markup=subjects_markup,
        parse_mode='Markdown'
    )


@bot.message_handler(content_types=['text'])
def handle_other_text(message):
    bot.send_message(message.chat.id, "Извините, я понимаю только команды /start или выбор класса/сайта из меню.")


if __name__ == '__main__':
    print("Бот запущен. Ожидание команды /start.")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
