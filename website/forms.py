from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

def SignUpForm(UserCreationForm):
    # username = forms.CharField(label="",max_length=100, widget= forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    # password = forms.CharField(label="", max_length=100, widget= forms.TextInput(attrs={'class':'form-control','placeholder':'password'}))
    name =  forms.CharField(label="", max_length=100, widget= forms.TextInput(attrs={'class':'form-control','placeholder':'name'}))
    email = forms.EmailField(label="", widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Email Adress'}))
    date = forms.DateField(label="", widget= forms.TextInput(attrs={'class':'form-control','placeholder':'date'}))
    
    class Meta:
        models = User
        fields = ('name','email','date','username','password1')

        def __init__(self,*args,**kwargs):
            super(SignUpForm, self).__init__(*args,**kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'username'
            self.fields['username'].label=""
            self.fields['username'].help_text = ""

            self.fields['password1'].widget.attrs['placeholder'] = 'password1'
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].label=""
            self.fields['password1'].help_text = '<ul class = "form-text text muted small"><li>Your password can\'t be less than 8 character.</li><li>Your password can\'t be too similar</li><li>Your password is weired.</li></ul>' 