from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time
import re

updater = Updater(token='TELEGRAM-BOT-TOKEN')
dispatcher = updater.dispatcher

regex_pattern = "(würde|ist|kennt|kann|darf|hat).+(jemand|jemande[m|n]|dich|euch|zufällig|mir).+(mit.+[a-zA-Z](.+auskennt\?|.+aus\?|.+aus[,| ]+der.+kann\?|helfen\?)|fragen\?|jemand helfen\?|(mir|uns) bei [a-zA-Z ]+ helfen\?)"
meta_text = "Warnung! System hat eine Metafrage entdeckt. Gibt es eine konkrete Frage zum Thema? (J/n):\n(Was ist eine Metafrage: http://metafrage.de/)"
help_text = "LsW Metafragen-Bot. https://github.com/DeatPlayer/lsw-meta-bot"

#auto-reply cooldown in seconds
min_call_freq = 30
used = {}

def fnmeta(bot: Bot, update: Update):
    bot.send_message(chat_id=update.message.chat_id, text=meta_text)
    localtime = time.asctime( time.localtime(time.time()) )
    print(localtime + ' >> [INFO] Command: /meta')

def fnhelp(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=help_text)
    localtime = time.asctime( time.localtime(time.time()) )
    print(localtime + ' >> [INFO] Command: /help')

def metadetector(bot, update):
    message = update.message.text
    pattern = re.compile(regex_pattern, re.IGNORECASE)
    detected = pattern.search(message)
    if detected:
        localtime = time.asctime( time.localtime(time.time()) )
        if "autodetected" not in used or time.time() - used["autodetected"] > min_call_freq:
          used["autodetected"] = time.time()
          bot.send_message(chat_id=update.message.chat_id, text=meta_text, reply_to_message_id=update.message.message_id)
          print(localtime + ' >> [INFO] Command: autodetect')
        else:
          print(localtime + ' >> [INFO] Cooldown active..')

autoresponse_handler = MessageHandler(Filters.text, metadetector)
dispatcher.add_handler(autoresponse_handler)

meta_handler = CommandHandler('meta', fnmeta)
dispatcher.add_handler(meta_handler)

help_handler = CommandHandler('help', fnhelp)
dispatcher.add_handler(help_handler)

updater.start_polling()
