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
        else:
            print("--------------------------------------------------------")
            print(form.errors)
            print("--------------------------------------------------------")

    context = {"form": form}
    return render(request, "products/contact.html", context)
