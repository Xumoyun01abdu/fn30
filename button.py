from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def menyu():
    murkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton('Fantastic')
    btn2 = KeyboardButton('Komediya')
    btn3 = KeyboardButton('Dramma')
    btn4 = KeyboardButton('Triller')
    murkup.add(btn1, btn2, btn3, btn4)

    return murkup