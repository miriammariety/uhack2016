from django.shortcuts import render
from django.views.generic import TemplateView
from generalsettings.models import Person
# Create your views here.
class WalangHomeView(TemplateView):
    model = Person
    template_name = "walang/worker.html"
