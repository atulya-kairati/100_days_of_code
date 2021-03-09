import smtplib


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""
    bot_mail = 'quotebot80@gmail.com'
    mail_password = 'quotebot.p455'

    def __init__(self):
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(user=NotificationManager.bot_mail, password=NotificationManager.mail_password)
        self.connection = connection

    def send_mail_notification(self, msg, to='atuly54321@gmail.com'):
        msg = f'Subject:Budget Flight Alert\n\n{msg}'.encode('utf-8')
        self.connection.sendmail(from_addr=self.bot_mail, to_addrs=to, msg=msg)
