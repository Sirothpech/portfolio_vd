from django import forms
from siteTemplate.models import SiteTemplate, UserTemplate
from tinymce.widgets import TinyMCE

class SiteTemplateForm(forms.ModelForm):
    """
    A Django form for creating and updating instances of the SiteTemplate model.

    Fields:
    - name: A field for the name of the site template.
    - description: A field for the description of the site template.
    """

    class Meta:
        model = SiteTemplate
        fields = ['name', 'description']



class TemplateForm(forms.ModelForm):
    """
    A Django form for creating a form for the UserTemplate model.

    This form includes a TinyMCE widget for the html_content field.
    """
    class Meta:
        model = UserTemplate
        fields = ('html_content',)
        widgets = {
            'html_content': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }

