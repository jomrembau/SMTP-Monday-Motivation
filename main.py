import random
import smtplib
import datetime as dt

email = "enter_email_here"
password = "enter_your_app_password_here"

quotes_list = []

with open('quotes.txt', "r", encoding="utf-8") as f:
    datafile = f.readlines()
    for line in datafile:
        quotes_list.append(line)

random_quote = random.choice(quotes_list)

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
now = dt.datetime.now()
message = f"Subject: Happy Monday\n\n{random_quote}"

connection.login(user=email,password= password)
if now.weekday() == 0:
    connection.sendmail(from_addr=email,
                        to_addrs="jomir.bautista@gmail.com",
                        msg= message.encode("utf-8"))

connection.close()