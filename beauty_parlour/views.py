from django.shortcuts import render,redirect
from .models import Message,Service,Barber,Gallery
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.db import models


def footer_message(request):
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Message.objects.create(content=content)
            return JsonResponse({"status": "success", "message": "Message sent successfully!"})
        else:
            return JsonResponse({"status": "error", "message": "Please write your message!"})


def about(request):
    if request.method == "POST":
        return footer_message(request)
    return render(request, 'about.html')


def home(request):
    if request.method == "POST":
        return footer_message(request)
    return render(request, 'home.html')


def service(request):
    data = Service.objects.all()
    li = []
    for i in data:
        li.append(i)
    data = li
    print(data)
    if request.method == "POST":
        return footer_message(request)
    
    return render(request, 'service.html', {'data': data})


def price(request):

    data = Service.objects.all()
    li = []
    for i in data:
        li.append(i)
    data = li

    if request.method == "POST":
        return footer_message(request)
    return render(request, 'price.html',{'data':data})


def team(request):

    data = Barber.objects.all()
    li = []
    for i in data:
        li.append(i)
    data = li

    if request.method == "POST":
        return footer_message(request)
    return render(request, 'team.html',{'data':data})


def gallery(request):
    data = Gallery.objects.all()
    li = []
    for i in data:
        li.append(i)
    data = li
    if request.method == "POST":
        return footer_message(request)
    return render(request, 'gallery.html', {'data':data})



# def contact(request):
#     if request.method == "POST":

#         success = False
#         error = None

#         username = request.POST.get('username')
#         user_email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         user_message = request.POST.get('message')

#         if username and user_email and subject and user_message:
#             sender_email = "projecttest09python@gmail.com"
#             sender_password = "pzfb hxzl xgrh yvjp"
#             receiver_email = "projecttest09python@gmail.com"

#             message = MIMEMultipart("alternative")
#             message["Subject"] = f"{subject} - Message from {username}"
#             message["From"] = user_email
#             message["To"] = receiver_email

#             text = f"""Hi,\n\nYou have received a message from {username} ({user_email}):\n\n{user_message}"""
#             message.attach(MIMEText(text, "plain"))

#             context = ssl.create_default_context()

#             try:
#                 with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
#                     server.login(sender_email, sender_password)
#                     server.sendmail(sender_email, receiver_email, message.as_string())
#                 success = True
#             except Exception as e:
#                 error = str(e)
#         else:
#             error = "All fields are required."

#         return render(request, 'contact.html', {'success': success, 'error': error})

#         # Handle footer form

#     return render(request, 'contact.html')


import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.shortcuts import render

def contact(request):
    if request.method == "POST":
        success = False
        error = None

        username = request.POST.get('username')
        user_email = request.POST.get('email')
        subject = request.POST.get('subject')
        user_message = request.POST.get('message')

        if username and user_email and subject and user_message:
            sender_email = "projecttest09python@gmail.com"
            sender_password = "pzfb hxzl xgrh yvjp"
            receiver_email = "projecttest09python@gmail.com"

            # Create the email message
            message = MIMEMultipart("alternative")
            message["Subject"] = f"{subject} - Message from {username}"
            message["From"] = sender_email  # Use sender's email here
            message["To"] = receiver_email
            message["Reply-To"] = user_email  # Set the user's email in the Reply-To field

            # Email body
            text = f"""
            Hi,

            You have received a message from {username} ({user_email}):
            
            {user_message}
            """
            message.attach(MIMEText(text, "plain"))

            # Create secure connection and send email
            try:
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, sender_password)
                    server.sendmail(sender_email, receiver_email, message.as_string())
                success = True
            except Exception as e:
                error = f"An error occurred while sending the email: {str(e)}"
        else:
            error = "All fields are required."

        return render(request, 'contact.html', {'success': success, 'error': error})

    return render(request, 'contact.html')

