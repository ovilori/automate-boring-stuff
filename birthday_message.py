from datetime import datetime
from email import message
import smtplib, random
date = datetime.now().strftime('%d/%m')
birthdates = {'09/11':'Polly', '10/12':'Alex', '19/12':'Arthur', '07/11':'Alfie', '15/07':'Tommy'}
contact = {'Alfie':'youremail@gmail.com'}
text = ['Wish you a great year. \n Alfie', 
        'Have a blast. Happy birthday \n Alfie.' ]
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

for key,value in birthdates.items():
    if date == key and value in contact.keys():
        print(f"It is {value}'s birthday today, and his email is {contact[value]}.")

        msg = message.EmailMessage()
        msg['Subject'] = f'{value}, happy birthday!'
        msg['From'] = 'youremail@gmail.com'
        msg['To'] = ', '.join({contact[value]})
        msg.set_content(text[random.randint(0, len(text) -1)])
        server.login('youremail+1@gmail.com', 'xxxxxxxxxx')
        server.send_message(msg)
        server.quit()