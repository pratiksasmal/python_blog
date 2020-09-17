from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:#gives a nested namespace for config and keeps config in 1 place
		model = User
		fields = ['username', 'email', 'password1','password2']