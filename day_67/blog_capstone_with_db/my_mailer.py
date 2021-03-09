import smtplib


def sendmail(detail: dict):
    bot_mail = 'quotebot80@gmail.com'
    mail_password = 'quotebot.p455'
    mail_to = 'atulya54321@gmail.com'

    msg = f'''
Name: {detail.get('name')}
E-mail: {detail.get('email')}
Phone num: {detail.get('phonenum')}\n\n
Message:\n{detail.get('msg')}
    '''

    con = smtplib.SMTP('smtp.gmail.com')
    con.starttls()
    con.login(user=bot_mail, password=mail_password)
    con.sendmail(from_addr=bot_mail, to_addrs=mail_to, msg=f'Subject:Mail from Blog site\n\n{msg}')
    con.close()
