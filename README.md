# Companion Code to "Battery Power in the Refridgerator"

This is a sixth grade science project that measures battery power over time on a Raspberry Pi.

The code will log a timestamp every 60 seconds and send an email. Once you stop receiving emails, you will know the Raspberry Pi has run out of battery power. You can then check the log file to determine how long the Raspberry Pi was running.

1. Get a free [SendGrid](https://sendgrid.com/) account.
2. Create a `sendgrid.env` file
3. Add the following to that file:
`export SENDGRID_API_KEY=YOUR_API_KEY_GOES HERE`
4. Change the email addresses in the code to be your own
5. `python app.py`
