import smtplib
import requests
from datetime import datetime

# this is a notifier that notifies you if International Space Station is above your head at night just add your latitude and longitude and change your email details,
# after that you can put this code on while loop and integrate time module that checks every 5 minutes if ISS is overhead.

MY_LAT = 28.044727
MY_LNG = 82.486756

my_email = "sangeet.himire@gmail.com"
password = "your app password "


def is_above():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "time_format" : 24,
    }

    response = requests.get("https://api.sunrisesunset.io/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split(":")[0])
    sunset = int(data["results"]["sunset"].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True



if is_above() and is_night():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email,password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=password,
        msg = "Subject: Look Up ISS is Above You ⬆🚀 \n\n The international space station is above your Head. Is'nt it cool "
    )
