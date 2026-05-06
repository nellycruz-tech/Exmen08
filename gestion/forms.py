from django import forms
from .models import Departamento, Empleado

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }