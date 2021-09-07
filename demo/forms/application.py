from django.forms import ModelForm
from demo.models.application import application



class ApplicationForm(ModelForm) :
    class Meta:
        model =	application
        fields = ("product_id", "indication_id", "number","name","region","type","created_at", "status")