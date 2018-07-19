
import logging
import os
import sys


from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

from bot_commands import start, help, echo, right_now, next, side, main, build, question

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

_log = logging.getLogger(__name__)


def deploy_bot():

    os.environ['TZ'] = 'Europe/Berlin'

    _log.info("....:Beginning dAppCon Bot Service:....")

    try:
        key = sys.argv[1]
    except IndexError:
        raise EnvironmentError(
            "Supply Telegram API-key as first script parameter!")

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
    dispatcher.add_handler(CommandHandler('question', question))

    updater.start_polling()
    _log.info("Successfully dispatched bot commands.")

if __name__ == '__main__':
    deploy_bot()
