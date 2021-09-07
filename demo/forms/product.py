from django.forms import ModelForm
from demo.models.product import product



class ProductForm(ModelForm) :
    class Meta:
        model =	product
        fields = ("name", "status")