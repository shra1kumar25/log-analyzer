import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()


def send_email(alerts):
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("EMAIL_RECEIVER")

    if not sender or not password or not receiver:
        print("Email configuration is missing")
        return

    message = EmailMessage()

    message["Subject"] = "Log Analyzer Alert"
    message["From"] = sender
    message["To"] = receiver

    body = "The following alerts were detected:\n\n"

    for alert in alerts:
        if isinstance(alert, dict):
            body += f"[{alert['level']}] {alert['message']}\n"
        else:
            body += alert + "\n"

    message.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(message)

    print("Email sent successfully")
