import time

from celery import shared_task, task


@shared_task
def send_mass_email(recipient):
    print(recipient)
    print("start to sleep")
    time.sleep(5)
    print("walk up from sleep")
    return


@shared_task
def add_two_numbers(x, y):
    print(x + y)
    print("The number has been calculated")
    time.sleep(5)
    print("walk up from sleep")
    return x + y


@task
def send_scheduled_emails():
    return "Hello"
