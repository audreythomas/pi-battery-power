#!/usr/bin/env python2.7
import os
import time
from time import gmtime, strftime
import sendgrid
from sendgrid.helpers.mail import *

def write_log(logline):
  logfile = open('battery_log.txt', 'a')
  logfile.write(logline + '\n')
  logfile.close()

def send_email(logline):
  sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
  from_email = Email("elmer@thinkingserious.com")
  subject = "Science Project: Test 4"
  to_email = Email("elmer.thomas+science2@gmail.com")
  content = Content("text/plain", logline)
  mail = Mail(from_email, subject, to_email, content)
  try:
    response = sg.client.mail.send.post(request_body=mail.get())
    print "email sent with status code %s" % str(response.status_code)
  except:
    print "problem sending email"

item = 'Battery log data'
logfile = open('battery_log.txt', 'w')
logfile.write(item + '\n')
logfile.close()

while True:
  logline = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
  print "adding %s to log file" % logline
  write_log(logline)
  send_email(logline)
  time.sleep(60)
