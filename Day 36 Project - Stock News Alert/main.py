import requests
import datetime
import smtplib

#INITIALISATION
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

MY_EMAIL = "frank.imagination@gmail.com"
MY_PASSWORD = "owrtiweonmoglxjh"






## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=UO4JWY5O58PLWGYZ")
response.raise_for_status()
data = response.json()

# #CREATING DATES TO BE USED
today = datetime.datetime.today().date()
yesterday = today - datetime.timedelta(days=1)
day_before_yesterday = today - datetime.timedelta(days=2)

x = 0
while f'{yesterday}' not in data['Time Series (Daily)']:
    x += 1
    yesterday = today - datetime.timedelta(days = x)
while f'{day_before_yesterday}' not in data['Time Series (Daily)']:
    x += 1
    day_before_yesterday = today - datetime.timedelta(days = x)

yesterday_close = float(data['Time Series (Daily)'][f'{yesterday}']['4. close'])
day_before_yesterday_close = float(data['Time Series (Daily)'][f'{day_before_yesterday}']['4. close'])
difference = abs(yesterday_close - day_before_yesterday_close)

if difference >= 0.05 * yesterday_close:
    news = requests.get("https://newsapi.org/v2/everything?q=Tesla&apiKey=caa015cc9f614c4b98f744b944a52cd0&language=en&pageSize=3")
    news.raise_for_status()
    news = news.json()
    articles = news['articles']


    email = [(f"{articles[x]['title']}\n"
              f"{articles[x]['url']}\n") for x in range(0,3)]

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="frankenstein.tran2@gmail.com",
            msg= f"Subject:TESLA STOCK ALERT!!\n\n{(''.join(email))}")



