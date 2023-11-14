"""
URL configuration for VD_02 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from account.views import register_user, index, login_user, logout_user
from contact.views import contact
from django.conf.urls.static import static
from siteTemplate.views import select_template, edit_template, view_template, get_template_preview
from utilisateur.views import create_profile, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('', index, name="index"),
    path('logout/', logout_user, name='logout'),
    path('contact/', contact, name='contact'),
    path('select_template/', select_template, name='select_template'),
    path('edit_template/<int:template_id>/', edit_template, name='edit_template'),
    path('view_template/<int:template_id>/', view_template, name='view_template'),
    path('get_template_preview/<int:template_id>/', get_template_preview, name='get_template_preview'),
    path('profile/', profile, name='profile'),
    path('create_profile/', create_profile, name='create_profile')

]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
