from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
class LoginViewCustom(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)
