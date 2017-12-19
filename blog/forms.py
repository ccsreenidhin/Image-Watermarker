from django import forms

from .models import Document

class DocumentForm(forms.ModelForm):
    
    class Meta:
        model = Document
        fields =('orimage','text','x','y','color','fontsize', 'email')
