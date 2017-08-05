import smtplib # simple mail transfer protocol

conn = smtplib.SMTP('smtp.gmail.com', 587) # server and port aka domain name

conn.ehlo() # starts connection

conn.starttls() # starts TLS encription for login
# can make app specific password
conn.login('email@address.com', 'password')
# if you want a subject must put Subject: name \n\n + body of email
conn.sendmail('From address(yours)', 'to.address.com', 'Subject: Header \n\n This\nis the body of the email \n\n -from you')

conn.quit()
