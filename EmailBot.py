import smtplib
import os
from email.mime.text import MIMEText


def send_email(recipient, message):

    sender = "your_email@gmail.com"  # Адрес отправителя
    password = os.getenv("EMAIL_PASSWORD")  # Пароль приложения или переменная окружения

    if not password:
        return "ERROR: EMAIL_PASSWORD environment variable is not set."

    # Создаем SMTP-клиент Gmail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        # Авторизация
        server.login(sender, password)

        # Формируем письмо
        msg = MIMEText(message)
        msg["Subject"] = "CLICK ME PLEASE!"
        msg["From"] = sender
        msg["To"] = recipient

        # Отправляем письмо
        server.sendmail(sender, recipient, msg.as_string())

        return f"Message successfully sent to {recipient}!"

    except Exception as e:
        return f"ERROR: {e}\nCheck your email, password, or recipient address."

    finally:
        server.quit()


def main():
    """Основная функция: принимает email получателя и текст сообщения."""
    recipient = input("Enter recipient email: ").strip()
    message = input("Type your message: ").strip()

    if not recipient:
        print("Recipient email cannot be empty.")
        return

    if not message:
        print("Message cannot be empty.")
        return

    print(send_email(recipient, message))


if __name__ == "__main__":
    main()
