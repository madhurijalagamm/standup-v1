from django import forms
from django.contrib.auth.models import User
from .models import Message

class MessageForm(forms.ModelForm):
    receiver = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=True), label='Send to')
    subject = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'content']
