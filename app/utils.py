from flask_mail import Message
from app import mail

def send_email(to_email,subject,body):
    msg = Message(
        subject=subject,
        recipients=[to_email],
        body=body
    )

    mail.send(msg)