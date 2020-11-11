from django import forms
from .models import Gatos_en_adopcion,Usuario

class Gatos_en_adopcion_form(forms.ModelForm):
    class Meta:
        model = Gatos_en_adopcion
        fields = ['nombre','fecha_encontrado','raza','edad']
        labels = {
            'nombre': 'Nombre',
            'fecha_encontrado': 'Fecha en la que fue econtrado',
            'raza': 'Raza',
            'edad': 'Edad estimada'
        }

    widgets = {
        'nombre': forms.TextInput(attrs={'class':'form-control'}),
        'fecha_de_encontrado': forms.DateField(),
        'raza': forms.TextInput(attrs={'class':'form-control'}),
        'edad': forms.TextInput(attrs={'class':'form-control'})
    }
