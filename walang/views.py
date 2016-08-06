from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from walang.models import Person, Service
# Create your views here.
class WalangHomeView(TemplateView):
    template_name = "walang/home.html"

    def get_context_d
