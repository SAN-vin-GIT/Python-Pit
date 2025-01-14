import smtplib
import datetime as dt
import random

# Your email credentials
my_email = "sangeet.himire@gmail.com"
password = "enter_your_custom_app_password"

# Grabbing the current date
now = dt.datetime.now()

# Grabbing a random quote from the list
with open('quotes.txt', 'r') as file:
    quotes = [line.strip() for line in file]
random_quote = random.choice(quotes)

# Reading email addresses from the file
with open('emails.txt', 'r') as email_file:
    email_list = [email.strip() for email in email_file]

# Sending an automated email
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()  # Start TLS encryption
    connection.login(user=my_email, password=password)  # Login to your email account

    for recipient in email_list:
        subject = "Your Daily Dose of Motivation from Sangit"
        body = f"Quote of the Day: {random_quote} \nThis is an automated email generated by a Python program I developed. From today onward, you’ll receive a daily dose of motivation, as this program delivers an inspiring quote to brighten your day. Stay tuned!"

        # Creating the email message
        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=message.encode('utf-8')  # Ensure proper encoding
        )
