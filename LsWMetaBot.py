from telegram.ext import Updater, CommandHandler

updater = Updater(token='TELEGRAM-BOT-TOKEN')
dispatcher = updater.dispatcher

def meta(bot, update):
    bot.send_message(chat_id=update.message.chat_id, 
        text="Warning. System discovered a meta question.\nIs there a concrete question on the topic ? (Y/n):\n(Was ist eine Metafrage: http://metafrage.de/)")
    localtime = time.asctime( time.localtime(time.time()) )
    print(localtime, " - Meta Befehl wurde ausgeführt!")
def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="LsW Metafragen-Bot. https://github.com/DeatPlayer/lsw-meta-bot")
    localtime = time.asctime( time.localtime(time.time()) )
    print(localtime, " - Help Befehl wurde ausgeführt!")

meta_handler = CommandHandler('meta', meta)
dispatcher.add_handler(meta_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

updater.start_polling()
