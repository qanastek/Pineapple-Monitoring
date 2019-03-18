# -*- coding: utf-8 -*-

import smtplib

# String sujet Sujet du mail
# String msg Contenue du mail

# The mail is send in IssueDetector
def SendEmail(sujet, msg):

	smtp_server = "smtp.gmail.com"
	port = 587

	sender_email = "qanastek@gmail.com"
	password = "hhfppcclexrcvcxq"

	recipient = ["yanis.labrak@alumni.univ-avignon.fr"]
	receiver_email = recipient if isinstance(recipient, list) else [recipient]

	subject = sujet
	content = msg + "\n\nSend by Pineapple-Monitoring.\nMade by Labrak Yanis & Vougeot Valentin"

	message = """ From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (sender_email, ", ".join(receiver_email), subject, content)
	
	mail = smtplib.SMTP(smtp_server, port)

	mail.ehlo()

	mail.starttls()

	mail.login(sender_email, password)

	mail.sendmail(sender_email, receiver_email, message)

	mail.close()