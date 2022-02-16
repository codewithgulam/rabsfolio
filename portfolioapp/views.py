from django.core.mail import send_mail
from django.contrib import messages

from django.shortcuts import redirect, render, HttpResponse

from portfolio import settings

# Create your views here.

def home(request):
    return render(request, 'portfolioapp/index.html')


def contact(request):
    if request.method == 'GET':
        sender_name = request.GET['name']
        email_subject = request.GET['subject']
        sender_email = request.GET['email']
        message = request.GET['message']
        receiver_email = ['pcboy177@gmail.com']
        from_email = settings.EMAIL_HOST_USER
        message1 = sender_name + "!! \n" + message + "sended by \n" + sender_email
        send_mail(email_subject, message1, from_email, receiver_email , fail_silently=False)
        messages.success(request, "You have successfully send the Email we'll contact you shortly.")

    return redirect(home)