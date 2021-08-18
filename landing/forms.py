from django import forms
from .models import Landing, Workers, Feedback


class NewForm(forms.ModelForm):

    class Meta:
        model = Landing
        fields = ('title', 'text', 'img',)

    
class NewFormTag(forms.ModelForm):

    class Meta:
        model = Workers
        fields = ('firs_name', 'last_name', 'position', 'text', 'img', )



class FeedbackForm(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'body')


        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'body': forms.Textarea(attrs={'class': 'form-control'}),
                'email': forms.EmailInput(attrs={'class': 'form-control'}),
                }