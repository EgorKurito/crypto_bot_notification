# Import libraries and packages
import config, bot
import telegram, logging


from telegram import Update, CallbackQuery
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

# Main variable
updater = Updater(token=config.BOT_TOKEN)

# Bot authentication
root = logging.getLogger()
root.setLevel(logging.INFO)

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  level = logging.INFO)

logger = logging.getLogger(__name__)

# Main function
def main():
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", bot.start))
    dp.add_handler(MessageHandler(Filters.text, bot.crypto))
    dp.add_handler(CallbackQueryHandler(callback = bot.callback))

    updater.start_polling()

if __name__ == '__main__':
    main()
