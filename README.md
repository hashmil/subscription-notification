# Subscriptions Expiry Email Reminder

A simple python script that reminds me when a subscription product is about to expire.

I made this because I keep forgetting when I need to cancel something that I subecribed to.

![Screenshot of email](https://i.imgur.com/aX5z3Yc.png)

## Setup

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

## Running it every 24 hours

If you need to run it every 24 hours, here's how to do it on a Mac. (Sorry Win/Linux, you may have to google this)

1. Edit the `com.subs.notifs.plist` so that the path of the app is pointing it where you have saved. There will be comments within the code indicating where this should be updated.
2. Copy the `com.subs.notifs.plist` file into `~/Library/LaunchAgents/`
3. Load the plist into launchd with the following command on Terminal
   ```
   launchctl load ~/Library/LaunchAgents/com.subs.subs-notifs.plist
   ```
4. Verify that the script is running by checking the log files specified in the `StandardErrorPath` and `StandardOutPath` keys. You can also check the script is running with the following command;
   ```
   launchctl list | grep subs-notifs
   ```
