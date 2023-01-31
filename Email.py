#program have errors

import smtplib #to send data via email
import base64 #to encode data to be sent via email
s = "anyone@gmail.com"
r = "anyother@gmail.com"
m = '''From: <anyone@gmail.com>
To: <anyother@gmail.com>
Subject: SMTP email test

Yoo.
'''
try:
    smtobj = smtplib.SMTP('localhost')
    smtpobj.sendmail(s , r , m)
    print("Sent Sucessfully")
except:
    print("Unable to send")