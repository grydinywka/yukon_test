from django import forms
from blog.models import BlogPost


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('name', 'text')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
