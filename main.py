# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
import config

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Methods handling commands

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Hello, would you like to play a game? I'm going to send you emojis and you tell me what movie title they refer to. Ok? If you ever need help, type /help!")

def hello(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Hello {}'.format(update.message.from_user.first_name))

def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='To start a new game, type /start. To get help, type /help. To end the current round and start a new one, type /next.')

def echo(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)


# Helpers

echo_handler = MessageHandler([Filters.text], echo)
caps_handler = CommandHandler('caps', caps, pass_args=True)

updater = Updater(config.TELEGRAM_SECRET_KEY)

# For quicker access to the Dispatcher used by your Updater
dispatcher = updater.dispatcher

# Register the methods handling commands
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('hello', hello))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)

updater.start_polling()
updater.idle()