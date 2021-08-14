from django import forms
from . models import ProcessorDetail, Product

class ProcessortDetailForm(forms.ModelForm):
    
    class Meta:
        model = ProcessorDetail
        fields = (
        'thread',
        'cores',
        'tdp', 
        'socket', 
        'generation', 
        'core_brand',
        'model_name', 
        'freq',
        'proc_image',
        )

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = (
            'rating', 'price', 'manufacture',
        )
