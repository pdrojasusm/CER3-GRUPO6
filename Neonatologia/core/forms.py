from django import forms

from .models import recien_nacido

class recien_nacidoForm(forms.ModelForm):

    class Meta:
        model = recien_nacido
        fields = '__all__'
