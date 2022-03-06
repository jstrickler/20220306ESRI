#!/usr/bin/env python
import smtplib
from datetime import datetime
from imghdr import what  # <1>
from email.message import EmailMessage # <2>
from getpass import getpass # <3>


SMTP_SERVER = "smtp2go.com"  # <4>
SMTP_PORT = 2525

SMTP_USER = 'pythonclass'

SENDER = 'jstrick@mindspring.com'
RECIPIENTS = ['jstrickler@gmail.com']


def main():
    smtp_server = create_smtp_server()
    now = datetime.now()
    msg = create_message(
        SENDER,
        RECIPIENTS,
        'Here is your attachment',
        'Testing email attachments from python class at {}\n\n'.format(now),
    )
    add_text_attachment('../DATA/parrot.txt', msg)
    add_image_attachment('../DATA/felix_auto.jpeg', msg)
    send_message(smtp_server, msg)


def create_message(sender, recipients, subject, body):
    msg = EmailMessage()  # <5>
    msg.set_content(body)  # <6>
    msg['From'] = sender
    msg['To'] = recipients
    msg['Subject'] = subject
    return msg


def add_text_attachment(file_name, message):
    with open(file_name) as file_in:  # <7>
        attachment_data = file_in.read()
    message.add_attachment(attachment_data)  # <8>


def add_image_attachment(file_name, message):
    with open(file_name, 'rb') as file_in:  # <9>
        attachment_data = file_in.read()
    image_type = what(None, h=attachment_data)  # <10>
    message.add_attachment(attachment_data, maintype='image', subtype=image_type)  # <11>


def create_smtp_server():
    password = getpass("Enter SMTP server password:")  # <12>
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)  # <13>
    smtpserver.login(SMTP_USER, password)  # <14>

    return smtpserver


def send_message(server, message):
    try:
        server.send_message(message)  # <15>
    finally:
        server.quit()


if __name__ == '__main__':
    main()
