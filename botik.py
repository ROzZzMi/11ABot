import telebot
import random
from config import qst2_list, qst_list, TOKEN

bot = telebot.TeleBot(token=TOKEN)

user_list = []

@bot.message_handler(commands=['join'])
def join(message):
        name = message.from_user.username
        user_list.append('@' + name)
        bot.send_message(message.chat.id, "Ти у грі!")

@bot.message_handler(commands=['list'])
def list(message):
        bot.send_message(message.chat.id, f'{user_list}')

@bot.message_handler(commands=['startgame1'])
def start1(message):
    bot.send_poll(message.chat.id, question=random.choice(qst_list), options=['+', '-'], is_anonymous=False)

@bot.message_handler(commands=['startgame2'])
def start2(message):
        bot.send_poll(message.chat.id, question=random.choice(qst2_list), options=(user_list), is_anonymous=False)

@bot.message_handler(commands=['endgame'])
def leave(message):
        user_list.clear()
        bot.send_message(message.chat.id, "Гру закінчено!")

bot.polling(none_stop=True)