from django import forms
from portfolio.contacts.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email Address'}),
            'email_subject': forms.TextInput(attrs={'placeholder': 'Email Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message'}),
        }