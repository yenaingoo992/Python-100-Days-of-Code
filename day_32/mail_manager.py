import smtplib
from email.message import EmailMessage


class MailManager:

    def __init__(self, **kwargs):
        self.sender = kwargs["sender"]
        self.password = kwargs["password"]
        self.smtp = "smtp.gmail.com"

    def send(self, **kwargs):
        subject = kwargs["subject"]
        to = kwargs["to"]
        contacts = [to]
        content = kwargs["content"]
        message = EmailMessage()
        message['Subject'] = subject
        message['From'] = self.sender
        message['To'] = ', '.join(contacts)
        message.set_content(content)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(self.sender, self.password)
            smtp.send_message(message)
