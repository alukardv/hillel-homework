from django.urls import path

from .views import my_first_view

app_name = 'my_random'

urlpatterns = [
    path('', my_first_view)
]
