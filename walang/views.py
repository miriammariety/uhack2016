from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from walang.models import Person, Service


class WalangHomeView(TemplateView):
    template_name = "walang/home.html"

    def get_context_data(self, *args):
        context = super(WalangHomeView, self).get_context_data(*args)
        context['services'] = Service.objects.all()
        context['person'] = self.request.user.person
        return context


class WelcomeView(TemplateView):
    template_name = "walang/index.html"
