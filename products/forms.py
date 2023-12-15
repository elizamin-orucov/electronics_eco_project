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

    def clean(self):
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        if name[0].islower:
            raise forms.ValidationError("Adin ilk herifi boyuk olmalidir.")
        return self.cleaned_data




