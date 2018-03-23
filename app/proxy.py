import requests
from fake_useragent import UserAgent
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


UA = UserAgent()
API_HEADER = {
    'User-Agent': UA.random,
    'Content-Type': 'text/plain;charset=UTF-8',
    'Access-Control-Allow-Origin': '*'
}

IMG_HERDER = {
    'User-Agent': UA.random,
    'Content-Type': 'images/jpeg, images/gif',
    'Access-Control-Allow-Origin': '*'
}

API = "http://news-at.zhihu.com/api/4"
s = requests.session()


@app.route("/news/before/<date>")
def daily_news_date(date):
    _url = API + "/news/before/{}".format(date)
    try:
        content = s.get(_url, headers=API_HEADER).content
    except:
        return "404"
    return content


@app.route("/news/<id>")
def daily_news_id(id):
    _url = API + "/news/{}".format(id)
    try:
        content = s.get(_url, headers=API_HEADER).content
    except:
        return "404"
    return content


@app.route('/themes')
def daily_all_themes():
    _url = API + "/themes".format()
    try:
        content = s.get(_url, headers=API_HEADER).content
    except:
        return "404"
    return content


@app.route('/theme/<id>')
def daily_theme_id(id):
    _url = API + "/theme/{}".format(id)
    try:
        content = s.get(_url, headers=API_HEADER).content
    except:
        return "404"
    return content


@app.route("/img/<path:url>")
def daily_images(url):
    try:
        content = s.get(url, headers=IMG_HERDER).content
    except:
        return "404"
    return content


if __name__ == "__main__":
    app.run()
