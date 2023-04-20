from django.forms import ModelForm
from .models import tabla,alumno,profesor

class objeto(ModelForm):
    class Meta:
        model=tabla
        fields = '__all__'
    
class alumno_objeto(ModelForm):
    class Meta:
        model=alumno
        fields = '__all__'
class profesor_objeto(ModelForm):
    class Meta:
        model=profesor
        fields = '__all__'