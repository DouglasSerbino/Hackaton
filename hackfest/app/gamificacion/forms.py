from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    def __init__(self, *args, **kwargs):
    	super(SignUpForm, self).__init__(*args, **kwargs)
    	self.fields['username'].widget.attrs.update({'class' : 'form-control'}),
    	self.fields['first_name'].widget.attrs.update({'class' : 'form-control'}),
    	self.fields['last_name'].widget.attrs.update({'class' : 'form-control' }),
    	self.fields['email'].widget.attrs.update({'class' : 'form-control' }),
    	self.fields['password1'].widget.attrs.update({'class' : 'form-control' }),
    	self.fields['password2'].widget.attrs.update({'class' : 'form-control' })