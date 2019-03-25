# -*- coding: utf-8 -*-

import smtplib
import json

# String sujet Sujet du mail
# String msg Contenue du mail

# The mail is send in IssueDetector
def SendEmail(sujet, msg):

	with open("mail.json", "r") as read_file:

			infos = json.load(read_file)

	smtp_server = infos['addresse']

	port = infos['port']

	sender_email = infos['senderMail']

	password = infos['password']

	recipient = ["yanis.labrak@alumni.univ-avignon.fr"]
	receiver_email = recipient if isinstance(recipient, list) else [recipient]

	subject = sujet
	content = msg + "\n\n" + infos['signature']

	message = """ From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (sender_email, ", ".join(receiver_email), subject, content)
	
	mail = smtplib.SMTP(smtp_server, port)

	mail.ehlo()

	mail.starttls()

	mail.login(sender_email, password)

	mail.sendmail(sender_email, receiver_email, message)

	mail.close()