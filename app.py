import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

address = config["email"]["address"]
password = config["email"]["password"]
recipient = config["recipient"]["address"]


def send_email(product_list):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    msg = MIMEMultipart()
    msg['From'] = address
    msg['To'] = recipient
    msg['Subject'] = "Subscriptions expiring soon"
    body = "The following subscriptions are expiring within the next 7 days: \n\n"
    for product in product_list:
        body += f"{product}\n"
    msg.attach(MIMEText(body, 'plain'))

    server.login(address, password)
    text = msg.as_string()
    server.sendmail(address, recipient, text)
    print("Email sent!")
    server.quit()


def main():
    today = datetime.now().date()
    df = pd.read_excel("subscriptions.xlsx")
    product_list = []
    for index, row in df.iterrows():
        expiry_date = row['Expiry Date'].date()
        if (expiry_date - today).days <= 7:
            product_list.append(row['Product'])
    if product_list:
        send_email(product_list)
    else:
        print("No subscriptions expiring within the next 7 days.")


if __name__ == "__main__":
    main()
