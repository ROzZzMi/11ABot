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

@bot.message_handler(commands=['leave'])
def leave(message):
    f'{user_list}'
    name = message.from_user.username
    user_list.remove('@' + name)
    bot.send_message(message.chat.id, 'Ти покинув(-ла) гру')

@bot.message_handler(commands=['list'])
def list(message):
        bot.send_message(message.chat.id, f'{user_list}')

@bot.message_handler(commands=['startgame1'])
def start1(message):
    bot.send_poll(message.chat.id, question=random.choice(qst_list), options=['+', '-'], is_anonymous=False)

@bot.message_handler(commands=['startgame2'])
def start2(message):
        f'{qst2_list}'
        n = 0
        q2 = qst2_list[n]
        bot.send_poll(message.chat.id, question=q2, options=(user_list), is_anonymous=False)
        del qst2_list[n]

@bot.message_handler(commands=['endgame'])
def leave(message):
        user_list.clear()
        bot.send_message(message.chat.id, "Гру закінчено!")

bot.polling(none_stop=True)