from django.shortcuts import render

from try_celery.tasks import send_mass_email


# Create your views here.
def mass_email_view(request):
    recipient = "john@example.com"
    print("received the request")
    send_mass_email.delay(recipient)
    print("send to celery")
    return render(request, "index.html")