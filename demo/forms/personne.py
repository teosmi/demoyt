from django.forms import ModelForm
from demo.models.personne import Personne



class PersonneForm(ModelForm) :
    class Meta:
        model =	Personne
        fields = ("nom","prenom","email","adresse","code_postal","ville", "telephone", "commentaire")