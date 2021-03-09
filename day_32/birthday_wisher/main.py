import smtplib
import datetime as dt
from random import choice
import json

bot_mail = 'quotebot80@gmail.com'
mail_password = 'quotebot.p455'


def send_mail(to, msg, name):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=bot_mail, password=mail_password)
        connection.sendmail(from_addr=bot_mail, to_addrs=to, msg=f'Subject:Happy Birthday {name.title()}\n\n{msg}')


today = dt.datetime.now()
print(today)
with open('birthday_dates.json') as file:
    data = json.load(fp=file)

for name, details in data.items():
    if details['day'] == today.day and details['month'] == today.month:
        with open('wishes.txt') as file:
            wish = choice(file.read().split('\n'))
        send_mail(to=details['email'], name=name, msg=wish)

