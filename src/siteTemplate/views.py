from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from siteTemplate.forms import TemplateForm
from .models import SiteTemplate, UserTemplate


@login_required
def select_template(request):
    """
    Selects a template based on the user's request method.

    If the request method is POST, the function retrieves the selected template from the database and redirects the user to the `edit_template` page.
    If the request method is GET, the function retrieves all templates from the database and renders the `select_template.html` template, passing the templates as context.

    Args:
        request (HttpRequest): The HTTP request object containing information about the current request.

    Returns:
        HttpResponseRedirect or HttpResponse: If the request method is POST, the function returns an HttpResponseRedirect object, redirecting the user to the `edit_template` page for the selected template.
        If the request method is GET, the function returns an HttpResponse object, rendering the `select_template.html` template with the templates passed as context.
    """

    if request.method == 'POST':
        template_id = request.POST['template']
        template = SiteTemplate.objects.get(pk=template_id)
        return HttpResponseRedirect(reverse('edit_template', args=[template.id]))
    else:
        templates = SiteTemplate.objects.all()
        return render(request, 'registration/select_template.html', {'templates': templates})


@login_required
def edit_template(request, template_id):
    """
    Edit a template.

    This function is a Django view function that allows a logged-in user to edit a template. If the request method is POST, the function saves the edited template to the database and redirects the user to view the updated template. If the request method is GET, the function renders the template editing form with the current template data.

    Args:
        request (HttpRequest): The HTTP request object containing information about the current request.
        template_id (int): The ID of the template to be edited.

    Returns:
        HttpResponse: If the request method is POST, the function redirects the user to view the updated template.
        HttpResponse: If the request method is GET, the function renders the template editing form.
    """

    template = get_object_or_404(SiteTemplate, pk=template_id)
    user = request.user

    if request.method == 'POST':
        form = TemplateForm(request.POST)
        if form.is_valid():

            custom_template = UserTemplate(user=user, template=template, html_content=form.cleaned_data['html_content'])
            custom_template.save()
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
    """
    Retrieves a site template object based on the provided ID, generates an HTML preview of the template, and renders it using a template file.

    Args:
        request (HttpRequest): The HTTP request object.
        template_id (int): The ID of the site template to preview.

    Returns:
        HttpResponse: The rendered HTML preview of the site template.
    """
    template = get_object_or_404(SiteTemplate, pk=template_id)

    model_preview = f'<div class="template-preview">{template.html_content}</div>'

    return render(request, 'registration/template_preview.html', {'model_preview': model_preview})
