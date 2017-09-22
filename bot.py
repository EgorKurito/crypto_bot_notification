import telegram
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import crypto

TOKEN = '308017424:AAEcnQMCPCaMP-s-YNVx298DFOPtR69DRFU'
updater = Updater(token = TOKEN)

def start(bot, update):
    message = update.message
    chat_id = message.chat_id

    bot.sendMessage(chat_id = chat_id, text = "Hello. Its test!")

def price_24(bot, update):
    message = update.message
    chat_id = message.chat_id
    text = message.text

    if text == "BTC":
        bot.sendMessage(chat_id = chat_id, text = crypro.BTCUSD)

def main():
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, price_24))

    updater.idle()
    updater.start_polling()

if __name__ == '__main__':
    main()
