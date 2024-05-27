from django import forms

class LocationForm(forms.Form):
    latitude = forms.FloatField(label='Latitude', required=True)
    longitude = forms.FloatField(label='Longitude', required=True)
