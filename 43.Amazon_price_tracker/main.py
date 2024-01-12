import requests
from bs4 import BeautifulSoup
import smtplib
import os

USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0"
              " Safari/537.36 Edg/120.0.0.0")
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
URL = "https://www.amazon.in/dp/B07WHR5ZG7/ref=twister_B0BSSQ6YMX"
FROM_EMAIL = os.environ.get("FROM_EMAIL")
PASSWORD = os.environ.get("EMAIL_PASSWORD")
TO_EMAIL = os.environ.get("EMAIL")

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE,
}

response = requests.get(URL, headers=headers)
website = response.text

soup = BeautifulSoup(website, "html.parser")
price_whole = soup.find(class_="a-offscreen")
price = float(price_whole.text.split("₹")[1].replace(",", ""))
target_price = 23000.00
title = soup.select("div h1 span")[0].text

if price < target_price:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=FROM_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
