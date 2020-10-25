import sys
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

if sys.version_info[0] == 2:
    from email.MIMEBase import MIMEBase
elif sys.version_info[0] == 3:
    from email.mime.base import MIMEBase

def send_email(
        recipients,
        subject,
        text,
        attachments=[],
        sender,
        password
    ):

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))

    for file in attachments: # get all attachments
        filename = file.split('/')[-1]
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(file, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % filename)
        msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(sender, password) # change it if you change the sender address
    mailServer.sendmail(sender, recipients, msg.as_string())
    mailServer.close()