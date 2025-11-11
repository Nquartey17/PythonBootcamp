import smtplib

#Using fake credentials, code will have errors

my_email = "test@gmail.com"
password = "test123"

with smtplib.SMTP("stmp.gmail.com") as connection: #Use to automatically close file after use
    connection.starttls() #secure connection
    connection.login(user=my_email, password=password) #login to email
    connection.sendmail(from_addr=my_email,
                        to_addrs="sample@yahoo.com", msg="Subject:Hello\n\nThis is the body of the email") #send mail
    connection.close() # close message