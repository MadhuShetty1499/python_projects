import os
import requests
from flight_data import FlightData

TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
header = {
    "apikey": TEQUILA_API_KEY,
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_iata_code(self, city):
        data = {
            "term": city,
            "location_types": "city",
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", headers=header, params=data)
        code = response.json()["locations"][0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 8,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=parameters)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            origin_airport=data["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["flyTo"],
            out_date=data["local_departure"].split("T")[0],
            return_date=data["local_arrival"].split("T")[0],
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
