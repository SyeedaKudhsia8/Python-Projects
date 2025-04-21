import smtplib as sm
import datetime as dt
import random
import os

MY_EMAIL = "skudhsia@gmail.com"
PASSWORD = os.environ.get("password")

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    with sm.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: Monday Motivation\n\n{quote}"
                            )



















