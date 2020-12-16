from django import forms
from .models import Post, Comment

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.RegexField(regex=r'^\+?1?\d{9,15}$')

    class Meta:
        model = User
        fields = ["username", "email", "phone", "password1", "password2"]



class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)