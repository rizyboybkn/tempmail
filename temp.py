import requests


def getCsrf(html):
    # html = requests.get("https://www.sonicbit.net")
    # csrf = ""
    # html = html.text
    html = html.split("\n")
    for i in html:
        if ('<meta name="csrf-token" content="' in i):
            csrf = i.replace(
                '<meta name="csrf-token" content="', "").replace('">', "")
            csrf = csrf.replace(" ", "")
            return csrf


session = requests.Session()
home = session.get("https://dash.sonicbit.net/login")
csrf = getCsrf(home.text)
data = {
    '_token': csrf,
    '_method': 'POST',
    'email': 'goincop1+2@gmail.com',
    'password': '@Anu123456',
    'remember': 'false',
}
login = session.post("https://dash.sonicbit.net/login_user", data=data)
home2 = session.get("https://dash.sonicbit.net/")
csrf = getCsrf(home2.text)

data = {
    '_token': csrf,
    'keyword': 'deadpool 2 hindi',
    'cat_name': 'Movies',
    'category': '2',
}


response = session.post(
    'https://dash.sonicbit.net/function/search-torrent-v3', data=data)


print(response.json())

