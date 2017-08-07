import telegram
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '308017424:AAEcnQMCPCaMP-s-YNVx298DFOPtR69DRFU'
updater = Updater(token = TOKEN)

def start(bot, update):
    message = update.message
    chat_id = message.chat_id

    bot.sendMessage(chat_id = chat_id, text = "Hello. Its test!")

def main():
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.idle()
    updater.start_polling()

if __name__ == '__main__':
    main()
