import smtplib, random
import datetime as dt

#Challenge: If day of the week is equal to Tuesday, send motivational quote to self

my_email = "test@gmail.com"
password = "test123"

now = dt.datetime.now()
day_of_week = now.weekday() #Counts from 0, Monday would be 0

if day_of_week == 1:
    with open('quotes.txt') as file:
        lines = file.read().splitlines()
    quote = random.choice(lines)
    print(quote)

    with smtplib.SMTP("stmp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Motivational Quote\n\n{quote}")
