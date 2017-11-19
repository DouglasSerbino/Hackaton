from django import forms 
from models import Documento

class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields=('nombre_documento', 'descripcion', 'archivo')

    def __init__(self, *args, **kwargs):
    	super(DocumentoForm, self).__init__(*args, **kwargs)
    	self.fields['nombre_documento'].widget.attrs.update({'class' : 'form-control'}),
    	self.fields['descripcion'].widget.attrs.update({'class' : 'form-control'}),
    	self.fields['archivo'].widget.attrs.update({'class' : 'dropify' })

