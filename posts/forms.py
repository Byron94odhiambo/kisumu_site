from django import forms
MINISTRY = [
   ('AGRIC AND LIVESTOCK', 'Agriculture And Livestock'),
   ('ENVIRON AND NATURAL RESOURCES', 'Environment And Natural Resources'),
   ('FINANCE AND ACCOUNTING', 'Finance And Accounting'),
   ('HEALTH AND SERVICES', 'Health And Services'),
   ('PHYSICAL PLANNING AND/HOUSING', 'Physical Planning And Housing'),
   ('PUBLIC WORKS & UTILITIES', ' Public Works And Utilities'),
   ('EDUCATION, CULTURE, SOCIAL', 'Education Culture And Social'),
   ('TRADE, INDUSTRY DEV & REG', 'Trade Industry Dev & Reg'),
   ('ROADS &TRANSPORT', 'Roads And Transport'),
]


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=30, required= True)
    last_name = forms.CharField(max_length=30, required= True )
    email = forms.EmailField(max_length=254, required= True)
    subject = forms.CharField(max_length=254, required= True)
    message = forms.CharField( max_length=2000, widget=forms.Textarea(),help_text='Write here your message!')
  

class MinistryForm(forms.Form):
    ministry=forms.CharField(widget=forms.Select(choices=MINISTRY))
    first_name = forms.CharField(max_length=30, required= True)
    last_name = forms.CharField(max_length=30, required= True )
    email = forms.EmailField(max_length=254, required= True)
    subject = forms.CharField(max_length=254, required= True)
    message = forms.CharField( max_length=2000, widget=forms.Textarea(),help_text='Write here your message!')
    
