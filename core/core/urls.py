"""core URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',include('login.urls')),
    path('home/',login_required(TemplateView.as_view(template_name = 'home/home.html')),name = 'home'),
    path('historia/',TemplateView.as_view(template_name = 'historia-clinica/historia.html'),name = 'historia'),
    path('novedades/',TemplateView.as_view(template_name = 'novedades/novedades.html'), name = 'novedades'),
    path('perfil/',TemplateView.as_view(template_name = 'perfil/perfil.html'), name = 'perfil'),
    path('notificaciones/',TemplateView.as_view(template_name = 'notificaciones/notificaciones.html'),name = 'notificaciones'),
    path('health/',include('health.urls')),
    path('',TemplateView.as_view(template_name = 'landing/landing.html'),name = 'landing'),
    path('dashboard/',include('dashboard.urls'))

]
