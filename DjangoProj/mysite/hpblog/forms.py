from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content']

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': 'Title Is ..'}
            ),
            'content': forms.Textarea(
                attrs={
                    'cols': '80',
                    'rows': '10',
                    'placeholder': 'Write Your Mind ..'
                }
            )
        }


'''
class InputTextForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'author', 'content']

class TareaForm(forms.Form):
    text = forms.Textarea
'''
