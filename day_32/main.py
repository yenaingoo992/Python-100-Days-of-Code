from mail_manager import MailManager
import random
import datetime as dt

now = dt.datetime.now()
today = now.weekday()

if today == 0: # only send once a week on Monday
    mail_manager = MailManager(sender="YOU MAIL ADDRESS", password="PASSWORD")
    with open("quotes.txt") as file:
        contents = file.readlines()
        quote = random.choice(contents)
        mail_manager.send(to="MAIL ADDRESS", subject= "Monday Quote", content=quote)