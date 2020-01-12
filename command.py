import parser
import storage


COMMANDS = ('/start', '/add', '/del', '/notify', '/links')


def start(update, context):
    text = 'Available commands:\n' + '\n'.join(COMMANDS)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def add(update, context):
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
        storage.save_link(user_id=update.message.chat.id, link=link, link_name=link_name, last_ad_id=last_ad_id)
        context.bot.send_message(chat_id=update.effective_chat.id, text='Saved')
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(e))


def delete(update, context):
    try:
        if len(context.args) != 1:
            raise Exception('You can pass only name argument, example: /del a4')

        link_name = context.args[0].split('=')[0]

        if not link_name:
            raise Exception('name not passed')

        storage.del_link(user_id=update.message.chat.id, link_name=link_name)
        context.bot.send_message(chat_id=update.effective_chat.id, text='Successfully deleted')
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(e))


def notify(update, context):
    try:
        user_id = update.message.chat.id
        links = storage.get_links(user_id=user_id)

        for link in links:
            parser.get_latest(bot=context.bot,
                              chat_id=update.effective_chat.id,
                              link=links[link]['link'],
                              last_ad_id=links[link]['last_ad_id'],
                              user_id=user_id,
                              link_name=link)

        context.bot.send_message(chat_id=update.effective_chat.id, text='Finished')
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(e))


def get_user_links(update, context):
    try:
        links = storage.get_links(user_id=update.message.chat.id)
        text = ''

        for link in links:
            text += f'\n{link}: {links[link]["link"]}'

        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=str(e))
