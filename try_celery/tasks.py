import time

from celery import shared_task, task


@shared_task
def send_mass_email(recipient):
    print(recipient)
    print("start to sleep")
    time.sleep(5)
    print("walk up from sleep")
    return


@task
def send_scheduled_emails():
    return "Hello"
