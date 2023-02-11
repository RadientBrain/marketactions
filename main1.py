from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    baseurl = "https://www.nseindia.com/"
    url = f"https://www.nseindia.com/api/corporates-corporateActions?index=equities&from_date=01-01-2023&to_date=28-04-2023"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
               'like Gecko) '
               'Chrome/80.0.3987.149 Safari/537.36',
               'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
    session = requests.Session()
    request = session.get(baseurl, headers=headers, timeout=5)
    cookies = dict(request.cookies)
    response = session.get(url, headers=headers, timeout=5, cookies=cookies)
    response_json = response.json()
    return render_template('index1.html', data=response_json)


if __name__ == "__main__":
    app.run(debug=True)
