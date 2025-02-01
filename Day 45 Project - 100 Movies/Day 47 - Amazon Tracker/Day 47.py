import requests
from bs4 import BeautifulSoup
import smtplib


URL = "https://www.amazon.com.au/Doorway-Thickened-Multi-Grip-Strength-Portable/dp/B0CSYZDQS4/ref=sr_1_5?crid=3GTY83O13C7VA&dib=eyJ2IjoiMSJ9.YcN45l1WvhGXlhHWwOPJcpqDsHp7ovVoetNGXi7GRYv4gPmVXTtr9d5gCBQAro76DC8b0KtntZJqLZ49CW9h2CApikdZe2QxJaQQIlDY2Ck_Wlv5_a-NGZyChGAVx_qzgyUCKhGK1YVBL_LPeglFa8Ei1sDTdqdo5CuzdRHeneMLF058FGYyjwpd7KYRGnTIajydVQOsMyT3erBTsg4PqVfEfip8DtaF5Mq3FvC514-SMopRXpFgcM96WoLc5DIuo_o19a0U3h0VpdWcpd1NTLC3XfFznU7A2mYZIsook98.tqxIKfTVUTy2lhbMLIgrZ-8mlSx4KDH5bqwjm98nuD4&dib_tag=se&keywords=pull+up+bar&qid=1711090606&sprefix=pull+up+%2Caps%2C296&sr=8-5"
MY_EMAIL = "frank.imagination@gmail.com"
MY_PASSWORD = "owrtiweonmoglxjh"
# Write your code below this line 👇

response = requests.get(f"{URL}")
page = response.text


soup = BeautifulSoup(page, "html.parser")
# print(soup)
price = soup.find(name = 'span', class_ = "a-offscreen").text
price = float(price[1:])
if price < 20:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg= f"ONLY 20 DOLLARS: {URL}"
        )

