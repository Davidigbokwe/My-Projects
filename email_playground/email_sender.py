import smtplib #smtp is a standard for email to be sent simle mail tranfer protocol
from email.message import EmailMessage
from string import Template 
from pathlib import Path  #os.path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'David Igbokwe'

email['to'] = 'delosmusicc@gmail.com'
email['subject'] = 'You won 1,000,000 dollars'

email.set_content(html.substitute({'name':'TinTin'}),'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('dommypython@gmail.com','pythondeveloper2019')
	smtp.send_message(email)
	print('all good boss!')
