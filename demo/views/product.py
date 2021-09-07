from django.shortcuts import render
from demo.models.product import product
from django.core.paginator import EmptyPage, Paginator
from django.views.generic import CreateView, UpdateView
from demo.forms.product import ProductForm
from django.urls import reverse_lazy


def product_list(request):
    selected            = "product"
    product_list    = product.objects.all()


    # Pagination : 10 éléments par page
    paginator = Paginator(product_list.order_by('-name'), 10)
    try :
        page = request.GET.get("page")
        if not page:
            page = 1
        product_list = paginator.page(page)
    except EmptyPage:

        # Si on dépasse ta limite de pages, on prend La dernière
        product_list = paginator.page(paginator.num_pages( ))
    return render(request, "demo/product/product_list.html", locals())

class CreateProduct(CreateView):
    model           = product
    form_class      = ProductForm
    template_name   = "demo/product/product_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_product", kwargs={"pk": self.object.id})

class UpdateProduct(UpdateView):
    model           = product
    form_class      = ProductForm
    template_name   = "demo/product/product_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_product", kwargs={"pk": self.object.id})        