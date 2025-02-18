import requests
from datetime import datetime
from mail_manager import MailManager

MY_LAT = 00.00  # Your latitude
MY_LONG = 00.00  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
mail_manager = MailManager(sender="YOUR MAIL", password="YOUR PASSWORD")

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

def send_alert():
    mail_manager.send(to="RECEIVER EMAIL", subject=f"ISS Alert", content="Hey! check outside now. ISS is passing.")


# Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead(city_latitude, city_longitude, iss_lat, iss_long, tolerance=5):
    min_latitude = city_latitude - tolerance
    max_latitude = city_latitude + tolerance
    min_longitude = city_longitude - tolerance
    max_longitude = city_longitude + tolerance

    if min_latitude <= iss_lat <= max_latitude and min_longitude <= iss_long <= max_longitude:
        return True
    else:
        return False


def is_night(sun_set, sun_rise):
    time_now = datetime.now()
    hour = time_now.hour
    if sun_set <= hour <= 24 or 0 <= hour <= sun_rise:
        return True
    return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
is_iss_passed = is_iss_overhead(city_latitude=MY_LAT, city_longitude=MY_LONG, iss_lat=iss_latitude,
                                iss_long=iss_longitude)
night = is_night(sun_set=sunset, sun_rise=sunrise)
if is_iss_passed and night:
    send_alert()