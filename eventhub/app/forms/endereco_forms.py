from django import forms
from ..models import EnderecoCliente

class EncerecoForm(forms.ModelForm):
    class Meta:
        model = EnderecoCliente
        fields = ['rua', 'cidade', 'estado']