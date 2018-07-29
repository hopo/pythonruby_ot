from django import forms

class TareaForm(forms.Form):
    text = forms.Textarea


class InputTextForm(forms.Form):
    title = forms.CharField(
        max_length=40,
        widget=forms.TextInput(attrs={'placeholder' : 'title is ..'}),
    )
