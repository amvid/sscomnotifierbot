from bs4 import BeautifulSoup
import storage
import requests
import re


HOST = 'https://ss.com'


def get_html_text(link):
    url = HOST + link
    session_request = requests.session()
    resp = session_request.get(url,
                               headers={
                                   'Content-type': 'application/x-www-form-urlencoded',
                                   'Referrer': HOST})

    if resp.status_code != 200:
        raise Exception('Something went wrong with url or it not exists: ' + url)

    return resp.text


def get_latest(bot, chat_id, link, last_ad_id, link_name, user_id):
    html = get_html_text(link)
    soup = BeautifulSoup(html, 'html.parser')
    ads = soup.find_all(id=re.compile(r'tr_[0-9]*'))
    iteration = 0
    new_last_ad_id = 0

    for ad in ads:
        current_id = ad.get('id')

        if current_id == last_ad_id:
            break

        if iteration == 0:
            new_last_ad_id = current_id

        iteration += 1
        childrens = ad.findChildren('td', class_='msga2', recursive=False)

        for child in childrens:
            link_tag = child.find('a', href=True)

            if not link_tag:
                continue

            text = HOST + link_tag.get('href')
            bot.send_message(chat_id=chat_id, text=text)
            break

        storage.update_last_ad_id(user_id=user_id, last_ad_id=new_last_ad_id, link_name=link_name)


def get_last_ad_id_by_link(link):
    html = get_html_text(link)
    soup = BeautifulSoup(html, 'html.parser')
    ads = soup.find_all(id=re.compile(r'tr_[0-9]*'))

    for ad in ads:
        return ad.get('id')

    raise Exception('Wrong link')
