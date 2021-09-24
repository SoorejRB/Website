from .views import IndexView, ContactView, TermsAndConditions
from django.urls import path


app_name = "general"
urlpatterns = [
    path("", IndexView.as_view(), name = "home"),
    path("contact/", ContactView.as_view(), name = "contact"),
    path("terms-and-conditions", TermsAndConditions.as_view(), name = "tandc"),

]