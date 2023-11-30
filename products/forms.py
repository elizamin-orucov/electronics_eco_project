from django import forms
from .models import ContactUs


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ("name", "email", "subject", "message")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control", "placeholder": field.title})




