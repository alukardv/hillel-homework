from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from apps.authentication.foms import RegistrationForm
from apps.authentication.models import ActivationToken

from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.authentication.models import User
from apps.authentication.serializers import UserSerializer

User = get_user_model()


class RegisterView(CreateView):
    model = User
    template_name = "registration/registration.html"
    success_url = reverse_lazy("authentication:registration-success")

    def get_form_class(self):
        return RegistrationForm


class RegisterSuccessView(TemplateView):
    template_name = "registration/registration-success.html"


class RegisterActivateEmailView(TemplateView):
    template_name = "registration/registration-activate.html"

    def get_context_data(self, **kwargs):
        token = self.kwargs.get("token")
        activation_token = get_object_or_404(ActivationToken, token=token)
        activation_token.user.is_active = True
        activation_token.user.save()
        activation_token.delete()


class AuthVieW(APIView):
    def get(self, request):
        user = request.user
        if not user.is_authenticated:
            raise Http404
        else:
            return Response(user.email)
