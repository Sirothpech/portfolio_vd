# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import ContactMessage
from decouple import config

def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email_utilisateur = request.POST.get('email')
        subject = request.POST.get('subject')  # Nouveau champ pour le sujet
        message = request.POST.get('message')

        # Créez une nouvelle instance du modèle ContactMessage et enregistrez-la dans la base de données
        contact_message = ContactMessage(nom=nom, email=email_utilisateur, subject=subject, message=message)
        contact_message.save()

        # Envoi d'e-mail
        email_subject = subject
        message_body = f'Nom: {nom}\nEmail: {email_utilisateur}\nSujet: {subject}\nMessage: {message}'
        sender_email = email_utilisateur
        receiver_email = config('EMAIL_HOST_USER')

        send_mail(email_subject, message_body, sender_email, [receiver_email])

        # Enregistrez un message flash
        messages.success(request, 'Demande bien envoyée.')

        # Redirigez l'utilisateur vers la page contact.html
        return redirect('contact')

    return render(request, 'registration/contact.html')
