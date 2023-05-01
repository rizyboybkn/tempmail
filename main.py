from typing import Union
import requests
import uvicorn
from fastapi import FastAPI
from fp.fp import FreeProxy
import random

import re
url = 'https://free-proxy-list.net/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}
source = str(requests.get(url, headers=headers, timeout=10).text)
data = [list(filter(None, i))[0] for i in re.findall('<td class="hm">(.*?)</td>|<td>(.*?)</td>', source)]
groupings = [dict(zip(['ip', 'port', 'code', 'using_anonymous'], data[i:i+4])) for i in range(0, len(data), 4)]
final_groupings = [{'full_ip':"{ip}:{port}".format(**i)} for i in groupings]

def check_proxy(px):
    try:
        requests.get("https://www.google.com/", proxies = {"https":  px}, timeout = 2)
    except Exception as x:
        print('--'+px + ' is dead: '+ x.__class__.__name__)
        return False
    return True


# print(groupings)

app = FastAPI()


@app.get("/")
def root():
    return "hi"


@app.get("/getMail")
def read_root():
    # proxy = FreeProxy(country_id=['US', 'BR'], timeout=0.3, rand=True).get()
    proxy = random.choice(groupings)
    proxy = proxy['ip']  + ":" + proxy['port']
    while check_proxy(proxy) == False:  
          proxy = random.choice(groupings)
          proxy = proxy['ip']  + ":" + proxy['port']
    print(proxy)

    headers = {
        'Content-Type': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        'Origin': 'https://temp-mail.org',
        'Referer': 'https://temp-mail.org/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        # Requests doesn't support trailers
        # 'Te': 'trailers',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
    }

    response = requests.post('https://web2.temp-mail.org/mailbox', headers=headers,
                             timeout=10,
                             proxies={
                                 'http': proxy,
                                 'https': proxy,
                             },)

    return response.json()


@app.get("/messages/{token}")
def read_item(token: Union[str, None] = None):

    headers = {
        'Accept-Language': 'en-US,en;q=0.5',
        'Authorization': 'Bearer '+token,
        'Origin': 'https://temp-mail.org',
        'Referer': 'https://temp-mail.org/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        # Requests doesn't support trailers
        # 'Te': 'trailers',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
    }

    response = requests.get(
        'https://web2.temp-mail.org/messages', headers=headers)
    return response.json()


@app.get("/message/{token}/{mid}")
def read(token: Union[str, None] = None, mid: Union[str, None] = None):

    headers = {
        'Accept-Language': 'en-US,en;q=0.5',
        'Authorization': 'Bearer '+token,
        'Origin': 'https://temp-mail.org',
        'Referer': 'https://temp-mail.org/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        # Requests doesn't support trailers
        # 'Te': 'trailers',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
    }

    response = requests.get(
        'https://web2.temp-mail.org/messages/' + mid, headers=headers)
    return response.json()
