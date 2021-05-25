from django import forms


class BoardForm(forms.Form):
    title = forms.CharField(
        error_messages={
            'required': 'Enter the title'
        },
        max_length=128, label="Title")
    contents = forms.CharField(
        error_messages={
            'required': 'Enter the contents'
        },
        widget=forms.Textarea, label="Contents")