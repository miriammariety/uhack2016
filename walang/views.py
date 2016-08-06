from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from walang.models import Person, Service


class WalangHomeView(TemplateView):
    template_name = "walang/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(WalangHomeView, self).get_context_data(*args, **kwargs)
        context['services'] = Service.objects.all()
        context['person'] = self.request.user.person
        return context


class WelcomeView(TemplateView):
    template_name = "walang/index.html"


class ServiceView(DetailView):
    model = Service
    pk_url_kwarg = 'service'

