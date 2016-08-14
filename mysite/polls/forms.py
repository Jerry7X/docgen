from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_pw = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=100)