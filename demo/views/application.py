from django.shortcuts import render
from demo.models.application import application
from django.core.paginator import EmptyPage, Paginator
from django.views.generic import CreateView, UpdateView
from demo.forms.application import ApplicationForm
from django.urls import reverse_lazy


def application_list(request):
    selected            = "application"
    application_list    = application.objects.all()


    # Pagination : 10 éléments par page
    paginator = Paginator(application_list.order_by('-name'), 10)
    try :
        page = request.GET.get("page")
        if not page:
            page = 1
        application_list = paginator.page(page)
    except EmptyPage:

        # Si on dépasse ta limite de pages, on prend La dernière
        application_list = paginator.page(paginator.num_pages( ))
    return render(request, "demo/application/application_list.html", locals())

class CreateApplication(CreateView):
    model           = application
    form_class      = ApplicationForm
    template_name   = "demo/application/application_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_application", kwargs={"pk": self.object.id})

class UpdateApplication(UpdateView):
    model           = application
    form_class      = ApplicationForm
    template_name   = "demo/application/application_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_application", kwargs={"pk": self.object.id})        