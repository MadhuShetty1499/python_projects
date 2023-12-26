import requests
from twilio.rest import Client

api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "<Your api key>"
lattitude = -9.604860
longitude = 27.590690

parameters = {
    "lat": lattitude,
    "lon": longitude,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(api_endpoint, params=parameters)
response.raise_for_status()
data = response.json()
weather_list = data["list"]
is_rain = False

account_sid = "<your account_sid>"
auth_token = "<your auth token>"
client = Client(account_sid, auth_token)

for n in weather_list:
    weather_id = n["weather"][0]["id"]
    if weather_id < 700:
        is_rain = True

message = client.messages.create(
        from_="<from mob number>",
        body="It's going to rain today, bring an umbrella☔",
        to="<to mob  number>"
    )

if is_rain:
    print(message)