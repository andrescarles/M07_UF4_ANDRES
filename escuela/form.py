from django.forms import ModelForm
from .models import tabla

class objeto(ModelForm):
    class Meta:
        model=tabla
        fields = '__all__'