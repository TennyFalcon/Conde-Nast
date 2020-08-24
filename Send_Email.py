# Python code to illustrate Sending mail from
# your Gmail account
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("tennyfalcon444@gmail.com", "Tenny@444")

# message to be sent
message = "Mail from python"

# sending the mail
s.sendmail("tennyfalcon444@gmail.com", "tennyfalcon444@gmail.com", message)

# terminating the session
s.quit()

print('completed')