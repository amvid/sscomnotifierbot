import os
from telegram.ext import Updater, CommandHandler
import command
from dotenv import load_dotenv
load_dotenv()


updater = Updater(token=os.getenv('TELEGRAM_TOKEN'), use_context=True, request_kwargs={
    'read_timeout': 30, 'connect_timeout': 30
})

dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', command.start))
dispatcher.add_handler(CommandHandler('notify', command.notify))
dispatcher.add_handler(CommandHandler('add', command.add))
dispatcher.add_handler(CommandHandler('del', command.delete))
dispatcher.add_handler(CommandHandler('links', command.get_user_links))

if __name__ == '__main__':
    updater.start_polling()
    print('Start listening...')
