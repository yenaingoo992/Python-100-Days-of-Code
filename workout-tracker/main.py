import requests
from datetime import datetime
import os

NUTRITIONX_BASE_URL = "https://trackapi.nutritionix.com"
APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
KEY = os.environ.get("NUTRITIONIX_KEY")
SHEETY_USER_NAME = os.environ.get("SHEETY_USER_NAME")
SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": KEY,
}
exercise_endpoints = f"{NUTRITIONX_BASE_URL}/v2/natural/exercise"
exercise_configs = {
    "query": input("Tell me which exercise you did: ")
}

response = requests.post(url=exercise_endpoints, json=exercise_configs, headers=headers)

json_data = response.json()
exercise = json_data["exercises"][0]

now = datetime.now()
date = now.date().strftime("%d/%m/%Y")
time = now.time().strftime("%H:%M:%S")

sheety_endpoints = "https://api.sheety.co/a87955762cbed93ca5999afb7aced155/myWorkouts/workouts"

sheety_headers = {
    "content-type": "application/json"
}

workout_configs = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise["user_input"].title(),
        "duration": f"{exercise['duration_min']}",
        "calories": exercise["nf_calories"]
    }
}

workout_response = requests.post(
    url=sheety_endpoints,
    json=workout_configs,
    headers=sheety_headers,
    auth=(SHEETY_USER_NAME, SHEETY_PASSWORD))
