import schedule
import time
import smtplib
import config
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = config.email
password = config.password

sms_gateway = config.text

smtp = "smtp.gmail.com"
port = 587

server = smtplib.SMTP(smtp,port)

server.starttls()

server.login(email,password)

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = sms_gateway

def job():
    msg['Subject'] = "Habit Tracker!"
    body = "Don't forget to code today!"
    msg.attach(MIMEText(body, 'plain'))
    sms = msg.as_string()
    server.sendmail(email,sms_gateway,sms)
    return

schedule.every().day.at("19:30").do(job) #currently at 7:30

while True:
    schedule.run_pending()
    time.sleep(60)