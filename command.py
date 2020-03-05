import parser
import storage
import time


COMMANDS = ('/start', '/add', '/del', '/notify', '/links')


def start(update, context):
    text = 'Available commands:\n' + '\n'.join(COMMANDS)
    context.bot.send_message(update.effective_chat.id, text=text)


def add(update, context):
    chat_id = update.effective_chat.id
    try:
        link = ''
        link_name = ''

        if len(context.args) != 2:
            raise Exception('Wrong args, correct example: /add name=a4 uri=/lv/transport/cars/audi/a4')

        for arg in context.args:
            if arg.startswith('name='):
                link_name = arg.split('=')[1]
                continue

            if arg.startswith('uri='):
                link = arg.split('=')[1]

                if not link.endswith('/'):
                    link += '/'

                if not link.startswith('/'):
                    link = '/' + link

                continue

            raise Exception('Wrong args, correct example: /add name=a4 uri=/lv/transport/cars/audi/a4')

        if not link:
            raise Exception('link not passed')

        if not link_name:
            raise Exception('name not passed')

        last_ad_id = parser.get_last_ad_id_by_link(link)
        storage.save_link(chat_id, link, link_name, last_ad_id)
        context.bot.send_message(chat_id, text='Saved')
    except Exception as e:
        context.bot.send_message(chat_id, text=str(e))


def delete(update, context):
    chat_id = update.effective_chat.id
    try:
        if len(context.args) != 1:
            raise Exception('You can pass only name argument, example: /del a4')

        link_name = context.args[0]

        if not link_name:
            raise Exception('name not passed')

        storage.del_link(chat_id, link_name)
        context.bot.send_message(chat_id, text='Successfully deleted')
    except Exception as e:
        context.bot.send_message(chat_id, text=str(e))


def notify(update, context):
    chat_id = update.effective_chat.id
    try:
        links = storage.get_links(chat_id)

        for link in links:
            time.sleep(1)
            context.bot.send_message(chat_id, text=f"<{link['name']}>")
            parser.get_latest(context.bot,
                              chat_id,
                              link['link'],
                              link['last_ad_id'],
                              link['name'])

            context.bot.send_message(chat_id, text=f"</{link['name']}>")
    except Exception as e:
        context.bot.send_message(chat_id, text=str(e))


def get_user_links(update, context):
    chat_id = update.effective_chat.id
    try:
        links = storage.get_links(chat_id)
        text = ''

        for link in links:
            text += f"\n{link['name']}: {link['link']}"

        context.bot.send_message(chat_id, text=text)
    except Exception as e:
        context.bot.send_message(chat_id, text=str(e))
