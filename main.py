
import logging
import os
import sys


from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

from bot_commands import start, help, echo, right_now, next, side, main, workshop_rinkeby, workshop_kovan, workshop_ropsten

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
    dispatcher.add_handler(CommandHandler('workshop_rinkeby', workshop_rinkeby))
    dispatcher.add_handler(CommandHandler('workshop_kovan', workshop_kovan))
    dispatcher.add_handler(CommandHandler('workshop_ropsten', workshop_ropsten))
    dispatcher.add_handler(CommandHandler('now', right_now))
    dispatcher.add_handler(CommandHandler('help', help))

    updater.start_polling()
    _log.info("Successfully dispatched bot commands.")

if __name__ == '__main__':
    deploy_bot()
