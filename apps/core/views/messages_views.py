from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView

from apps.core.forms import MessageForm
from apps.core.models import Message


class ListViewAllMessages(ListView):
    """
    Lista todos los mensajes
    """
    model = Message
    template_name = 'messages/messages.html'
    context_object_name = 'messages'
    ordering = ['-created_date']
    paginate_by = 10


class ListViewMessagesByUser(ListView):
    """
    Lista todos los mensajes dado un usuario
    """
    model = Message
    template_name = 'messages/messages_by_user.html'
    context_object_name = 'messages'
    paginate_by = 10

    def get_queryset(self):
        """
        Retorna todos los mensajes dado un usuario ordenado por fecha del más reciente al menos reciente
        :return: listado de mensajes
        """
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        if user:
            return Message.objects.filter(author_id=user_id).order_by('-created_date')


class CreateViewMessage(LoginRequiredMixin, CreateView):
    """
    Crea un mensaje
    """
    model = Message
    form_class = MessageForm
    template_name = 'messages/message_create.html'

    def form_valid(self, form):
        """
        Valida y crea un mensaje
        :param form: formulario con los datos del mensaje
        :return: HttpResponseRedirect: Una respuesta de redirección a la URL de éxito si el formulario es válido.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        """
        Obtiene la URL de éxito después de procesar el formulario.
        :return: La URL de éxito después de procesar el formulario.
        """
        return reverse_lazy('all_messages_by_user', kwargs={'user_id': self.request.user.pk})
