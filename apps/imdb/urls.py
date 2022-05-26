from django.urls import path

from apps.imdb.views import MyView, MovieRetrieveUpdateView, MovieDetailRetrieveUpdateView, PersonDetailRetrieveUpdateView

app_name = "imdb"

urlpatterns = [
    path("", MyView.as_view()),
    path("movie/<str:pk>/", MovieDetailRetrieveUpdateView.as_view()),
    path("person/<str:pk>/", PersonDetailRetrieveUpdateView.as_view()),
]
