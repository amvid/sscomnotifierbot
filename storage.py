from collections import defaultdict


MAX_LINKS_PER_CHAT = 7
SETTINGS = defaultdict(dict)


def update_last_ad_id(chat_id, link_name, last_ad_id):
    SETTINGS[chat_id][link_name]['last_ad_id'] = last_ad_id


def get_links(chat_id):
    if chat_id not in SETTINGS or len(SETTINGS[chat_id]) == 0:
        raise Exception('You need to add valid link first')

    return SETTINGS[chat_id]


def save_link(chat_id, link, link_name, last_ad_id):
    if chat_id in SETTINGS:
        if link_name in SETTINGS[chat_id]:
            raise Exception('This name is already in use')

        if len(SETTINGS[chat_id]) >= MAX_LINKS_PER_CHAT:
            raise Exception('You have maximum available links saved per chat')

    SETTINGS[chat_id][link_name] = {'link': link, 'last_ad_id': last_ad_id}


def del_link(chat_id, link_name):
    if chat_id not in SETTINGS:
        raise Exception('You dont have any saved links')

    if link_name not in SETTINGS[chat_id]:
        raise Exception(f'{link_name} not exists')

    del SETTINGS[chat_id][link_name]
