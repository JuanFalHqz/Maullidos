from django.test import TestCase
from django.urls import reverse
from .models import Message
from django.contrib.auth.models import User


class MessageListViewTests(TestCase):
    def setUp(self):
        # Crear algunos mensajes y un usuario para las pruebas
        self.user = User.objects.create_user(username='test_user', password='test_password')
        for i in range(15):
            Message.objects.create(message=f'Test message {i}', author=self.user)

    def test_all_messages_view(self):
        # Prueba que la vista de todos los mensajes carga correctamente y devuelve la cantidad correcta de mensajes
        response = self.client.get(reverse('all_messages'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'messages/messages.html')
        self.assertEqual(len(response.context['messages']), 10)  # Probamos que se muestran 10 mensajes por página

    def test_user_messages_view(self):
        # Prueba que la vista de mensajes de usuario carga correctamente y devuelve los mensajes correctos del usuario
        response = self.client.get(reverse('all_messages_by_user', kwargs={'user_id': self.user.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'messages/messages_by_user.html')
        self.assertEqual(len(response.context['messages']), 10)  # Probamos que se muestran los mensajes del usuario
        for message in response.context['messages']:
            self.assertEqual(message.author, self.user)  # Probamos que todos los mensajes pertenecen al usuario creado

        # Crear un nuevo usuario y asegurarse de que sus mensajes no estén presentes
        other_user = User.objects.create_user(username='other_user', password='test_password')
        for i in range(5):
            Message.objects.create(message=f'Test message {i}', author=other_user)
        response = self.client.get(reverse('all_messages_by_user', kwargs={'user_id': other_user.id}))
        self.assertEqual(len(response.context['messages']),
                         5)  # Probamos que solo se muestran los mensajes del usuario correcto
