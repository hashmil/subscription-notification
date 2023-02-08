# Subscriptions Expiry Email Reminder

A simple python script that reminds me when a subscription product is about to expire.

I made this because I keep forgetting when I need to cancel something that I subecribed to.

Update the `subscriptions.xlsx` file with your subscriptions and the expiry date. Run the script, and you will get an email 7 days before a product expires.

Make sure to create a `config.ini` file and include:

```
[email]
address = sender_email_address
password = sender_email_password

[recipient]
address = recipient_email_address
```

## Notes

- Email should be a gmail address
- Set up 2 factor authentication, and then in the Security Settings in Google create an app password to use.
