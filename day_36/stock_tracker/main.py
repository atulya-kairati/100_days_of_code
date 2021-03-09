import requests
import smtplib

STOCK_API = "https://www.alphavantage.co/query"
NEWS_API = 'https://newsapi.org/v2/everything'

STOCK_API_KEY = '2ZU4LG7Z6K1R1HIA'
EQUITY = 'TSLA'
NEWS_API_KEY = '745f33cfd212490ea77a51ce8cf50eee'
CRITICAL_CHANGE = 100000

stock_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": EQUITY,
    "apikey": STOCK_API_KEY,
}


def send_alert_mail(msg, to='atulya54321@gmail.com'):
    creds = 'quotebot80@gmail.com', 'quotebot.p455'
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=creds[0], password=creds[1])
    msg = 'Subject:Stock Fluctuation\n\n {0}'.format(msg).encode('utf-8')
    print(msg)
    connection.sendmail(from_addr=creds[0], to_addrs=to, msg=msg)


def get_news(topic):
    news_api_params = {
        'q': topic,
        'apiKey': NEWS_API_KEY,
    }
    res_news = requests.get(url=NEWS_API, params=news_api_params)
    res_news.raise_for_status()
    news = res_news.json()['articles']
    return '\n\n'.join([article['description'] for article in news])


res = requests.get(url=STOCK_API, params=stock_api_params)
res.raise_for_status()
daily_data = res.json()['Time Series (Daily)']
yesterday, day_before_yesterday = list(daily_data.keys())[1:3]
diff = float(daily_data[yesterday]['4. close']) - float(daily_data[day_before_yesterday]['4. close'])
print(diff)
if abs(diff) > CRITICAL_CHANGE:
    headlines = get_news('tesla')
    send_alert_mail(msg=f'{EQUITY} changed by {diff}\n\nPossible Reasons:\n{headlines}')
else:
    print('Change is not that great so.... Byeee.')
print([yesterday, day_before_yesterday])
print(daily_data[yesterday])
print(daily_data[day_before_yesterday])
