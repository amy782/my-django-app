from django import forms
from .models import Blog, Profile

class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'desc', 'date', 'img']

class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']