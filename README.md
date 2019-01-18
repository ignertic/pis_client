# Bluedot-sms unofficial API

This is an unofficial API for [Bluedot-sms](http://bluedotsms.com)

Requirements:
  paynow
  Python 3

Installation:
  pip install paynow
  pip install pybluedot

Usage

from pybluedot import Bluedot
client = Bluedot(acc_token, sec_token)

#send SMS
msg = "Hey There"
client.set_sender_name("Me") //set sender name (optional) default will be used if not set
resp = client.send_sms(msg, "26312345678")
//check if successful
if resp.success:
  //check balance
  stats = resp.content
  for key, value in stats.items():
    print key + " : " + value
else:
  resp.error_code

#broadcasting sms
msg = "Don't be late for the meeting"
contacts = ["0912736772", "123457656", "23465554"]
resp = client.brodcast_sms(contacts, msg, sender_name="Me")
if resp.success:
  stats=resp.content
