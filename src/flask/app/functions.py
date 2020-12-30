from flask import current_app, render_template
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
from .celery import celery

def send_message_over_smtp_server(msg):
  host = current_app.config["MAIL_SMTP"]
  login = current_app.config["MAIL_LOGIN"]
  password = current_app.config["MAIL_PASS"]

  with SMTP_SSL(host) as smtp:
    response_code, response_text = smtp.login(login, password)
    smtp.send_message(msg)

@celery.task(rate_limit="30/m")  # разрешено выполнятся не более 30 таких задач в минуту
def sendEmail(to: str, subject: str, body: str):
    html = render_template("mail.tpl", title=subject, body=body)
    msg = MIMEText(html, 'html')
    msg["Subject"] = subject
    msg["From"] = current_app.config["MAIL_LOGIN"]
    msg["To"] = to
    send_message_over_smtp_server(msg)