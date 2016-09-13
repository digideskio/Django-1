from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

from .models import Post

User = get_user_model()

class PostCreateForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			"user",
			"title",
			"content",
		]

class PostDeleteForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = []

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("This user does not")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect Password")
			if not user.is_active:
				raise forms.ValidationError("This user is not longer active")
		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegistrationForm(forms.ModelForm):
	email = forms.EmailField(label = 'Email address')
	email2 = forms.EmailField(label = 'Confirm Email')
	password = forms.CharField(widget = forms.PasswordInput)
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'email2',
			'password',
		]

	def clean_email2(self):
		email = self.cleaned_data.get("email")
		email2 = self.cleaned_data.get("email2")
		if email != email2:
			raise forms.ValidationError("Email must match")
		
		email_exist = User.objects.filter(email = email)
		if email_exist.exists():
			raise forms.ValidationError("Email has been already exist")	
		return email
	#	return super(UserRegistrationForm, self).clean(*args, **kwargs)
