import requests

SHEETY_ENDPOINT = "<Your sheety api endpoint>"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
    def retrieve_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        sheety_data = response.json()
        self.destination_data = sheety_data["prices"]
        return self.destination_data

    def update_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city["id"]}", json=new_data)
            print(response.text)


