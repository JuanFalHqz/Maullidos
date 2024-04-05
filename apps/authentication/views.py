from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import RedirectView, CreateView

from apps.authentication.form import RegisterForm


# Create your views here.
class CustomLoginView(LoginView):
    """
    Establece el inicio de sesión
    """
    template_name = 'authentication/login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('all_messages')
        return super().dispatch(request, *args, **kwargs)


class CustomLogoutView(RedirectView):
    """
    Establece la salida de sesión
    """
    pattern_name = 'all_messages'  # Redirige al usuario al login después de hacer logout

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)


class RegisterView(CreateView):
    """
    Establece el registro de usuario
    """
    model = User
    form_class = RegisterForm
    template_name = 'authentication/register.html'
    success_url = reverse_lazy('all_messages')  # Definimos la URL de éxito

    def form_valid(self, form):
        """
        Procesa el formulario si es válido.
        Autentica al usuario recién creado.

        :param form: form: El formulario de registro del usuario.
        :return: HttpResponseRedirect: Una respuesta de redirección a la URL de éxito del formulario.
        """
        # Guardamos el usuario en la base de datos
        response = super().form_valid(form)
        # Autenticamos al usuario recién creado
        login(self.request, self.object)
        return response
