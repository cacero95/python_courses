from django import forms
from django.core import validators

class FormWord(forms.Form):
    content = forms.CharField(
        label = "Contenido",
        required = True,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Digitar una palabra',
                'class': 'form_input'
            }
        )
    )
    type_options = [
        (1, 'Positiva'),
        (0, 'Negativa')
    ]
    content_type = forms.TypedChoiceField(
        label = "Calificación",
        choices = type_options
    )