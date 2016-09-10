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

def help(bot, update):
  bot.sendMessage(update.message.chat_id, text='To start a new game, type /play. To get help, type /help. To end the current round and start a new one, type /next.')

def play(bot, update):
  scream3 = "😱😱😱"
  bot.sendMessage(update.message.chat_id, text= scream3)



# Helpers


updater = Updater(config.TELEGRAM_SECRET_KEY)

# For quicker access to the Dispatcher used by your Updater
dispatcher = updater.dispatcher

# Register the methods handling commands
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('play', play))
dispatcher.add_handler(CommandHandler('next', next))

updater.start_polling()
updater.idle()