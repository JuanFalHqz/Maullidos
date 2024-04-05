from .form import RegisterForm
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class CustomLoginViewTest(TestCase):
    """
    Caso de prueba para el inicio de sesión de usuario
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas
        :return: None
        """
        self.client = Client()  # Cliente de prueba para hacer solicitudes HTTP
        self.login_url = reverse('login')  # URL de inicio de sesión
        self.all_messages_url = reverse('all_messages')  # URL de todos los mensajes
        # Creamos un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_redirect_authenticated_user(self):
        """
        Verifica que un usuario autenticado sea redirigido a la página de mensajes si intenta acceder a la página de inicio de sesión.
        :return: None
        """
        self.client.login(username='testuser', password='testpassword')
        # Hacemos una solicitud GET a la vista de inicio de sesión
        response = self.client.get(self.login_url)
        # Verificamos que nos redirija a la página de mensajes si el usuario ya está autenticado
        self.assertRedirects(response, self.all_messages_url)

    def test_login_view(self):
        """
        Verifica que la página de inicio de sesión se pueda acceder correctamente y que la plantilla correcta se esté utilizando para renderizar la página.
        :return: None
        """
        response = self.client.get(self.login_url)
        # Verificamos que la vista devuelve el código de estado HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Verificamos que la plantilla correcta se utiliza para renderizar la página
        self.assertTemplateUsed(response, 'authentication/login.html')

    def test_login_dispatch_authenticated_user(self):
        """
        Prueba de redireccionamiento para un usuario autenticado.
        :return: None
        """
        self.client.login(username='testuser', password='testpassword')
        # Hacemos una solicitud GET a la vista de inicio de sesión
        response = self.client.get(self.login_url)
        # Verificamos que nos redirija a la página de mensajes si el usuario ya está autenticado
        self.assertRedirects(response, self.all_messages_url)

    def test_login_dispatch_unauthenticated_user(self):
        """
        Prueba de acceso a la vista de inicio de sesión para un usuario no autenticado.
        :return: None
        """
        response = self.client.get(self.login_url)
        # Verificamos que la vista devuelve el código de estado HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Verificamos que la plantilla correcta se utiliza para renderizar la página
        self.assertTemplateUsed(response, 'authentication/login.html')


class CustomLogoutViewTest(TestCase):
    """
    Caso de prueba para la salida de sesión de usuario
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas
        :return:
        """
        self.client = Client()
        self.logout_url = reverse('logout')
        self.login_url = reverse('login')

        # Creamos un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_logout_view(self):
        """
        Verifica que al hacer logout, el usuario sea redirigido correctamente a la página de inicio de sesión.
        Verifica que después de hacer logout, el usuario ya no esté autenticado.
        :return: None
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.logout_url)

        # Verificamos que nos redirija a la página de inicio de sesión después de hacer logout
        self.assertRedirects(response, self.login_url)
        # Verificamos que el usuario ya no está autenticado
        self.assertFalse(response.wsgi_request.user.is_authenticated)


class RegisterViewTest(TestCase):
    """
    Caso de prueba para el registro de usuario
    """
    def test_register_user(self):
        """
        Prueba de registro exitoso de un nuevo usuario.
        :return: None
        """
        # Creamos un usuario para simular el registro
        data = {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'}
        form = RegisterForm(data)
        self.assertTrue(form.is_valid())

        # Simulamos una solicitud POST al formulario de registro
        response = self.client.post(reverse('register'), data)

        # Verificamos si el usuario ha sido creado
        self.assertEqual(response.status_code, 302)  # Debe redirigir después del registro exitoso
        self.assertTrue(User.objects.filter(username='testuser').exists())

        # Verificamos si el usuario ha iniciado sesión automáticamente
        user = authenticate(username='testuser', password='testpassword')
        self.assertIsNotNone(user)

    def test_register_existing_user(self):
        """
        Prueba de manejo adecuado cuando se intenta registrar un usuario con un nombre de usuario que ya está en uso.
        :return: None
        """
        existing_user = User.objects.create_user(username='existinguser', password='testpassword')
        # Simulamos una solicitud POST al formulario de registro con el mismo nombre de usuario
        data = {'username': 'existinguser', 'password1': 'testpassword', 'password2': 'testpassword'}
        response = self.client.post(reverse('register'), data)

        # Verificamos que no se haya creado un nuevo usuario
        self.assertEqual(response.status_code, 200)  # Debe volver a cargar la página de registro
        self.assertTrue(User.objects.filter(username='existinguser').exists())
        self.assertFalse(User.objects.filter(username='existinguser').count() > 1)
