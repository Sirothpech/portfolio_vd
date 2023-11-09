from django import forms
from siteTemplate.models import SiteTemplate, UserTemplate
from tinymce.widgets import TinyMCE

class SiteTemplateForm(forms.ModelForm):

    class Meta:
        model = SiteTemplate
        fields = ['name', 'description']



class TemplateForm(forms.ModelForm):
    class Meta:
        model = UserTemplate
        fields = ('html_content',)
        widgets = {
            'html_content': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }

