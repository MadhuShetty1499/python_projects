import os
from twilio.rest import Client
import smtplib

FROM_NUMBER = os.environ.get("FROM_NUMBER")
TO_NUMBER = os.environ.get("TO_NUMBER")
TWILIO_ACC_SID = os.environ.get("ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
EMAIL = os.environ.get("FROM_EMAIL")
PASSWORD = os.environ.get("EMAIL_PASSWORD")


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_sms(self, message):
        client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            from_=FROM_NUMBER,
            to=TO_NUMBER,
            body=message,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(EMAIL, PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
