from django.forms import ModelForm
from demo.models.indication import indication



class IndicationForm(ModelForm) :
    class Meta:
        model =	indication
        fields = ("name", "status")