import sqlite3
import os


def get_connection():
    return sqlite3.connect("{0}/storage.sqlite".format(os.path.dirname(__file__)))


def query(sql, commit=False):
    conn = get_connection()
    res = conn.execute(sql)

    if commit:
        conn.commit()

    res = res.fetchall()
    conn.close()

    return res


def update_last_ad_id(chat_id, link_name, last_ad_id):
    query(
        f"UPDATE settings SET last_ad_id = '{last_ad_id}' WHERE link_name = '{link_name}' AND chat_id = {chat_id}", True
    )


def get_links(chat_id):
    links = query(f"SELECT * FROM settings WHERE chat_id = {chat_id}")
    if not any(links):
        raise Exception("You need to add valid link first")

    res = []

    for link in links:
        res.append({
            'id': link[0],
            'chat_id': link[1],
            'last_ad_id': link[2],
            'name': link[3],
            'link': link[4]
        })

    return res


def get_link_by_name_and_chat_id(name, chat_id):
    return query(f"SELECT link_name FROM settings WHERE chat_id = {chat_id} AND link_name = '{name}'")


def save_link(chat_id, link, link_name, last_ad_id):
    exists = get_link_by_name_and_chat_id(link_name, chat_id)

    if any(exists):
        raise Exception("Name already exists")

    query(
        "INSERT INTO settings (chat_id, last_ad_id, link, link_name) "
        f"VALUES ({chat_id}, '{last_ad_id}', '{link}', '{link_name}')",
        True
    )


def get_all():
    links = query(f'SELECT * FROM settings')

    res = []

    for link in links:
        res.append({
            'id': link[0],
            'chat_id': link[1],
            'last_ad_id': link[2],
            'name': link[3],
            'link': link[4]
        })

    return res


def del_link(chat_id, link_name):
    links = get_links(chat_id)

    found = False
    for link in links:
        if link_name == link['name']:
            found = True
            break

    if not found:
        raise Exception(f"{link_name} not exists")

    query(
        f"DELETE FROM settings WHERE chat_id = {chat_id} AND link_name = '{link_name}'", True)
