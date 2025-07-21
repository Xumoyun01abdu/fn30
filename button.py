from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def menyu():
    murkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton('Fantastic')
    btn2 = KeyboardButton('Komediya')
    btn3 = KeyboardButton('Ramantika')
    btn4 = KeyboardButton('Criminal')
    murkup.add(btn1, btn2, btn3, btn4)

    return murkup