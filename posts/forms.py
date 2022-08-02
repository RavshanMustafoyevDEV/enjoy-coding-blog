
from django import forms
from django.forms import ModelForm
from .models import post
from ckeditor.fields import RichTextField


class new_post_form(ModelForm):
    class Meta:
        model = post
        fields = ['post_img','post_title','post_text','author']

        widgets = {
            'post_img':forms.FileInput(attrs={'class':'form-control'}),
            'post_title':forms.TextInput(attrs={'class':'form-control'}),
            'post_text':RichTextField(),
            'author':forms.Select(),

        }
        

        


