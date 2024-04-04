from django import forms
from django.forms import TextInput

from .models import Message


class MessageForm(forms.ModelForm):
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

    """def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) > 140:
            raise forms.ValidationError("El mensaje debe tener menos de 140 caracteres.")
        return message"""
