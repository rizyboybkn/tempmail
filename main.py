from typing import Union
import requests
import uvicorn

from fastapi import FastAPI
from fp.fp import FreeProxy

app = FastAPI()


@app.get("/")
def root():
    return "hi"


@app.get("/getMail")
def read_root():
    proxy = FreeProxy(elite=True,timeout=1).get()
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
                             proxies={
                                 'http': proxy,
                                 'https': proxy
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
        'https://web2.temp-mail.org/messages', headers=headers)
    return response.json()
