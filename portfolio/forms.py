from django import forms

class ContactForms(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your Name'}),label=False,max_length=100,required=True)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter Your Email'}),label=False,required=True)
    selectOption=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Your Subject'}),label=False,required=True)
    message=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter Your Message'}),label=False,required=True)