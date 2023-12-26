import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCKS_API_KEY = os.environ.get("STOCKS_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
STOCK_URL = "https://www.alphavantage.co/query"
NEWS_URL = "https://newsapi.org/v2/everything"
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
FROM_NUMBER = os.environ.get("FROM_NUMBER")
TO_NUMBER = os.environ.get("TO_NUMBER")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCKS_API_KEY,
    "outputsize": "compact",
}

response_stock = requests.get(STOCK_URL, params=stock_parameters)
response_stock.raise_for_status()
stock_data = response_stock.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
yesterday_closing_price = float(stock_data_list[0]["4. close"])
day_before_yesterday_closing_price = float(stock_data_list[1]["4. close"])
difference = round(day_before_yesterday_closing_price - yesterday_closing_price, 2)
percentage = round(difference / yesterday_closing_price * 100, 2)
if percentage > 0:
    symbol = "🔺"
else:
    symbol = "🔻"

if abs(percentage) > 0.1:
    new_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "searchIn": "title"
    }
    response_news = requests.get(NEWS_URL, params=new_parameters)
    news_data = response_news.json()["articles"]
    three_articles = news_data[:3]
    formatted_articles = [(f"{STOCK}: {symbol}{percentage}%\nHeadline: {article['title']}. "
                           f"\nBrief: {article['description']}")for article in three_articles]

    account_sid = ACCOUNT_SID
    auth_token = AUTH_TOKEN
    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
          from_=FROM_NUMBER,
          to=TO_NUMBER,
          body=article,
        )
        print(message.sid)
