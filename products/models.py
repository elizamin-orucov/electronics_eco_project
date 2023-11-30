from django.db import models
from services.mixin import DateMixin
from ckeditor.fields import RichTextField


class ContactUs(DateMixin):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact us"


class Faq(models.Model):
    question = models.CharField(max_length=300)
    answer = RichTextField()
    order = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "FAQ"
        verbose_name = "question"




