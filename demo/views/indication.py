from django.shortcuts import render
from demo.models.indication import indication
from django.core.paginator import EmptyPage, Paginator
from django.views.generic import CreateView, UpdateView
from demo.forms.indication import IndicationForm
from django.urls import reverse_lazy


def indication_list(request):
    selected            = "indication"
    indication_list    = indication.objects.all()


    # Pagination : 10 éléments par page
    paginator = Paginator(indication_list.order_by('-name'), 10)
    try :
        page = request.GET.get("page")
        if not page:
            page = 1
        indication_list = paginator.page(page)
    except EmptyPage:

        # Si on dépasse ta limite de pages, on prend La dernière
        indication_list = paginator.page(paginator.num_pages( ))
    return render(request, "demo/indication/indication_list.html", locals())

class CreateIndication(CreateView):
    model           = indication
    form_class      = IndicationForm
    template_name   = "demo/indication/indication_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_indication", kwargs={"pk": self.object.id})

class UpdateIndication(UpdateView):
    model           = indication
    form_class      = IndicationForm
    template_name   = "demo/indication/indication_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_indication", kwargs={"pk": self.object.id})        