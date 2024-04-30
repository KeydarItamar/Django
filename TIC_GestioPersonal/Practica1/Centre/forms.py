from django.forms import ModelForm
from .models import persona

class PersonForm(ModelForm):
    class Meta:
        model = persona
        fields = '__all__'