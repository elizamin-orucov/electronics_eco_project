from django.shortcuts import render
from .models import Faq
from .forms import ContactForm


def vacancies_view(request):
    context = {}
    return render(request, "products/vacancies.html", context)


def faq_view(request):
    faq = Faq.objects.order_by("order")
    context = {"faqs": faq}
    return render(request, "products/faq.html", context)


def contact_us_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "products/contact.html", context)


def index_view(request):
    return render(request, "products/index.html", status=200)


def shop_view(request):
    context = {}
    return render(request, "products/shop.html", context)

