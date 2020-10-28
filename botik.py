import telebot
import random
from config import qst3_list, qst2_list, qst_list, TOKEN

bot = telebot.TeleBot(token=TOKEN)

user_list = []
i = 0

@bot.message_handler(commands=['join'])
def join(message):
        un = message.from_user.username
        name = message.from_user.first_name

        try:
            if '@' + un in user_list:
                bot.send_message(message.chat.id, 'Ти вже у грі!')
            else:
                user_list.append('@' + un)
                bot.send_message(message.chat.id, "Ти у грі!")
        except:
            if name in user_list:
                bot.send_message(message.chat.id, 'Ти вже у грі!')
            else:
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
    try:    
        m = 0
        q1 = qst_list[m]
        bot.send_poll(message.chat.id, question=q1, options=['+', '-'], is_anonymous=False)
        del qst_list[m]
    except:
        bot.send_message(message.chat.id, 'Питання закінчилися :(')


@bot.message_handler(commands=['startgame2'])
def start2(message):
    f'{qst2_list}'
    try:
        n = 0
        q2 = qst2_list[n]
        bot.send_poll(message.chat.id, question=q2, options=(user_list), is_anonymous=False)
        del qst2_list[n]
    except:
        bot.send_message(message.chat.id, 'Питання закінчилися :(') 


@bot.message_handler(commands=['startgame3'])
def start3(message):
    f'{qst3_list}'
    f'{user_list}'
    global i
    try:
        j = 0
        all = len(user_list)
        q3 = qst3_list[j]

        if i < all:
            pers = user_list[i] 
            bot.send_message(message.chat.id, 'Питання для ' + pers + ' (' + ranfom.choice(user_list) + ')\n' + q3)
            del qst3_list[j]
            i += 1
        else: 
            i = 0
            pers = user_list[i] 
            bot.send_message(message.chat.id, 'Питання для ' + pers + ' (' + ranfom.choice(user_list) + ')\n' + q3)
            del qst3_list[j]
    except:
        bot.send_message(message.chat.id, 'Питання закінчилися :(')

@bot.message_handler(commands=['endgame'])
def endgame(message):
        user_list.clear()
        bot.send_message(message.chat.id, "Гру закінчено!")

bot.polling(none_stop=True)
