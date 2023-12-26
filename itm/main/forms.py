from django import forms

class ContactForm(forms.Form ):
    name = forms.CharField (
        max_length=255,
        widget=forms.TextInput(
            attrs= { 'class' : 'form__daten__base' }
        )
    )

    surname = forms.CharField (
        max_length=255,
        widget=forms.TextInput(
            attrs= { 'class' : 'form__daten__base' }
        ) 
    )

    firma = forms.CharField (        
        max_length=255,
        widget=forms.TextInput(
            attrs= { 'class' : 'form__daten__base' }
        ) 
    )

    position = forms.CharField (        
        max_length=255,
        required=False,
        widget=forms.TextInput(
            attrs= { 'class' : 'form__daten__base' }
        ) 
    )

    telefon = forms.CharField (
        max_length=30,
        required=False,
        widget=forms.TextInput(
            attrs= { 'class' : 'form__daten__base' }
        ) 
    )

    place = forms.CharField (
        max_length=100,
        widget=forms.TextInput(
            attrs= { 'class' : 'form__daten__base' }
        ) 
    )

    email = forms.EmailField (
        widget=forms.EmailInput(
            attrs= { 'class' : 'form__daten__base'}
        ) 
    )
    plz = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs= { 'class' : 'form__daten__base' }
        ) 
    )
    
