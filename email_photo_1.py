import smtplib
import os
from email.message import EmailMessage
import imghdr
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

subject = 'Python Mail'

msg = MIMEMultipart()
msg['From'] = "kk28296@gmail.com"
msg['To'] = "kk28296@gmail.com"

body  = 'Hey boy, check this out image'
msg.attach(MIMEText(body, 'plain'))

filename = '2.png'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename=" +filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("kk28296@gmail.com", "ihtrakmk")
server.sendmail("kk28296@gmail.com", "kk28296@gmail.com", text)

server.quit()
