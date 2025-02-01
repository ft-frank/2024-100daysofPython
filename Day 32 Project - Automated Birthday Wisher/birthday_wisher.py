##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import smtplib
import random
#provides values for my email and its password
MY_EMAIL = "frank.imagination@gmail.com"
MY_PASSWORD = "owrtiweonmoglxjh"

#create a dictionary of emails and birthday
birthdays = pandas.read_csv("birthdays.csv")
birthday_df = pandas.DataFrame(birthdays)
birthday_dict ={row.first_name: [(row.month, row.day), row.email] for (index, row) in birthday_df.iterrows()}

#attaches values to the current date
month = dt.datetime.now().month
day = dt.datetime.now().day

#checks if there is a birthday today and adds to a list of emails to be sent
today = False
people = []
for key in birthday_dict:
    if (month, day) == birthday_dict[key][0]:
        today = True
        people.append(key)


if today:
    for people in people:
        print(people)
        #creates message:
        with open(f"letter_{random.randint(1,3)}.txt") as letter:
            letterdata = letter.read()
            letterdata = letterdata.replace("[NAME]", people)


        with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs= birthday_dict[people][1],
                msg = f"Subject: HAPPY BIRTHDAY\n\n {letterdata}"
            )