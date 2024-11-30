import random
import smtplib
import datetime as dt
with open("quotes.txt") as file:
    data = file.readlines()

quote_of_day = random.choice(data)

def send_mail():
    my_email = "pumpkinslay8@gmail.com"
    password = "crfggipymjqvtsdm"
    to_address = "parnavisalunke50026040@gmail.com"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user= my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs= to_address, msg = f"Subject: Happy Monday\n\n{quote_of_day}")


date = dt.datetime.now()
if date.weekday() == 4:
    send_mail()

