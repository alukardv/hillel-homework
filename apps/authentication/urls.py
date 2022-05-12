from django.urls import path

# from apps.authentication.views import (
#     RegisterView,
#     RegisterSuccessView,
#     RegisterActivateEmailView,
# )
from apps.authentication.views import AuthVieW

app_name = "authentication"

urlpatterns = [
    path('', AuthVieW.as_view())
    # path("registration/", RegisterView.as_view(), name="registration"),
    # path(
    #     "registration-success/",
    #     RegisterSuccessView.as_view(),
    #     name="registration-success",
    # ),
    # path(
    #     "registration-activate/<str:token>/",
    #     RegisterActivateEmailView.as_view(),
    #     name="registration-activate",
    # ),
]
