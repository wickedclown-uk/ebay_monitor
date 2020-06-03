# This is a tool to monior an Ebay page for updates.
# Have you ever been wait for something to appear on ebay,
# but they only appear a few times a week or month, 
# so you do not need to check it every day this will check it every 6hrs.
# You of cause need to have this on a machine, that is on 24 / 7 .. like a media server?!?
#
# Save this script to you system, 
#
# make sure is it is executable 'chmod +x em.py'
#
# Configure crontab: crontab -e
# at the bottom of the file add the following:
# 0 */6 * * * /opt/em/em.py
# 55 23 * * * /opt/em/em.py
#
# Save the file, now the cronjob will run every 6 hrs, and 2355hrs.
# REMEBER: change the folder location where you saved the script.


#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# copy and paste your ebay page url, remember to order by 'newly listed'
url = "<ENTER URL>"

items = []
today = datetime.date.today()


res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.content, 'html.parser')

new = soup.find_all("span", class_="tme")

items.append(new)
date =today.strftime("%d-%b")


def email():
    # make a note to email yourself
    mail_content = '''<ENTER A MESSAGE, I NORMAL HAVE THE LINK TO THE PAGE YOUR MONITORING>'''
    #The mail addresses and password
    sender_address = '<EMAIL ADDRESS OF THE SEND>'
    sender_pass = '<THEIR PASSOWRD>'
    receiver_address = '<EMAIL ADDRESS OF WHERE YOU WANT THE EMAIL TO BE SENT TO>'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Automated Message: Check Ebay for XV1900'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    #You need your SMTP SERVER and PORT to connect too.
    session = smtplib.SMTP('<YOUR SMTP SERVER>', <PORT>) #use email with port
    #session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')


if date in str(items):
    #print ("New Item Detected")
    email()
else:
    print ("nothing new")    



