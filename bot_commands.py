from datetime import datetime
import utils

from random import randint

SCHEDULE = utils.load_schedule()

GENERIC_REPLIES = [
    'oh really!?',
    'Sounds interesting, tell me more',
    'That is definitely a good thought',
    'How about that local sport team?',
    'I completely agree',
    'Sprechen Sie Deutsch?',
    'Great weather today!',
    'I am a robot',
    'I completely agree',
    'How about this WiFi?',
    'Are you participating in the Olympia? Its lit',
    'Are there beaches in Berlin?',
    'I really enjoyed the previous talk on the Mainchain stage.',
    'Hungry for apples or bananas?',
    'I only have finitely many distinct replies.',
    'Most likely',
]


def start(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="I'm the dAppCon Schedule bot! Type /help for a list of commands. "
             "\n\nHave a question for the ongoing talks @dappcon_berlin? "
             "\nPlease head to https://www.sli.do/ and enter one of the following codes:"
             "\n - The legally - compliant DAO: More hype than substance Code: #6737"
             "\n - Look at my flashy colors and rounded corners! Code: #B398"
             "\n - Epicenter Live Code: #K367"
             "\n - Tales of governance: DAOs, Swarms and Anarchic systems Code: #Q749"
             "\n - AMA - Joseph Lubin Code: #Q293"
             "\n - How to measure success? Code: #D624"
    )


def echo(bot, update):
    random_index = randint(0, len(GENERIC_REPLIES))
    reply = GENERIC_REPLIES[random_index]
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

    build = [b for b in SCHEDULE if b.location in {'Rinkeby Room', "Kovan Room", "Ropsten Room"} if b.start >= now]
    main = [m for m in SCHEDULE if m.location == 'Mainchain Stage' if m.start >= now]
    side = [s for s in SCHEDULE if s.location == 'Sidechain Stage' if s.start >= now]


    next_build = sorted(build, key=lambda x: x.start)[0]
    next_main = sorted(main, key=lambda x: x.start)[0]
    next_side = sorted(side, key=lambda x: x.start)[0]

    warning = "(Remember that workshops don't start until friday!)"

    mess = '\n\n'.join(map(str, [next_main, next_side, next_build, warning]))
    bot.send_message(chat_id=update.message.chat_id, text=mess)


def rest(rest_of_what):
    now = datetime.now()

    rest = [
        m for m in SCHEDULE if m.location == rest_of_what
        if m.start >= now and m.start.date() == now.date()
    ]

    remaining = sorted(rest, key=lambda x: x.start)
    empty = "There are no more talks, panels or workshops there for the rest of the day!"
    message = '\n\n'.join(map(str, remaining)) or empty
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


def workshop_rinkeby(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=rest('Rinkeby Room')
    )


def workshop_kovan(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=rest('Kovan Room')
    )


def workshop_ropsten(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text=rest('Ropsten Room')
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
        '/workshop_rinkeby - remaining events for today in the Rinkeby workshop room',
        '/workshop_kovan - remaining events for today in the Kovan workshop room',
        '/workshop_ropsten - remaining events for today in the Ropsten workshop room',
        '/start - welcome message when joining the chat',
        '/help - shows the message you are reading right now!',
    ]
    bot.send_message(
        chat_id=update.message.chat_id,
        text='\n'.join(available_commands)
    )
