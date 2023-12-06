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
            # self.add_error("name", "Adin ilk herifi boyuk olmalidir.")
            raise forms.ValidationError("ad kicikdi")
        if email == "test@gmail.com":
            raise forms.ValidationError("mail kicikdi")
        return self.cleaned_data




