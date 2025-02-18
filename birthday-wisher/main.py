import datetime as dt
from zoneinfo import ZoneInfo
import pandas
import random
from mail_manager import MailManager

def to_times(num:int):
    times = str(num)
    if times.endswith("1"):
        times += " st"
    elif times.endswith("2"):
        times += " nd"
    elif times.endswith("3"):
        times += " rd"
    else:
        times += " th"
    return times

now = dt.datetime.now(tz=ZoneInfo("Asia/Rangoon"))
templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
mail_manager = MailManager(sender="YOUR MAIL ADDRESS", password="YOUR PASSWORD")
df = pandas.read_csv("birthdays.csv")
records = df.to_dict(orient="records")

for record in records:
    month = record['month']
    day = record['day']
    year_diff = now.year - record['year']
    birthday_times = to_times(year_diff)

    if now.month == month and now.day == day:
        message = ""
        file_path = "letter_templates/" + random.choice(templates)
        with open(file_path) as file:
            for line in file.readlines():
                message += line.replace("[NAME]", record["name"])

        mail_manager.send(to=[record["email"]], subject=f"HAPPY {birthday_times} Birthday", content=message)