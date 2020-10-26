import os
import telebot
from telebot import types
from flask import Flask, request

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

# This method will fire whenever the bot receives a message from a user,
@bot.message_handler(commands=['check'])
def check(message):
   text = (
   "<b>Please select your block! </b>\n"
   )

   markup = types.ReplyKeyboardMarkup(row_width=2)
   itembtn1 = types.KeyboardButton('A')
   itembtn2 = types.KeyboardButton('B')
   itembtn3 = types.KeyboardButton('C')
   itembtn4 = types.KeyboardButton('D')
   itembtn5 = types.KeyboardButton('F')
   markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
   bot.send_message(message.chat.id, text, parse_mode='HTML', reply_markup=markup)



@bot.message_handler(func=lambda msg: msg.text is not None)
def reply_to_message(message):
   sendMessage(message, 'Hello! Sorry idk what you are saying')


# SERVER SIDE 
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