from datetime import datetime

from random import randint
import utils

SCHEDULE = utils.load_schedule()

GENERIC_REPLIES = [
    'oh really!?',
    'You look great today',
    'Sounds interesting, tell me more',
    'That is a good thought',
    'Much wow, many excite',
    'Have you ever tried that re-usable bamboo paper towel?',
    'How about that local sport team?',
    'Awesome right?',
    'I completely agree',
    'Sprechen Sie deutsch?',
    'Great weather today!',
    'Did you get stuck in traffic this morning?',
    'I like your haircut!',
    'That sounds pleasant',
    'I am a robot',
    'I completely agree',
    'Nice venue',
    'Are you participating in the Olympia?',
    'I would like to go to the beach.',
    'I really enjoyed the previous talk on the Mainchain stage.',
    'Hungry for apples?',
    'I only have finitely many distinct replies.',
    'All signs point to yes',
    'Lemonade is the German word for pop which is the Canadian word for soda',
    'Most likely',
]

def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="I'm the dAppCon Schedule bot! Type /help for a list of commands. "
             "\nHave a question for the ongoing talks @dappcon_berlin? "
             "Please head to https://www.sli.do/ and enter the code 9189 to ask your question!"
    )

def echo(bot, update):
    random_index = randint(0, len(GENERIC_REPLIES))
    reply = GENERIC_REPLIES[random_index]
    # reply = "Have a question for the ongoing talks @dappcon_berlin?\n" \
    #         "Please head to https://www.sli.do/ and enter the code 9189 to ask your question!"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=reply
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

def question(bot, update):
    reply = "Have a question for the ongoing talks @dappcon_berlin?\n" \
            "Please head to https://www.sli.do/ and enter the code 9189 to ask your question!"
    bot.send_message(
        chat_id=update.message.chat_id,
        text=reply
    )

def help(bot, update):
    available_commands = [
        '/next - shows next event in each of the three areas',
        '/now - displays current events',
        '/question - reminder link to ask questions about a talk',
        '/main - remaining events for today on Mainchain',
        '/side - remaining events for today on Sidechain',
        '/buidl - remaining events for today on Buidl',
        '/start - welcome message when joining the chat',
        '/help - shows the message you are reading right now!',
        '\nAlso, type anything for a link to ask questions about a talk'
    ]
    bot.send_message(
        chat_id=update.message.chat_id,
        text='\n'.join(available_commands)
    )