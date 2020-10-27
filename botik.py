import telebot
import random
from config import qst2_list, qst_list, TOKEN

bot = telebot.TeleBot(token=TOKEN)

user_list = []

@bot.message_handler(commands=['join'])
def join(message):
        un = message.from_user.username
        name = message.from_user.first_name

        try:
            user_list.append('@' + un)
            bot.send_message(message.chat.id, "Ти у грі!")
        except:
            user_list.append(name)
            bot.send_message(message.chat.id, "Ти у грі!")

@bot.message_handler(commands=['leave'])
def leave(message):
    f'{user_list}'
    un = message.from_user.username
    name = message.from_user.first_name
    
    try:
        try:
            user_list.remove('@' + un)
            bot.send_message(message.chat.id, 'Ти покинув(-ла) гру')
        except:
            user_list.remove(name)
            bot.send_message(message.chat.id, 'Ти покинув(-ла) гру')
    except:
        bot.send_message(message.chat.id, 'Ти вже покинув(-ла) гру')

@bot.message_handler(commands=['list'])
def list(message):
        bot.send_message(message.chat.id, f'{user_list}')

@bot.message_handler(commands=['startgame1'])
def start1(message):
    f'{qst_list}'
    m = 0
    q1 = qst_list[m]
    bot.send_poll(message.chat.id, question=q1, options=['+', '-'], is_anonymous=False)
    del qst_list[m]

@bot.message_handler(commands=['startgame2'])
def start2(message):
    try:
        f'{qst2_list}'
        n = 0
        q2 = qst2_list[n]
        bot.send_poll(message.chat.id, question=q2, options=(user_list), is_anonymous=False)
        del qst2_list[n]
    except:
        bot.send_message(message.chat.id, 'Питання закінчилися :(') 

@bot.message_handler(commands=['endgame'])
def endgame(message):
        user_list.clear()
        bot.send_message(message.chat.id, "Гру закінчено!")

bot.polling(none_stop=True)
