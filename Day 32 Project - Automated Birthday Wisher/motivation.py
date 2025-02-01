#Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "frank.imagination@gmail.com"
MY_PASSWORD = "owrtiweonmoglxjh"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt", encoding="utf8") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs= "frankenstein.tran2@gmail.com",
            msg=f"Subject:Birthday Motivation\n\n{quote}".encode("utf8")
        )