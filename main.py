from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        from_date = request.form['from_date']
        to_date = request.form['to_date']
        baseurl = "https://www.nseindia.com/"
        url = f"https://www.nseindia.com/api/corporates-corporateActions?index=equities&from_date={from_date}&to_date={to_date}"
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                   'like Gecko) '
                   'Chrome/80.0.3987.149 Safari/537.36',
                   'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}
        session = requests.Session()
        req = session.get(baseurl, headers=headers, timeout=5)
        cookies = dict(req.cookies)
        resp = session.get(url, headers=headers, timeout=5, cookies=cookies)
        response_json = resp.json()
        # print(response_json)
        return render_template('result.html', actions=response_json)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

# GET /live_market/dynaContent/live_watch/get_quote/companySnapshot/getCorporateActions.json HTTP/1.1
# Accept: */*
# Accept-Encoding: gzip, deflate, br
# Accept-Language: en-GB,en;q=0.9
# Connection: keep-alive
# Cookie: NSE-TEST-1=1960845322.20480.0000; JSESSIONID=58F2007E10B1287664ECF52FAEC92F94.tomcat1; bm_mi=26EFC3D432547ABE19BBDAA83552C60B~YAAQ1IosMSsYh9SFAQAANfc8LRKC96m4SF4EBCSYUynkzYOpMoIGa+VtpJ1ilJa+sh7eL0vOOWX1fuCT6buRs3wECj2sv9W7Llme6jXNaJ9v7JAbHhxMyFNnyfzXhuX5DaRivUO+fGoVuOMk+4JK4T2hggKh/MXcW6QBbAQb3KiTKxPeLjdAwRrGRlqfvHa6FCxDGyoxqB9xENEQ115K7ureY+7yOs4wzqfpf4qwRqzRCV/b0D6/fXS3J0wH3pJCKI1Iblg65SiVmBxgpW/kb3T12ypq0b75OsNuL7Uye5YN+HV6aeD0OZg61lkwGKxlG5yF7hqE+WcFlY4xm9dS9+++4kL37XMLM40=~1; ak_bmsc=7F6C5FA0A926A58E6637C483F27539C9~000000000000000000000000000000~YAAQ1IosMYAeh9SFAQAAk909LRIvPxaEfgNzHPlprWFJbpqL9Dm45w2LwjT1kmycO70j2SIJTYkM874XCEBjV3Z7yW8sfS5eKQ9JVCO6mJyRFmRyTak+9hhyBXvkEXQSEGl6ouvMTNcPtIO2zg7b4pHGll3jIjuGPYfVwbzAeiQPEDpcBMbMw53JgKLwN1hMQxfwEgjD4+5lg6mpcrFp/9oMPQO8NnVXVqkFKzqzAkbrkEC+Rfh85SG8emLic6cMaU6ZNdJl341lhVz4ufXkWwmrYNNE/JbhjvrZsBZQ4io/1mh+muqVElOonIKq+F2ZAYV5p6V1DovIbIncIkgFO+flivmKC1+nDRRTf9HCzrjZ5ODezSnWK4Tg6zZtEM3PIA/M7IUEHmK70eUy6gv0Vmhz8W/l4zhKlSOzOaCsVuGtK/aOIDY1KxQidtSaQDU=; bm_sv=83C71DFAF0CAE86BAB5C3BB9B64D2A4A~YAAQ1owsMeXFeSaGAQAA1gBcLRL7bCri50Cm2Jvk9L4gU+A5SsvAU0LCWjfbMYVvNTjPp8f1SthbNK3V1dj2WgOFqZjZ3QXNe3DWVSqFDOxZpcvlTyTtDwk5UwCx5zAumBrmLvAh75NhMs8bU6Iq9bJ9WwXKBC/SVr8EKG9J5NhBrxfmPx5IZQleUvPhk+3bWB8WriVrg1qMjsEBs0fFP3spprokZbr0EIwKz30Qbi4NG2RrYW5TUPoW0vkFfvnW2JE1~1
# Host: www1.nseindia.com
# Referer: https://www1.nseindia.com/corporates/corporateHome.html
# Sec-Fetch-Dest: empty
# Sec-Fetch-Mode: cors
# Sec-Fetch-Site: same-origin
# Sec-GPC: 1
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
# X-Requested-With: XMLHttpRequest

# fetch("https://www.nseindia.com/api/corporates-corporateActions?index=equities&from_date=02-02-2023&to_date=28-02-2023", {
#   "headers": {
#     "accept": "*/*",
#     "accept-language": "en-GB,en;q=0.9",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "sec-gpc": "1"
#   },
#   "referrer": "https://www.nseindia.com/companies-listing/corporate-filings-actions",
#   "referrerPolicy": "strict-origin-when-cross-origin",
#   "body": null,
#   "method": "GET",
#   "mode": "cors",
#   "credentials": "include"
# });
