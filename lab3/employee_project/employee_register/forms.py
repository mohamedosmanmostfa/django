from django import forms
from .models import std


class stdForm(forms.ModelForm):

    class Meta:
        model = std
        fields = ('std_fname','std_lname','std_email','std_gender')
        labels = {
            'std_fname':'First Name',
            'std_lname':'last name',
            'std_email':'Email',
            'std_gender':'Gender'
        }

    def __init__(self, *args, **kwargs):
        super(stdForm,self).__init__(*args, **kwargs)
        
        self.fields['std_gender'].required = False
