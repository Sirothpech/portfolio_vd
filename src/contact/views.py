# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import ContactMessage
from decouple import config

def contact(request):
    """
    Handles a contact form submission in a Django web application.

    Saves the submitted message to the database, sends an email notification to the site owner,
    and displays a success message to the user.

    Args:
        request (HttpRequest): The HTTP request object containing the form data.

    Returns:
        HttpResponseRedirect: Redirects the user to the contact page.
    """
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email_utilisateur = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')


        contact_message = ContactMessage(nom=nom, email=email_utilisateur, subject=subject, message=message)
        contact_message.save()

        email_subject = subject
        message_body = f'Nom: {nom}\nEmail: {email_utilisateur}\nSujet: {subject}\nMessage: {message}'
        sender_email = email_utilisateur
        receiver_email = config('EMAIL_HOST_USER')

        send_mail(email_subject, message_body, sender_email, [receiver_email])


        messages.success(request, 'Demande bien envoyée.')


        return redirect('contact')

    return render(request, 'registration/contact.html')
