from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=30, required= True)
    last_name = forms.CharField(max_length=30, required= True )
    email = forms.EmailField(max_length=254, required= True)
    message = forms.CharField( max_length=2000, widget=forms.Textarea(),help_text='Write here your message!')
  

   