from django import forms
from .models import Account

class RegistrationForms(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Ingrese password'
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Repetir password'
    }))

    class Meta:
        model = Account
        fields = ['first_name','last_name','phone_number','email','password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForms, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'Ingrese nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Ingrese apellido'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Ingrese telefono'
        self.fields['email'].widget.attrs['placeholder'] = 'Ingrese email'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control' ## instanciamos cada caja de texto y llamo a la propiedad attribute

    def clean(self):
        cleaned_data = super(RegistrationForms, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "El password no coincide, reintente"
            )