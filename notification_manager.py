import os
from twilio.rest import Client

from flight_data import FlightData


class NotificationManager:
    def __init__(self):
        self.client = Client(os.getenv('TWILIO_SID_KEY'), os.getenv('TWILIO_AUTH_TOKEN'))

    def send_msg(self, flight_data: FlightData):
        msg = (f"Sent from your Twilio trial account\n"
               f"- Low price alert! Only R${flight_data.price} to fly from {flight_data.origin} to {flight_data.destination},"
               f" on {flight_data.out_date} until {flight_data.return_date}.")
        message = self.client.messages.create(
            from_=f'whatsapp:{os.getenv('TWILIO_WPP_NUMBER')}',
            body=msg,
            to=f'whatsapp:{os.getenv('MY_WPP_NUMBER')}'
        )
