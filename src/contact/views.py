from django.shortcuts import render
from django.contrib import messages
from .models import ContactMessage

# Create your views here.
def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        sender_email = request.POST.get('email')

        # Créez une nouvelle instance du modèle ContactMessage et enregistrez-la dans la base de données
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_message = ContactMessage(nom=nom, email=email, message=message)
        contact_message.save()

        # Enregistrez un message flash
        messages.success(request, 'Demande bien envoyée.')

        # Redirigez l'utilisateur vers la page contact.html
        # return JsonResponse({'success': True})

    return render(request, 'registration/contact.html')
