from django.contrib import admin
from django.urls import path, include

from apps.core.views import ListViewAllMessages, ListViewMessagesByUser, CreateViewMessage

urlpatterns = [
    path('', ListViewAllMessages.as_view(), name='all_messages'),
    path('<int:user_id>/', ListViewMessagesByUser.as_view(), name='all_messages_by_user'),
    path('create/', CreateViewMessage.as_view(), name='create_message'),
]
