#form Modelform
from django.forms import ModelForm
from django import forms
from .models import Contact

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     email = forms.EmailField(max_length=50)
#     content = forms.TextInput()

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name","email","content"]
    
    def clean(self):
 
        # data from the form is fetched using super function
        super(ContactForm, self).clean()
         
        # extract the username and text field from the data
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        content = self.cleaned_data.get('content')
        # (print(name))
        # conditions to be met for the username length
        if name:
            if len(name) < 3:
                self._errors['name'] = self.error_class([
                    'Minimum 3 characters required'])
        else:
            self._errors['name'] = self.error_class([
                    'name is required'])
        # if len(text) <10:
        #     self._errors['text'] = self.error_class([
        #         'Post Should Contain a minimum of 10 characters'])
 
        # return any errors if found
        return self.cleaned_data