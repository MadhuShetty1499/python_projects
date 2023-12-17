import random
import pandas
import datetime as dt
import smtplib

data = pandas.read_csv("birthdays.csv")
dict = data.to_dict(orient="records")

now = dt.datetime.now()
letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
for n in dict:
    if n["month"] == now.month and n["day"] == now.day:
        letter = random.choice(letters)
        with open(letter, mode='r') as file:
            lett = file.read()
            replaced_lett = lett.replace("[NAME]", n["name"])
        from_address = <your email>
        password = <your app password>
        to_address = n["email"]
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=from_address, password=password)
            connection.sendmail(
                from_addr=from_address,
                to_addrs=to_address,
                msg=f"Subject:Birthday Greetings!!\n\n{replaced_lett}"
            )
    else:
        print("None of them have Birthday today!!")



