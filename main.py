import smtplib

my_email = "pumpkinslay8@gmail.com"
password = "crfggipymjqvtsdm"
with smtplib.SMTP("smtp.gmail.com", 587) as connection:   # this is the server for g-mail establishes connection with server
    connection.starttls()  # secures the connection with server
    connection.login(user= my_email, password= password)   # login into your gmail account
    connection.sendmail(from_addr= my_email,
                        to_addrs= "parnavisalunke50026040@gmail.com",
                        msg= "Subject: Hello \n\nHow U Doin??")
