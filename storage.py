from collections import defaultdict


MAX_LINKS_PER_USER = 3
SETTINGS = defaultdict(dict)


def update_last_ad_id(user_id, link_name, last_ad_id):
    SETTINGS[user_id][link_name]['last_ad_id'] = last_ad_id


def get_links(user_id):
    if user_id not in SETTINGS or len(SETTINGS[user_id]) == 0:
        raise Exception('You need to add valid link first')

    return SETTINGS[user_id]


def save_link(user_id, link, link_name, last_ad_id):
    if user_id in SETTINGS:
        if link_name in SETTINGS[user_id]:
            raise Exception('This name is already in use')

        if len(SETTINGS[user_id]) >= MAX_LINKS_PER_USER:
            raise Exception('You have maximum available links saved')

    SETTINGS[user_id][link_name] = {'link': link, 'last_ad_id': last_ad_id}


def del_link(user_id, link_name):
    if user_id not in SETTINGS:
        raise Exception('You dont have any saved links')

    if link_name not in SETTINGS[user_id]:
        raise Exception(f'{link_name} not exists')

    del SETTINGS[user_id][link_name]
