from django import forms
from django.contrib.auth import authenticate

from ex.models import Tip, User


class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists.')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm = cleaned_data.get('password_confirm')

        if password and confirm and password != confirm:
            self.add_error('password_confirm', 'Passwords do not match.')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Invalid credentials.')
            self.user = user


class TipsForm(forms.ModelForm):
    class Meta:
        model = Tip
        fields = ['content']
        labels = {
            'content': 'Your Life Pro Tip',
        }
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Share your best life advice...', 'rows': 3}),
        }
