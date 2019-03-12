# -*- coding: utf-8 -*-

import smtplib

smtp_server = "smtp.gmail.com"
port = 587

sender_email = "qanastek@gmail.com"
password = "###"

recipient = ["yanis.labrak@alumni.univ-avignon.fr"]
receiver_email = recipient if isinstance(recipient, list) else [recipient]

subject = "Le sujet"
content = "Mon message"

message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (sender_email, ", ".join(receiver_email), subject, content)

mail = smtplib.SMTP(smtp_server, port)

mail.ehlo()

mail.starttls()

mail.login(sender_email, password)

mail.sendmail(sender_email, receiver_email, message)

mail.close()