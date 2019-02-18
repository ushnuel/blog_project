from drycleaningApp.models import Message
from django import forms

class MessageForm(forms.ModelForm):

    class Meta():
        model = Message
        fields = ('author', 'phone', 'location','plan_type', 'text',)
        labels = {
            'author': (''),
            'phone': (''),
            'location': (''),
            'text': (''),
            'plan_type': (''),
        }
        widgets = {
                'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name - please enter your fullname','name':'author'}),
                'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone number','name':'phone'}),
                'plan_type': forms.Select(attrs={'class':'form-control','name':'plan_type'}),
                'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Location ex: Opposite Oil and Gas Polythecnic','name':'location'}),
                'text': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Describe in details what you want us to get for you', 'rows':'6', 'cols':'80', 'name':'text'}),
            }
