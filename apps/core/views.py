from django.views.generic import ListView

from apps.core.models import Message


class ListViewAllMessages(ListView):
    model = Message
    template_name = 'messages/messages.html'  # Reemplaza 'all_messages.html' con la ruta de tu plantilla
    context_object_name = 'messages'
    ordering = ['-created_date']
    paginate_by = 10


class ListViewMessagesByUser(ListView):
    model = Message
    template_name = 'messages/messages_by_user.html'  # Reemplaza 'user_messages.html' con la ruta de tu plantilla
    context_object_name = 'messages'
    paginate_by = 10

    def get_queryset(self):
        user_id = self.kwargs['user_id']  # Obtén el ID del usuario de los argumentos de la URL
        return Message.objects.filter(author_id=user_id).order_by('-created_date')
