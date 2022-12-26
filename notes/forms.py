from django import forms
from django.core.exceptions import ValidationError
from .models import Notes


class NotesForm(forms.ModelForm):
    """Form definition for Notes."""

    class Meta:
        """Meta definition for Notesform."""

        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-5'}),
        }
        labels = {
            'text': 'Write your thoughts here'
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError("We only accept notes about Django!")
        return title
