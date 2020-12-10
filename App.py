import os
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request
from sheets import findAvilbility
from AnswerGen import generateAnswer

TOKEN = '1344716453:AAH9b9tDUgGsP49GleNo0rnWDZn_bgr0qRo'
bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)


# Bot's Functionalities
def sendMessage(message, text):
   bot.send_message(message.chat.id, text)
# This method will send a message formatted in HTML to the user whenever it starts the bot with the /start command, feel free to add as many commands' handlers as you want


@bot.message_handler(commands=['start'])
def send_info(message):
   text = (
   "<b>Welcome to the Eusoff laundary bot 🤖!</b>\n"
   "/check - check the avilbility of washing machine in your block"
   )
   bot.send_message(message.chat.id, text, parse_mode='HTML')





# This method will fire whenever the bot receives /check
@bot.message_handler(commands=['check'])
def check(message):
   text = (
   "<b>Please select your block! </b>\n"
   )

   bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=gen_markup())


# This method is to create the inline keyboard of all the block
def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("A", callback_data="A"),
                               InlineKeyboardButton("B", callback_data="B"),
                               InlineKeyboardButton("C", callback_data="C"),
                               InlineKeyboardButton("D", callback_data="D"),
                               InlineKeyboardButton("E", callback_data="E"))
    return markup



#this method is to handle when the block keyborad is selscted 
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    blockarr = findAvilbility()
    if call.data == "A":
        bot.answer_callback_query(call.id, "A")
        ans = generateAnswer(blockarr, "A")
        sendMessage(call.message, ans)
    elif call.data == "B":
        bot.answer_callback_query(call.id, "B")
        ans = generateAnswer(blockarr, "B")
        sendMessage(call.message, ans)
    elif call.data == "C":
        bot.answer_callback_query(call.id, "C")
        ans = generateAnswer(blockarr, "C")
        sendMessage(call.message, ans)
    elif call.data == "D":
        bot.answer_callback_query(call.id, "D")
        ans = generateAnswer(blockarr, "D")
        sendMessage(call.message, ans)
    elif call.data == "E":
        ans = generateAnswer(blockarr, "E")
        sendMessage(call.message, ans)



#this method is when user input somthing else 
@bot.message_handler(func=lambda msg: msg.text is not None)
def reply_to_message(message):
   sendMessage(message, 'Sorry idk what you are saying!')



# SERVER SIDE -------------------------------------------------------------------------------------------------------------
@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
   bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
   return "!", 200


@server.route("/")
def webhook():
   bot.remove_webhook()
   bot.set_webhook(url='https://laundarybottest.herokuapp.com/' + TOKEN)
   return "!", 200


if __name__ == "__main__":
   server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))