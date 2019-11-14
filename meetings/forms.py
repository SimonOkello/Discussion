from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=5000)

    class Meta:
        model = Question
        fields = ['subject', 'message']

