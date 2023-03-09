import smtplib, ssl, imaplib, time
from webchecker import *

def mailer():
    r1 = ring1()
    r2 = ring2()
    r3 = ring3()
    r4 = ring4()


    if r1 == True:
        message = f"""From: {sender_email}
To: {reciever_email}

The bus will reach the stop in 10 minutes, get ready. """

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.set_debuglevel(1)
            server.login(sender_email, password)
            server.sendmail(sender_email, reciever_email, message)

    elif r2 == True:
        message = f"""From: {sender_email}
To: {reciever_email}

The bus will reach the stop in 8 minutes. """

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.set_debuglevel(1)
            server.login(sender_email, password)
            server.sendmail(sender_email, reciever_email, message)

    elif r3 == True:
        message = f"""From: {sender_email}
To: {reciever_email}

The bus will reach the stop in 5 minutes, leave now. """

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.set_debuglevel(1)
            server.login(sender_email, password)
            server.sendmail(sender_email, reciever_email, message)

    elif r4 == True:
        message = f"""From: {sender_email}
To: {reciever_email}

The bus will reach the stop in 2 minutes, run to the bus! """

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.set_debuglevel(1)
            server.login(sender_email, password)
            server.sendmail(sender_email, reciever_email, message)