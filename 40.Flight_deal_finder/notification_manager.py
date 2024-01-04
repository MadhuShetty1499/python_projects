import os
from twilio.rest import Client

FROM_NUMBER = os.environ.get("FROM_NUMBER")
TO_NUMBER = os.environ.get("TO_NUMBER")
TWILIO_ACC_SID = os.environ.get("ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_sms(self, price, origin_city, origin_city_code, destination_city, destination_city_code, from_date, to_date):
        client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            from_=FROM_NUMBER,
            to=TO_NUMBER,
            body=f"Low price alert! Only £{price} to fly from {origin_city}-{origin_city_code}"
                 f"to {destination_city}-{destination_city_code}, from {from_date} to {to_date}."
        )
        print(message.sid)
