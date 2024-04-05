from django import forms
from django.forms import TextInput

from .models import Message


class MessageForm(forms.ModelForm):
    """
    Formulario para crear un mensaje
    """

    class Meta:
        model = Message
        fields = ['message']
        widgets = {
            'message': TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Escriba su maullido',
            })
        }

    def clean_message(self):
        """
        Método para validar que la longitud del mensaje tenga menos de 140 caracteres.

        :return: El mensaje validado si tiene menos de 140 caracteres.
        :raises: forms.ValidationError: Si el mensaje excede los 140 caracteres.
        """
        message = self.cleaned_data['message']
        if len(message) > 140:
            raise forms.ValidationError("El mensaje debe tener menos de 140 caracteres.")
        return message
