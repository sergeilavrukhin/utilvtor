from flask import current_app, render_template
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from .celery import celery
import random

def gen_password():
  password = ''
  for x in range(10):  # Количество символов (16)
    password = password + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
  return password

def send_message_over_smtp_server(msg):
  host = current_app.config["MAIL_SMTP"]
  login = current_app.config["MAIL_LOGIN"]
  password = current_app.config["MAIL_PASS"]

  with SMTP_SSL(host) as smtp:
    response_code, response_text = smtp.login(login, password)
    smtp.send_message(msg)

@celery.task(rate_limit="30/m")  # разрешено выполнятся не более 30 таких задач в минуту
def sendEmail(to: str, subject: str, body: str):
    msg = MIMEText(body, 'html')
    msg["Subject"] = subject
    msg["From"] = current_app.config["MAIL_LOGIN"]
    msg["To"] = to
    send_message_over_smtp_server(msg)

def mail_signup(email, password):
  subject = "Добро пожаловать на сайт Веботход.ру"
  html = render_template("mail_signup.tpl",
                         title=subject,
                         email=email,
                         password=password)
  sendEmail.delay(email, subject, html)

def mail_recovery(email, password):
  subject = "Новый пароль на сайт Веботход.ру"
  html = render_template("mail_recovery.tpl",
                         title=subject,
                         email=email,
                         password=password)
  sendEmail.delay(email, subject, html)

def mail_query_add():
  print('test')