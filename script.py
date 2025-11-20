import telebot
import os
from dotenv import load_dotenv
from telebot import types

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

site = 'https://answer-bot-website.vercel.app/'
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
        'Наука ✅ (5)': 'https://answer-bot-website.vercel.app/%D0%BD%D0%B0%D1%83%D0%BA%D0%B05.html',
        'Английский Язык (5)': 'https://answer-bot-website.vercel.app/sor.html',
        'Биология (5)': 'https://answer-bot-website.vercel.app/sor.html',
        'География (5)': 'https://answer-bot-website.vercel.app/sor.html',
        'ИЗО (5)': 'https://answer-bot-website.vercel.app/sor.html',
        'Информатика (5)': 'https://answer-bot-website.vercel.app/sor.html',
        'История (5)': 'https://answer-bot-website.vercel.app/sor.html',
        'Литература (5)': 'https://answer-bot-website.vercel.app/sor.html',
        'Математика (5)': 'https://answer-bot-website.vercel.app/sor.html',
        'Музыка (5)': 'https://answer-bot-website.vercel.app/sor.html',
        'Немецкий язык (5)': 'https://answer-bot-website.vercel.app/sor.html',
        'Русский язык (5)': 'https://answer-bot-website.vercel.app/sor.html',
        'Технология (5)': 'https://answer-bot-website.vercel.app/sor.html',
        'Узбекский язык (5)': 'https://answer-bot-website.vercel.app/sor.html',
        'Физкультура (5)': 'https://answer-bot-website.vercel.app/sor.html',
        'Французский язык (5)': 'https://answer-bot-website.vercel.app/sor.html',

    },
    'class_6': {
        'Наука ✅ (6)': 'https://answer-bot-website.vercel.app/%D0%BD%D0%B0%D1%83%D0%BA%D0%B06.html',
        'Английский Язык (6)': 'https://answer-bot-website.vercel.app/sor.html',
        'Биология (6)': 'https://answer-bot-website.vercel.app/sor.html',
        'География (6)': 'https://answer-bot-website.vercel.app/sor.html',
        'ИЗО (6)': 'https://answer-bot-website.vercel.app/sor.html',
        'Информатика (6)': 'https://answer-bot-website.vercel.app/sor.html',
        'История (6)': 'https://answer-bot-website.vercel.app/sor.html',
        'Литература (6)': 'https://answer-bot-website.vercel.app/sor.html',
        'Математика (6)': 'https://answer-bot-website.vercel.app/sor.html',
        'Музыка (6)': 'https://answer-bot-website.vercel.app/sor.html',
        'Немецкий язык (6)': 'https://answer-bot-website.vercel.app/sor.html',
        'Русский язык (6)': 'https://answer-bot-website.vercel.app/sor.html',
        'Технология (6)': 'https://answer-bot-website.vercel.app/sor.html',
        'Узбекский язык (6)': 'https://answer-bot-website.vercel.app/sor.html',
        'Физкультура (6)': 'https://answer-bot-website.vercel.app/sor.html',
        'Французский язык (6)': 'https://answer-bot-website.vercel.app/sor.html',
    },
    'class_7': {
        'Алгебра ✅ (7)': 'https://answer-bot-website.vercel.app/%D0%BD%D0%B0%D1%83%D0%BA%D0%B06.html',
        'Английский Язык (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'Биология (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'География (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'ИЗО (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'Информатика (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'История (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'Литература (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'Геометрия (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'Физика (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'Музыка (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'Немецкий язык (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'Русский язык (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'Технология (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'Узбекский язык (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'Физкультура (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'Французский язык (7)': 'https://answer-bot-website.vercel.app/sor.html',
        'Химия (7)': 'https://answer-bot-website.vercel.app/sor.html',
    },
    'class_8': {
        'Алгебра ✅ (8)': 'https://answer-bot-website.vercel.app/algebra8.html',
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
        'Алгебра ✅ (9)': 'https://answer-bot-website.vercel.app/algebra9.html',
        'Английский язык (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Биология (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Воспитание (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Всемирная история (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'География (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Геометрия (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Информатика (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'История Узбекистана (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Литература (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Немецкий язык (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'ОГП (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Русский язык (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Технология (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Узбекский язык (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Физика (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Физкультура (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Французский язык (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Химия (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Черчение (8)': 'https://answer-bot-website.vercel.app/sor.html',
        'Экономика (8)': 'https://answer-bot-website.vercel.app/sor.html',
    },
    'class_10': {
        'Алгебра ✅ (10)': 'https://answer-bot-website.vercel.app/algebra10.html',
        'Английский язык (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'Биология (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'Воспитание (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'Всемирная история (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'География (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'Геометрия (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'Информатика (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'История Узбекистана (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'Литература (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'НДП (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'Немецкий язык (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'ОГП (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'Русский язык (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'Узбекский язык (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'Физика (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'Физкультура (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'Французский язык (10)': 'https://answer-bot-website.vercel.app/sor.html',
        'Химия (10)': 'https://answer-bot-website.vercel.app/sor.html'
    },
    'class_11': {
        'Алгебра ✅ (11)': 'https://answer-bot-website.vercel.app/algebra11.html',
        'Английский язык (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'Астрономия (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'Биология (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'Воспитание (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'Всемирная история (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'Геометрия (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'Информатика (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'История Узбекистана (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'Литература (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'НДП (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'Немецкий язык (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'Предпринимательство (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'Русский язык (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'Узбекский язык (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'Физика (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'Физкультура (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'Французский язык (11)': 'https://answer-bot-website.vercel.app/sor.html',
        'Химия (11)': 'https://answer-bot-website.vercel.app/sor.html'
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
