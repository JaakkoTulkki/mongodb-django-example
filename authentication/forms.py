from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="Your username", max_length=64)
    email = forms.EmailField(label="Your email")
    password = forms.CharField(widget=forms.PasswordInput())
