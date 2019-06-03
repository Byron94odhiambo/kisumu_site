from django import forms
MINISTRY = [
    ('AGRIC AND LIVESTOCK', 'Agriculture And Livestock'),
    ('ENVIRON AND NATURAL RESOURCES', 'Environment And Natural Resources'),
    ('FINANCE AND ECONOMIC PLANNING', 'Finance And Economic Planning'),
    ('HEALTH AND SANITATION', 'Health And Sanitaion'),
    ('PHYSICAL PLANNING AND URBAN DEVELOPMENT', 'Physical Planning And Urban Development'),
    ('ROAD TRANSPORT AND PUBLIC WORKS', 'Road Transport And Public Works'),
    ('FINANCE AND ECONOMIC PLANNING', 'Finance And Economic Planning'),
    ('TOURISM ARTS CULTURE AND SPORT', 'Tourism Arts Culture And Sport.'),
    ('BUSINESS COOPERATIVES AND MARKETING', 'Business Cooperatives And Marketing'),
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
