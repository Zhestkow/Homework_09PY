import telebot, datetime


 
from telebot import types

bot = telebot.TeleBot("5952047176:AAGIe_D3pr3TYYiQ46SziG2G8iiA96jN_Q4")



num1 = 0
num2 = 0
sign=None

@bot.message_handler(commands=["start"])
def start(message):
    dtn = datetime.datetime.now()
    botlogfile = open('TestBot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    bot.send_message(message.chat.id, f"Вас приветствует Калькулятор")
    mrk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = telebot.types.KeyboardButton("Комплексные")
    key2= telebot.types.KeyboardButton("Действительные")
    mrk.add(key1)
    mrk.add(key2)
    bot.send_message(message.chat.id,"С какими числами будем работать?", reply_markup=mrk)
    bot.register_next_step_handler(message,choose_op)

def choose_op(message):
    dtn = datetime.datetime.now()
    botlogfile = open('TestBot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    bot.send_message(message.chat.id,"введи первое число", reply_markup=types.ReplyKeyboardRemove())
    if message.text == "Комплексные":
        bot.register_next_step_handler(message,compl)
    else:
        bot.register_next_step_handler(message,norm)
        
   
def compl(message):
    dtn = datetime.datetime.now()
    botlogfile = open('TestBot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global num1
    num1 = complex(message.text)
    bot.send_message(message.chat.id, f"введи второе число")
    bot.register_next_step_handler(message,action_compl)

def norm(message):
    dtn = datetime.datetime.now()
    botlogfile = open('TestBot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global num1
    num1 = int(message.text)
    bot.send_message(message.chat.id, f"введи второе число")
    bot.register_next_step_handler(message,action_norm)

def action_compl(message):
    dtn = datetime.datetime.now()
    botlogfile = open('TestBot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global num2
    num2 = complex(message.text)
    mrk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = telebot.types.KeyboardButton("+")
    key2 = telebot.types.KeyboardButton("-")
    key3 = telebot.types.KeyboardButton("*")
    key4 = telebot.types.KeyboardButton("/")
    key5 = telebot.types.KeyboardButton("/start")
    mrk.add(key1,key2,key3,key4,key5)
    bot.send_message(message.chat.id,"Выберите действие", reply_markup=mrk)
    bot.register_next_step_handler(message,choose_act)


def action_norm(message):
    dtn = datetime.datetime.now()
    botlogfile = open('TestBot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global num2
    num2 = int(message.text)
    mrk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = telebot.types.KeyboardButton("+")
    key2 = telebot.types.KeyboardButton("-")
    key3 = telebot.types.KeyboardButton("*")
    key4 = telebot.types.KeyboardButton("/")
    key5 = telebot.types.KeyboardButton("//")
    key6 = telebot.types.KeyboardButton("%")
    key7 = telebot.types.KeyboardButton("/start")
    mrk.add(key1,key2,key3,key4,key5,key6,key7)
    bot.send_message(message.chat.id,"Выберите действие", reply_markup=mrk)
    bot.register_next_step_handler(message,choose_act)

@bot.message_handler(content_types=["text"])
def choose_act(message):
    dtn = datetime.datetime.now()
    botlogfile = open('TestBot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M"), 'Пользователь ' + message.from_user.first_name, message.from_user.id, 'написал следующее: ' + message.text, file=botlogfile)
    botlogfile.close()
    global num2, num1, sign
    sign=message.text
    if message.text == "+":
        res = num1 + num2
    elif message.text == "-":
        res = num1-num2
    elif message.text == "*":
        res = num1*num2
    elif message.text == "/":
        res = num1/num2
    elif message.text == "//":
        res = num1//num2
    elif message.text == "%":
        res = num1%num2        
    bot.send_message(message.chat.id, f"\n {num1} {sign} {num2} = {res}\n\
                     \n\
Чтобы вернуться нажмите start\n")
    

bot.infinity_polling()