#!/usr/bin/env python
from getpass import getpass  # <1>
import smtplib  # <2>
from email.message import EmailMessage  # <3>
from datetime import datetime

TIMESTAMP = datetime.now().ctime()  # <4>

SENDER = 'jstrick@mindspring.com'
RECIPIENTS = ['jstrickler@gmail.com']
MESSAGE_SUBJECT = 'Python SMTP example'

MESSAGE_BODY = """
Hello at {}.

Testing email from Python
""".format(TIMESTAMP)

SMTP_USER = 'pythonclass'
SMTP_PASSWORD = getpass("Enter SMTP server password:")  # <5>

smtpserver = smtplib.SMTP("smtp2go.com", 2525)  # <6>
smtpserver.login(SMTP_USER, SMTP_PASSWORD)  # <7>

msg = EmailMessage()  # <8>
msg.set_content(MESSAGE_BODY)  # <9>
msg['Subject'] = MESSAGE_SUBJECT  # <10>
msg['from'] = SENDER  # <11>
msg['to'] = RECIPIENTS  # <12>

try:
    smtpserver.send_message(msg)  # <13>
except smtplib.SMTPException as err:
    print("Unable to send mail:", err)
finally:
    smtpserver.quit()  # <14>
