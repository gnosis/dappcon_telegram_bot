
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from bot_commands import start, help, echo, right_now, next, side, main, build

import logging


import sys

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def main():
    print("Beginning dAppCon Bot Service")

    key = sys.argv[1]

    updater = Updater(token=key)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_handler(CommandHandler('next', next))
    dispatcher.add_handler(CommandHandler('main', main))
    dispatcher.add_handler(CommandHandler('side', side))
    dispatcher.add_handler(CommandHandler('buidl', build))
    dispatcher.add_handler(CommandHandler('now', right_now))
    dispatcher.add_handler(CommandHandler('help', help))

    updater.start_polling()

if __name__ == '__main__':
    main()
