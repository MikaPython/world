from datetime import datetime

from django import forms

from .models import Country, Image


class CountryForm(forms.ModelForm):
    updated = forms.DateTimeField(initial=datetime.now().strftime('%Y:%m:%d %H:%M:%S'), required=False)

    class Meta:
        model = Country
        fields = '__all__'

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )