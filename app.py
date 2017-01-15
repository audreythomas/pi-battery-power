#!/usr/bin/env python2.7
import os
import time
from time import gmtime, strftime
import sendgrid
from sendgrid.helpers.mail import *

# Write (append) messages to a file called battery_log.txt
def write_log(logline):
  logfile = open('battery_log.txt', 'a')
  logfile.write(logline + '\n')
  logfile.close()

# Send an email
# NOTE: Be sure to change the from_email and to_email addresses
def send_email(logline):
  sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
  from_email = Email("test@example.com")
  subject = "Science Project: The Raspberry Pi is Still Alive!"
  to_email = Email("test@example.com")
  content = Content("text/plain", logline)
  mail = Mail(from_email, subject, to_email, content)
  try:
    response = sg.client.mail.send.post(request_body=mail.get())
    print "email sent with status code %s" % str(response.status_code)
  except:
    print "problem sending email"

# Open a log file and write the title
title = 'Battery Log Data'
logfile = open('battery_log.txt', 'w')
logfile.write(title + '\n')
logfile.close()

# Run the program until the Raspberry Pi runs out of battery power
while True:
  log_time = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
  message = "The Rasberry Pi is still alive at: %s" % log_time
  # Print the message to the console screen
  print(message)
  # Write the message to our battery_log.txt file
  write_log(message)
  # Send an email with our message
  send_email(message)
  # Wait for 1 minute
  time.sleep(60)
