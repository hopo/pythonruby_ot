from django import forms
from markdownx.fields import MarkdownxFormField

class MyForm(forms.Form):
    content = MarkdownxFormField()
