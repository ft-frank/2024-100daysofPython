import requests
import smtplib

API_KEY = "c4e2b28d14048e9d76377bafb70546b3"
MY_EMAIL = "frank.imagination@gmail.com"
MY_PASSWORD = "owrtiweonmoglxjh"

#Response for next 12 hours
response= requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=-34&lon=151&appid=c4e2b28d14048e9d76377bafb70546b3&cnt=4")
response.raise_for_status()
data = response.json()

umbrella = None
for x in range(0, 4):
    description = data['list'][x]['weather'][0]['id']
    if int(description) < 700:
        umbrella = True

if umbrella == True:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="frankenstein.tran2@gmail.com",
            msg="BRING UMBRELLA GANG")
else:
    ()
