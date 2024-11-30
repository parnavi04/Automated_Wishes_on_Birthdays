##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
# 1. Update the birthdays.csv
data_dict = {}
data = pandas.read_csv("Birthdays.csv")
name = data["name"].tolist()
email = data["email"].tolist()
year = data["year"].tolist()
month = data["month"].tolist()
day = data["day"].tolist()

for i in range(len(name)):
    data_dict[i] = [name[i], email[i], year[i], month[i], day[i]]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

def send(key):
    file_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    with open(random.choice(file_list)) as file:
        data = file.read()
        value = data_dict[key]
        new_data = data.replace("[NAME]", value[0])
        return new_data

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month
year = now.year
position = None
found = False
for key, value in data_dict.items():
    if value[4] == day and value[3] == month:
        found = True
        position = key

body = send(position)


# 4. Send the letter generated in step 3 to that person's email address.
my_email = "pumpkinslay8@gmail.com"
password = "crfggipymjqvtsdm"
to_value = data_dict[position]
to_address = to_value[1]
with smtplib.SMTP("smtp.gmail.com", 587) as connection: # this is the server for g-mail establishes connection with server
    connection.starttls()  # secures the connection with server
    connection.login(user= my_email, password= password)   # login into your gmail account
    connection.sendmail(from_addr= my_email,
                        to_addrs= to_address,
                        msg= f"Subject: Happy Birthday \n\n{body}")




