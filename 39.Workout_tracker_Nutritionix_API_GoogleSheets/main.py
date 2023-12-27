import os
import requests
from datetime import datetime

NUTRITIONIX_ID = os.environ.get("NUTRITIONIX_ID")
NUTRITIONIX_API = os.environ.get("NUTRITIONIX_API")
SHEETY_AUTH_TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")
GENDER = <your gender>
AGE = <your age>
HEIGHT_CM = <your height>
WEIGHT_KG = <your weight>

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_api_endpoint = "https://api.sheety.co/646d03120bcc87b2b47ad6e35990337c/workoutTracker/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_API,
}

nutritionix_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=nutritionix_endpoint, headers=headers, json=nutritionix_params)
result = response.json()

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")
header = {
    "Authorization": SHEETY_AUTH_TOKEN,
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
            "exercise": exercise["name"].title(),
        }
    }
    sheety_response = requests.post(url=sheety_api_endpoint, json=sheet_inputs, headers=header)
    print(sheety_response.text)
