import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender_email = "bnbmuniz@gmail.com"
receiver_email = "gjpcalvinho@gmail.com"
password = "Paraisonice2016"

message = MIMEMultipart("alternative")
message["Subject"] = "Ironhack Reviews Weekly Report"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you? :)
Attached you'll find the updated report on Ironhack reviews for last week.
Let us know if we can be on any assistance!
Cheers"""
html = """\
<html>
  <body>
    <p>Hi,<br><br>
       How are you? :)<br><br>
       Attached you'll find the updated report on Ironhack reviews for last week.
       Let us know if we can be on any assistance!
       Cheers<br>
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message.as_string())
