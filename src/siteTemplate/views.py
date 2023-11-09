from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from siteTemplate.forms import TemplateForm
from .models import SiteTemplate, UserTemplate


@login_required
def select_template(request):
    if request.method == 'POST':
        template_id = request.POST['template']
        template = SiteTemplate.objects.get(pk=template_id)
        return HttpResponseRedirect(reverse('edit_template', args=[template.id]))
    else:
        templates = SiteTemplate.objects.all()
        return render(request, 'registration/select_template.html', {'templates': templates})


@login_required
def edit_template(request, template_id):
    template = get_object_or_404(SiteTemplate, pk=template_id)
    user = request.user

    if request.method == 'POST':
        form = TemplateForm(request.POST)
        if form.is_valid():
            # Créez une copie personnalisée et enregistrez-la
            custom_template = UserTemplate(user=user, template=template, html_content=form.cleaned_data['html_content'])
            custom_template.save()
            # Redirigez vers la vue "view_template" avec l'ID de la copie personnalisée
            return redirect('view_template', template_id=custom_template.pk)
    else:
        form = TemplateForm(instance=template)

    context = {
        'form': form,
        'template': template,
    }
    return render(request, 'registration/edit_template.html', context)


def view_template(request, template_id):
    try:
        template = UserTemplate.objects.get(pk=template_id)
    except UserTemplate.DoesNotExist:
        template = None

    return render(request, 'registration/view_template.html', {'template': template})

def get_template_preview(request, template_id):
    # Récupérez le modèle de site en fonction de l'ID sélectionné
    template = get_object_or_404(SiteTemplate, pk=template_id)

    # Générez un aperçu HTML du modèle (vous pouvez personnaliser cette partie en fonction de votre modèle)
    model_preview = f'<div class="template-preview">{template.html_content}</div>'

    # Vous pouvez également renvoyer l'aperçu sous forme de JsonResponse si vous préférez JSON
    # model_preview = {'preview': template.html_content}

    # Renvoyez l'aperçu en tant que réponse au format HTML
    return render(request, 'registration/template_preview.html', {'model_preview': model_preview})
