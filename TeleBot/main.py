import telebot
import sqlite3
import csv

bot = telebot.Telebot("6384674184:AAERz9OSmqyXMUYGzQD5TAfLEjKu08VxZc0")


@bot.message_handler(commands="start")
def startfunc():
    bot.send_message("asdasdas")




bot.polling(none_stop=True)


with open("store.csv", "r") as f:
    content = csv.reader(f)
    for item in content:
        print(item)