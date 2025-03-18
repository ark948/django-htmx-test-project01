from django import forms
from django.core.exceptions import ValidationError
from .models import Contact




class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': "input input-bordered w-full",
            'placeholder': 'Contact Name'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': "input input-bordered w-full",
            'placeholder': 'Email Address'
        })
    )

    # dummy version, replace with actual validation code
    def clean_name(self):
        name = self.cleaned_data['name']
        if name.startswith('X'):
            raise ValidationError('No names start with X!')
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if Contact.objects.filter(user=self.initial.get('user'), email=email).exists():
            raise ValidationError("A contact with this email already exists.")
        return email

    class Meta:
        model = Contact
        fields = (
            "name", "email"
        )



