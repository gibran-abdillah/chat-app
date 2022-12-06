import requests, re
from bs4 import BeautifulSoup
from .core.message import send_message
from asgiref.sync import async_to_sync

session = requests.Session()
session.headers['User-Agent'] = 'Mozilla/5.0'

URL = 'https://www.lyricfinder.org/search?searchtype=tracks&query={}'

async def get_lyrics(url):
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    link = soup.find('a', attrs={'class':'list-group-item'})
    if link and link.get('href'):
        follow_link = session.get(f"https:{link.get('href')}").text 
        soup = BeautifulSoup(follow_link, 'html.parser')
        col_lg_6 = soup.find('div', attrs={'class':'col-lg-6'})
        return str(col_lg_6)
    return "Sorry, we cant find it :("

async def execute_command(argument, group_room_code):
    send_message('Working on it....', group_room_code)
    if len(argument) == 0:
        return "usage : /lyrics Song Name"
    response = await get_lyrics(URL.format('+'.join(argument)))
    #return response
    return response