import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import time
import random
 


sender='gmawarni9@gmail.com'
password='Hackeline!'

receiver= 'gjpcalvinho@gmail.com'


msg = MIMEMultipart()
msg["From"] = 'Gladys - Data TA'
msg['Subject'] = "Weekly Lab Summary"
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""


part1 = MIMEText(text, "plain")

msg.attach(part1)


server= smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.sendmail(sender,receiver,msg.as_string())

sleep_time = random.random()*3
time.sleep(sleep_time)


