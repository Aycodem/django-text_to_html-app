from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget







class Postform(forms.ModelForm):
    body=forms.CharField(widget=CKEditorWidget(),label='Text Editor')
    class Meta:
        model=Post
        fields=('body',)