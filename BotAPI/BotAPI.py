import telebot
import time
from telebot import types
from random import randint
from array import *

bot = telebot.TeleBot('your_token')

fn = randint(11,99)
sn = randint(11,99)
answer = fn + sn

next = False

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Старт')
    bot.send_message(message.chat.id, "Начнем!", reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    global next
    if message.text == "Старт": start_answer(message)
    if message.text == "1": 
        msg = bot.send_message(message.chat.id, "loading...")
        bot.edit_message_text("result", chat_id=message.chat.id, message_id=msg.message_id)

def start_answer(message):
    count = 3
    time_count = 3

    for i in range(count):
        a = start_message(message, i, count)

        msg = bot.send_message(message.chat.id, "Осталось: " + str(time_count) + " с")
        for t in range(time_count):
            time.sleep(1)
            bot.edit_message_text("Осталось: " + str(time_count - 1 - t) + " с", chat_id=message.chat.id, message_id=msg.message_id)

        bot.delete_message(a.chat.id, a.message_id)
        
def start_message(message, count, max_count):
        global fn
        global sn
        global answer
        
        fn = randint(11,99)
        sn = randint(11,99)
        answer = fn + sn
        number = randint(0,3)
        buttons = array('i', [])

        for i in range(4):
            buttons.append(randint(fn, 200))

        buttons[number] = answer
        
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text=str(buttons[0]), callback_data=buttons[0]))
        markup.add(telebot.types.InlineKeyboardButton(text=str(buttons[1]), callback_data=buttons[1]))
        markup.add(telebot.types.InlineKeyboardButton(text=str(buttons[2]), callback_data=buttons[2]))
        markup.add(telebot.types.InlineKeyboardButton(text=str(buttons[3]), callback_data=buttons[3]))
        return bot.send_message(message.chat.id, text=str(fn) + ' + ' + str(sn) + " ( " + str(count) + " из " + str(max_count) + ")", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id)
    ans = ''
    bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == str(answer):
        ans = 'Верно! '
    else: ans = 'Неа'

    bot.send_message(call.message.chat.id, ans)

bot.polling(none_stop=True, interval=0)