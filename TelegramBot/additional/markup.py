import telebot

import database_package

approved_values = ["0", "1", "2", "3", "+"]

def menu_markup():
    # TODO: вынесена кнопкка 'техника'
    massive_values = ["Получить тренировку","Отчитаться о тренировке","Диета"]
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for i in massive_values:
        button = telebot.types.KeyboardButton(text=i)
        keyboard.add(button)
    return keyboard


def supply_markup():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for i in approved_values:
        button = telebot.types.KeyboardButton(text=i)
        keyboard.add(button)
    button = telebot.types.KeyboardButton(text="Не выполнил заданное число")
    keyboard.add(button)
    button = telebot.types.KeyboardButton(text="Отмена")
    keyboard.add(button)
    return keyboard


def phone_number_markup():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = telebot.types.KeyboardButton(text="Send phone", request_contact=True)
    keyboard.add(button_phone)
    return keyboard


def cancel_markup():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = telebot.types.KeyboardButton(text="Отмена")
    keyboard.add(button_phone)
    return keyboard


def list_markup(number):
    cursor = database_package.database.Con()
    SelectAll = "SELECT execises FROM " + str("f") + number
    cursor.execute(SelectAll)
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    massive = []
    for row in cursor:
        if row[0] != "f":
            massive.append(row[0])
            button = telebot.types.KeyboardButton(text=row[0])
            keyboard.add(button)
    button = telebot.types.KeyboardButton(text="Отмена")
    keyboard.add(button)
    if len(massive) != 0:
       return keyboard
    else:
        return None