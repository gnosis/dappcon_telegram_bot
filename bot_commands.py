from datetime import datetime

import utils

SCHEDULE = utils.load_schedule()

def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="I'm the dAppCon Schedule bot! Type /help for a list of commands"
    )

def echo(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=update.message.text
    )

def now(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=str(datetime.now())
    )

def next(bot, update):
    now = datetime.now()

    build = [b for b in SCHEDULE if b.location == 'Buidl Room' if b.start >= now]
    main = [m for m in SCHEDULE if m.location == 'Mainchain Stage' if m.start >= now]
    side = [s for s in SCHEDULE if s.location == 'Sidechain Stage' if s.start >= now]

    next_build = sorted(build, key=lambda x: x.start)[0]
    next_main = sorted(main, key=lambda x: x.start)[0]
    next_side = sorted(side, key=lambda x: x.start)[0]

    mess = '\n\n'.join(map(str, [next_main, next_side, next_build]))
    bot.send_message(chat_id=update.message.chat_id, text=mess)


def rest(rest_of_what):
    now = datetime.now()

    rest = [
        m for m in SCHEDULE if m.location == rest_of_what
        if m.start >= now and m.start.date() == now.date()
    ]

    remaining = sorted(rest, key=lambda x: x.start)

    message = '\n\n'.join(map(str, remaining))
    return message


def main(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=rest('Mainchain Stage')
    )

def side(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=rest('Sidechain Stage')
    )

def build(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=rest('Buidl Room')
    )

def right_now(bot, update):
    current_events = [e for e in SCHEDULE if e.is_now()]
    empty = "There are no current events at the moment!"
    mess = '\n\n'.join(map(str, current_events)) or empty
    bot.send_message(
        chat_id=update.message.chat_id,
        text=mess
    )

def help(bot, update):
    available_commands = [
        '/next - shows next event in each of the three areas',
        '/now - displays current events',
        '/main - remaining events for today on Mainchain',
        '/side - remaining events for today on Sidechain',
        '/buidl - remaining events for today on Buidl',
        '/start - welcome message when joining the chat',
        '/help - shows the message you are reading right now!'
    ]
    bot.send_message(
        chat_id=update.message.chat_id,
        text='\n'.join(available_commands)
    )