import telebot
from telebot import types
from telebot import callback_data



bot = telebot.TeleBot("6593111407:AAEvjoFqPPoB8hr9soMECCJCgjqt4MiuQlk")

@bot.message_handler(commands=["start"])
def start_func(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton("⚽️Balls")
    button_2 = types.KeyboardButton("🧤Gloves")
    button_3 = types.KeyboardButton("👞Boots")
    button_4 = types.KeyboardButton("🚲Bikes")
    markup.add(button_1, button_2, button_3, button_4)
    bot.send_message(message.chat.id, "Hello welcome to our sport shop", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def func_(message):
    if message.text == "⚽️Balls":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.InlineKeyboardButton("⚽️Joma")
        button_2 = types.InlineKeyboardButton("⚽️Adidas")
        button_3 = types.InlineKeyboardButton("⚽️Nike")
        button_4 = types.InlineKeyboardButton("⬅️Back", callback_data="button_4")
        markup.add(button_1, button_2, button_3, button_4)
        bot.send_message(message.chat.id, 'This are brands our of balls ', reply_markup=markup)

# @bot.callback_query_handlers(func=lambda call: True)
#
#     elif (message.text == "⚽️Joma"):
#         Photo = open('jomaball.jpg', 'rb')
#         bot.send_photo(message.chat.id, Photo)
#         bot.send_message(message.chat.id, text='Я работаю')
        # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # button = types.KeyboardButton("buy now")
        # markup.add(button)
        # bot.send_message(message.chat.id, "", reply_markup=markup)
        # Photo.close()


    elif (message.text == "🧤Gloves"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton("🧤Puma")
        button_2 = types.KeyboardButton("🧤Adidas")
        button_3 = types.KeyboardButton("🧤Nike")
        button_4 = types.InlineKeyboardButton("⬅️Back", callback_data="button_3")
        markup.add(button_1, button_2, button_3)
        bot.send_message(message.chat.id, "This are brands our of gloves ", reply_markup=markup)



    elif (message.text == "👞Boots"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton("👞Adidas")
        button_2 = types.KeyboardButton("👞Nike")
        button_3 = types.InlineKeyboardButton("⬅️Back", callback_data="button_2")
        markup.add(button_1, button_2)
        bot.send_message(message.chat.id, "This are brands our of boots ", reply_markup=markup)


    elif (message.text == "🚲Bikes"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton("🚲Trek")
        button_2 = types.InlineKeyboardButton("⬅️Back", callback_data="button_1")
        markup.add(button_1, button_2)
        # bot.send_message(message.chat.id, "This are brands our of bikes ", reply_markup=markup)

# @bot.callback_query_handler(func=lambda call: True)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "⬅️Back":
        # bot.answer_callback_query(call.id, "Answer is Yes")
      start_func()
bot.polling(none_stop=True)