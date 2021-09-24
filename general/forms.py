from django.forms import ModelForm
from .models import Contact, Career


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
    

class CareerForm(ModelForm):
    class Meta:
        model = Career
        fields = "__all__"



