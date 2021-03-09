import smtplib
import unicodedata

import requests
from bs4 import BeautifulSoup

# amazon blocks if it sees a bot
reasonable_price = 300
bot_mail = 'quotebot80@gmail.com'
mail_password = 'quotebot.p455'


def send_mail(msg):
    conn = smtplib.SMTP('smtp.gmail.com')
    conn.starttls()
    conn.login(user=bot_mail, password=mail_password)
    conn.sendmail(from_addr=bot_mail, to_addrs="atulya54321@gmail.com", msg=f'Subject:Price Drop Alert\n\n{msg}')


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
    }
product_url = "https://www.amazon.in/Xiaomi-Redmi-Hi-Resolution-Audio-Earphone/dp/B08FMLCRXM/ref=sr_1_3?dchild=1&keywords=mi+earphone&qid=1610293703&sr=8-3"
res = requests.get(
    url=product_url,
    headers=headers,
)

res.raise_for_status()


soup = BeautifulSoup(res.text, 'html.parser')

price = float(unicodedata.normalize('NFKD', soup.find(name="span", id="priceblock_ourprice").getText()).split(' ')[1])
print(price)

if price <= reasonable_price:
    print('BUY It!')
    send_mail(msg=product_url)
else:
    print('Don\'t')
