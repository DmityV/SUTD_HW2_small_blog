from django import forms

from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'category')
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 8,
                'cols': 40,
                'placeholder': 'Текст поста'}
            )
        }