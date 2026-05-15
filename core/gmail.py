import os

from dotenv import load_dotenv
from redmail.email import gmail as gm

load_dotenv()


def gmail(email: str, attachment: str):
    mail_me = os.getenv("GMAIL")
    app_pass_me = os.getenv("GMAIL_APP_PASSWORD")

    if not mail_me or not app_pass_me:
        raise ValueError(
            "GMAIL and GMAIL_APP_PASSWORD environment variables are required"
        )

    gm.username = mail_me
    gm.password = app_pass_me

    try:
        print("[INFO] sending email")
        gm.send(
            subject="[Recuun] Recon report ready",
            sender=mail_me,
            receivers=email,
            attachments={
                "report.txt": attachment,
            },
        )
        print(f"Email sent successfully to {email}")
    except Exception as e:
        return str(e)
