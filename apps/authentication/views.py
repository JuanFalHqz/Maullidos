from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import RedirectView


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('all_messages')
        return super().dispatch(request, *args, **kwargs)


class CustomLogoutView(RedirectView):
    pattern_name = 'all_messages'  # Redirige al usuario al login después de hacer logout

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)
