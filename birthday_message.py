from datetime import datetime
from email import message
import smtplib, random
date = datetime.now().strftime('%d/%m')
birthdates = {'09/09':'Dad', '10/07':'Mum', '19/04':'Ayomide', '07/11':'Olamide', '05/07':'Similoluwa'}
contact = {'Dad':'temitayo', 'Olamide':'olailori01@gmail.com'}
text = ['Wish you a great year. \n Olamide Ilori', 
        'Have a blast. Happy birthday \n Olamide Ilori.' ]
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

for key,value in birthdates.items():
    if date == key and value in contact.keys():
        print(f"It is {value}'s birthday today, and his email is {contact[value]}.")

        msg = message.EmailMessage()
        msg['Subject'] = f'{value}, happy birthday!'
        msg['From'] = 'olailori01@gmail.com'
        msg['To'] = ', '.join({contact[value]})
        msg.set_content(text[random.randint(0, len(text) -1)])
        server.login('iloriolamidevincent@gmail.com', 'Dailystoic..')
        server.send_message(msg)
        server.quit()