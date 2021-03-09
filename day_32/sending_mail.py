import smtplib

bot_mail = 'quotebot80@gmail.com'
mail_password = 'quotebot.p455'

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()

connection.login(user=bot_mail, password=mail_password)
connection.sendmail(from_addr=bot_mail, to_addrs='atulya54321@gmail.com', msg='Subject:Hey Friend\n\nHello Bro')
connection.close()
