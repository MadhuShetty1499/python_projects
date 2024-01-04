#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

sheet_data = DataManager()
flight_search = FlightSearch()
notification = NotificationManager()

for row in sheet_data.retrieve_data():
    if row["iataCode"] == '':
        row["iataCode"] = flight_search.get_iata_code(row["city"])

# sheet_data.update_data()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6*30))

origin_city_IATA = "LON"

for destination in sheet_data.retrieve_data():
    flight = flight_search.check_flights(
        origin_city_code=origin_city_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification.send_sms(
            price=flight.price,
            origin_city=flight.origin_city,
            origin_city_code=flight.origin_airport,
            destination_city=flight.destination_city,
            destination_city_code=flight.destination_airport,
            from_date=flight.out_date,
            to_date=flight.return_date
        )

