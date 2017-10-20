# Import libraries and packages
import config, main, bitfinex
import telegram

from telegram import * #Update, ForceReply, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import * #Updater, CommandHandler, MessageHandler, Filters

# Main bot function
button_list = [[InlineKeyboardButton("BTC/USD", callback_data='btcusd')],
                [InlineKeyboardButton("ETH/USD", callback_data='ethusd'),
                InlineKeyboardButton("ETP/USD", callback_data='etpeth'),
                InlineKeyboardButton("XMR/USD", callback_data='xmrusd')],
                [InlineKeyboardButton("MENU", callback_data='menu')]]
button_markup = InlineKeyboardMarkup(button_list)


menu_list = [[InlineKeyboardButton("HELP", callback_data='help'),
             InlineKeyboardButton("BACK", callback_data='back'),]]
menu_markup = InlineKeyboardMarkup(menu_list)
# Required start function
def start(bot, update):
    message = update.message
    chat_id = message.chat_id

    bot.send_message(chat_id = chat_id, text = "Hello", reply_markup=button_markup)



def callback(bot, update):
    call = update.callback_query
    message = call.message
    chat_id = message.chat_id

    if call.data == 'menu':
        bot.edit_message_text(chat_id = chat_id, message_id=message.message_id, text = 'MENU', reply_markup=menu_markup)
    elif call.data == 'back':
        bot.edit_message_text(chat_id = chat_id, message_id=message.message_id, text = 'PRICE - ___', reply_markup=button_markup)
    else:
        x = bitfinex.BitFinex(call.data)
        mid = x.mid()
        bot.edit_message_text(chat_id = chat_id, message_id=message.message_id, text = 'PRICE - '+mid, reply_markup=button_markup)
def crypto(bot, update):
    message = update.message
    chat_id = message.chat_id
    text = message.text



    x = bitfinex.BitFinex(text)
    mid = x.mid()
    bot.send_message(chat_id = chat_id, text = mid , reply_markup = crypto_markup)
