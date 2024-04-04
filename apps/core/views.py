from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.core.forms import MessageForm
from apps.core.models import Message


class ListViewAllMessages(ListView):
    model = Message
    template_name = 'messages/messages.html'
    context_object_name = 'messages'
    ordering = ['-created_date']
    paginate_by = 10


class ListViewMessagesByUser(ListView):
    model = Message
    template_name = 'messages/messages_by_user.html'
    context_object_name = 'messages'
    paginate_by = 10

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Message.objects.filter(author_id=user_id).order_by('-created_date')


class CreateViewMessage(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'messages/message_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('all_messages_by_user', kwargs={'user_id': self.request.user.pk})
