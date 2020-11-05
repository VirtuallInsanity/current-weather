from django import forms


class CityForm(forms.Form):
    city = forms.CharField(label='', label_suffix='', required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'City Name'}))
