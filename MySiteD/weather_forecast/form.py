from .models import CityName
from django.forms import ModelForm, TextInput
class CityForm (ModelForm):
    class Meta:
        model= CityName
        fields= ['name']