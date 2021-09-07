from django.shortcuts import render

def index(request):
    selected = "home"
    return render(request, "demo/home.html", locals())
