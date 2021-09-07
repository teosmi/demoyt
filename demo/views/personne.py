from django.shortcuts import render
from demo.models.personne import Personne
from demo.forms.personne import PersonneForm
from django.core.paginator import EmptyPage, Paginator
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy



def personne_list(request):
    selected        = "personnes"
    personne_list   = Personne.objects.all()


    # Pagination : 10 éléments par page
    paginator = Paginator(personne_list.order_by('-date_mise_a_jour'), 10)
    try :
        page = request.GET.get("page")
        if not page:
            page = 1
        personne_list = paginator.page(page)
    except EmptyPage:

        # Si on dépasse ta limite de pages, on prend La dernière
        personne_list = paginator.page(paginator.num_pages( ))
    return render(request, "demo/personne/personne_list.html", locals())

class CreatePersonne(CreateView):
    model           = Personne
    form_class      = PersonneForm
    template_name   = "demo/personne/personne_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_personne", kwargs={"pk": self.object.id})

class UpdatePersonne(UpdateView):
    model           = Personne
    form_class      = PersonneForm
    template_name   = "demo/personne/personne_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_personne", kwargs={"pk": self.object.id})    



