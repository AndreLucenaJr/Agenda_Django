from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-a',
                'placeholder' : 'Aqui veio do init'
            }
        ),
        help_text='Texto de ajuda'

    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description', 'category')


    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name != last_name:
            msg = ValidationError(
                    'Primeira nome não pode ser diferente do segundo',
                    code = 'invalid')
            
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
            
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            raise ValidationError(
                'Não digite ABC nesse campo',
                code='  invalid'
            )

        return first_name