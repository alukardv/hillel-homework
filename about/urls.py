from django.urls import path

from .views import index, whoami

app_name = 'about'

urlpatterns = [
    path('', index),
    path('about/whoami', whoami),
]
