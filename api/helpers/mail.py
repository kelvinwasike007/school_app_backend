import smtplib, ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from dotenv import load_env
import os

load_env()
def sendMail(recipients, message, subject):
    server = "mail.wesempire.co.ke"
    username = os.genenv("EMAIL")
    password = os.getenv("EMAIL_PASS")
    port = 465
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = username
    msg['To'] = recipients[0]
    msg.attach(MIMEText(message, 'plain'))
    ctx = ssl.create_default_context()
    mail = smtplib.SMTP_SSL(server, port, context=ctx)
    try:
        mail.login(username, password)
        mail.sendmail(username, recipients, msg=msg.as_string())
        return 'sent'
    except smtplib.SMTPException:
        return 'failed'

def signup_mail(to, domain ,account):
    payload = {
        'message': f"""\
            Thank you for choosing School-Platform By WesEmpire\
            Your School Domain is {domain} \
            The Adminstrator Account Credentials are: \
            USERNAME:{account["username"]} \
            PASSWORD: {account["password"]} \

            PLEASE CHANGE THIS PASSWORD AFTER YOU HAVE LOGGED IN
            """,
    }

    return sendMail(to, payload, 'NEW SIGN UP SETUP')
