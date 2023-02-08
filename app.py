import smtplib
import pandas as pd
from email.mime.text import MIMEText
import configparser
from datetime import datetime, timedelta


def send_email(product, expiry_date):
    config = configparser.ConfigParser()
    config.read("config.ini")

    address = config["email"]["address"]
    password = config["email"]["password"]
    to_address = config["recipient"]["address"]

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(address, password)

    subject = f"Subscription Reminder: {product}"
    body = f"Your {product} subscription will expire on {expiry_date}. Please renew it soon."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = address
    msg["To"] = to_address

    server.send_message(msg)
    print("Email sent successfully!")
    server.quit()


def main():
    df = pd.read_excel("subscriptions.xlsx")
    today = datetime.now().date()
    for index, row in df.iterrows():
        product = row["Product"]
        expiry_date = row["Expiry Date"]
        expiry_date = expiry_date.date()
        days_until_expiry = (expiry_date - today).days
        if days_until_expiry == 7:
            send_email(product, expiry_date)


if __name__ == "__main__":
    main()
