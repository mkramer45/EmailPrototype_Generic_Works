import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

msg = MIMEMultipart()
msg['From'] = 'mkramer265@gmail.com'
msg['To'] = 'mkramer789@gmail.com'
msg['Subject'] = 'simple email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('mkramer265@gmail.com', 'Celtics123')

mailserver.sendmail('mkramer265@gmail.com','mkramer789@gmail.com',msg.as_string())

mailserver.quit()