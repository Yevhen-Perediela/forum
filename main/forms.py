from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Articles, Comments

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1']

class CustomUserAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class addPost(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'text']   

class addComment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']  
    # post_id = forms.IntegerField(widget=forms.HiddenInput())           
