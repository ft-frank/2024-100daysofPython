import requests
from datetime import datetime
import smtplib
import time
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


MY_EMAIL = "frank.imagination@gmail.com"
MY_PASSWORD = "owrtiweonmoglxjh"



MY_LAT = -33.908211# Your latitude
MY_LONG = 150.886872 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


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
hour = datetime.now().hour

def isnear():
    if abs(iss_latitude - MY_LAT) <= 5:
        if abs(iss_longitude - MY_LONG) <= 5:
            if hour <= sunrise or hour >= sunset:
                return True


def email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="frankenstein.tran2@gmail.com",
        msg= "Subject:ISS!\n\nLook up Cuz")
while True:
    time.sleep(60)
    if isnear():
        email()