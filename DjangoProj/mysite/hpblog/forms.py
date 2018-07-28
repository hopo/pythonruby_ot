from django import forms
# from markdownx.fields import MarkdownxFormField

# class MDForm(forms.Form):
#     content = MarkdownxFormField()

class InsertForm(forms.Form):
    text = forms.Textarea
