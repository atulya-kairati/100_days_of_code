import datetime as dt
import smtplib
from random import choice


def send_mail(quote):
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=bot_mail, password=mail_password)
    connection.sendmail(from_addr=bot_mail, to_addrs='atulya54321@gmail.com', msg=f'Subject:Monday Motivation\n\n{quote}')
    connection.close()


bot_mail = 'quotebot80@gmail.com'
mail_password = 'quotebot.p455'


if dt.datetime.now().weekday() == 0: # Monday
    with open('quotes.txt') as file:
        quotes = file.read().split('\n')
    send_mail(choice(quotes))
else:
    print('Not Monday Today')