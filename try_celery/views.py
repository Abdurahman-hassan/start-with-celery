from django.shortcuts import render

from try_celery.tasks import send_mass_email, add_two_numbers


# Create your views here.
def mass_email_view(request):
    recipient = "john@example.com"
    print("received the request")
    send_mass_email.delay(recipient)
    print("send to celery")
    return render(request, "index.html")


def add_two_number_view(request):
    number1 = 4
    number2 = 5
    print("received the request")
    add_two_numbers.delay(number1, number2)
    print("send to celery")
    dict = {
        "number1": number1,
        "number2": number2,
        "sum": number1 + number2,
    }
    return render(request, "add.html", context=dict)
