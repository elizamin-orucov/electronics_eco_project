from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("vacancy/", views.vacancies_view, name="vacancies"),
    path("faq/", views.faq_view, name="faq"),
    path("contact/", views.contact_us_view, name="contact-us"),
]
