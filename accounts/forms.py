from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.forms import Textarea, TextInput, EmailInput, TextInput, PasswordInput, FileInput





class UserForm(UserCreationForm):

    password1 = forms.CharField(
            widget = forms.PasswordInput(attrs={
            #'style': 'height:45px; width:100%; border:1px solid darkgreen; color:white; background:transparent; margin-top:15px; font-size:18px',
            'placeholder':'Create Password',
            'class': 'login'
            })
    )

    password2 = forms.CharField(
            widget = forms.PasswordInput(attrs={
           # 'style': 'height:45px; width:100%; border:1px solid darkgreen; color:white; background:transparent; margin-top:15px; font-size:18px',
            'placeholder':'Confirm Password',
            'class': 'login'
            })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'profile_pic']
        widgets={
		'username':TextInput(attrs={
			# 'style': 'height:45px; width:100%; border:1px solid darkgreen; color:white; background:transparent; margin-top:15px;font-size:18px',
            'placeholder':'Username',
            'class': 'login'
			}),
		'email':EmailInput(attrs={
			# 'style': 'height:45px; width:100%; border:1px solid darkgreen; color:white; background:transparent; margin-top:15px;font-size:18px',
            'placeholder':'Email',
            'class': 'login'
			}),
        'profile_pic':FileInput(attrs={
    		# 'style': 'height:45px; width:100%; border:1px solid darkgreen; color:white; background:transparent; margin-top:15px;font-size:18px',
            'class': 'login'
    		}),
		}