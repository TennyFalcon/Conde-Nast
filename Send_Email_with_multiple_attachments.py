import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import os

msg = MIMEMultipart()
sender_email_addr = 'tennyfalcon444@gmail.com'
receiver_email_list = ['tennyfalcon444@gmail.com','tennyson_paul@condenast.com']
msg['From'] = sender_email_addr
msg['To'] = ", ".join(receiver_email_list)
msg['Subject'] = 'L2C - Data Validation Failed'

#email content
message = 'This is the body'

msg.attach(MIMEText(message, 'html'))
files = ['/Users/tenny/Desktop/L2C/Output files/India/India_Validation_Results.xls',
         '/Users/tenny/Desktop/L2C/Output files/China/China_Validation_Results.xls']

files = []
if os.path.exists('/Users/tenny/Desktop/L2C/Output files/India/India_Validation_Results.xls'):
    files.append('/Users/tenny/Desktop/L2C/Output files/India/India_Validation_Results.xls')

print(files)

for a_file in files:
    attachment = open(a_file, 'rb')
    file_name = os.path.basename(a_file)
    part = MIMEBase('application','octet-stream')
    part.set_payload(attachment.read())
    part.add_header('Content-Disposition',
                    'attachment',
                    filename=file_name)
    encoders.encode_base64(part)
    msg.attach(part)

#sends email

smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
smtpserver.starttls()

# Authentication
smtpserver.login(sender_email_addr, "Tenny@444")
smtpserver.sendmail(sender_email_addr, receiver_email_list, msg.as_string())
smtpserver.quit()

print('completed')