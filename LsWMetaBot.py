from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
import time
import sys
import re

updater = Updater(token='TELEGRAM-BOT-TOKEN')
dispatcher = updater.dispatcher

regex_pattern = "/(würde|ist|kennt|kann|darf|hat).+(jemand|jemande[m|n]|dich|euch|zufällig|mir).+(mit.+[a-zA-Z](.+auskennt\?|.+aus\?|.+aus[,| ]+der.+kann\?|helfen\?)|fragen\?|jemand helfen\?|(mir|uns) bei [a-zA-Z ]+ helfen\?)/gmi"
meta_text = "Warning. System discovered a meta question.\nIs there a concrete question on the topic ? (Y/n):\n(Was ist eine Metafrage: http://metafrage.de/)"
help_text = "LsW Metafragen-Bot. https://github.com/DeatPlayer/lsw-meta-bot"

def meta(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=meta_text)
    localtime = time.asctime( time.localtime(time.time()) )
    sys.stdout.write(localtime + " [INFO] Command: /meta - Chat-ID: " + update.message.chat_id + " => " + update.message.text)

def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=help_text)
    localtime = time.asctime( time.localtime(time.time()) )
    sys.stdout.write(localtime + " [INFO] Command: /help - Chat-ID: " + update.message.chat_id + " => " + update.message.text)
    
def metadetector(bot, update):
    message = update.message.text
    pattern = re.compile(regex_pattern, re.IGNORECASE)
    detected = pattern.search(message)
    if detected:
        bot.send_message(chat_id=update.message.chat_id, text=meta_text)
    localtime = time.asctime( time.localtime(time.time()) )
    sys.stdout.write(localtime + " [INFO] Command: autodetect - Chat-ID: " + update.message.chat_id + " => " + update.message.text)

autoresponse_handler = MessageHandler(Filters.text, metadetector)
dispatcher.add_handler(autoresponse_handler)

meta_handler = CommandHandler('meta', meta)
dispatcher.add_handler(meta_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

updater.start_polling()
