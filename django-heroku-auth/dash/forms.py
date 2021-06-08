
from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from dash.models import MyUser


class RegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = MyUser
		fields = ( "username", "email", "password1", "password2" )



## submit job form

## zip of images
#  config file (maybe zip)



## approve users form
# either generate one giant form based on number of accounts (checkboxes)
## or a bunc hof individual forms that pass the id (see nav trading example)
