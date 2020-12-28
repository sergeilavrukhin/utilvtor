
def get_login_smtp(email: str) -> str:
    mail_server = email.split("@")[1]
    if mail_server in ["mail.ru", "list.ru", "bk.ru"]:
        login = current_app.config["MAIL_RU_LOGIN"]
    else:
        login = current_app.config["YANDEX_RU_LOGIN"]
    return login

def get_smtp_settings(email: str) -> Tuple[str, str, str]:
  login: str = get_login_smtp(email)
  if login == current_app.config["MAIL_RU_LOGIN"]:
    host = current_app.config["MAIL_RU_HOST"]
    login = current_app.config["MAIL_RU_LOGIN"]
    password = current_app.config["MAIL_RU_PASSWORD"]
  else:
    host = current_app.config["YANDEX_RU_HOST"]
    login = current_app.config["YANDEX_RU_LOGIN"]
    password = current_app.config["YANDEX_RU_PASSWORD"]
  return host, login, password

def send_message_over_smtp_server(msg):
    host, login, password = get_smtp_settings(msg["to"])

    with SMTP_SSL(host) as smtp:
        response_code, response_text = smtp.login(login, password)
        smtp.send_message(msg)

def sendEmail(to: str, theme: str, text: str):
    # Отправка email пользователю
    msg = MIMEText(text)
    msg["Subject"] = theme
    msg["From"] = get_login_smtp(to)
    msg["to"] = current_app.config.get("MAIL_TO", to)
    send_message_over_smtp_server(msg)