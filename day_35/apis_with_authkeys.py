import requests
import smtplib


def send_rain_mail():
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user='quotebot80@gmail.com', password='quotebot.p455')
    connection.sendmail(
        from_addr='quotebot80@gmail.com',
        to_addrs='atulya54321@gmail.com',
        msg='Subject:Rainy\n\nDon\'t go out'
    )


MY_LAT = 29.951065
MY_LNG = -90.071533
OWM_KEY = '6e7fd4f910dd769ac8d364afb1709d73'
CITY = 'balrampur'
API_URL = f'https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LNG}&exclude=minutely,current,alerts,daily&appid={OWM_KEY}'
# API_URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OWM_KEY}'

res = requests.get(url=API_URL)
res.raise_for_status()
for weather in res.json()["hourly"][0:12]:
    print(weather['weather'])
    if weather['weather'][0]['id'] <= 700:
        print('rain')
        send_rain_mail()
        break

