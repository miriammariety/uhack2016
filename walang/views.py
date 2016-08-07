from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from walang.models import Person, Service
from .forms import UserForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext



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

    def get_context_data(self, *args, **kwargs):
        context = super(ServiceView, self).get_context_data(*args, **kwargs)
        return context


class SignUpView(TemplateView):
    template_name = "walang/signup.html"

    def get_success_url(self):
        return ('walang:home')

    def post(self,request):
        uf = UserForm(request.POST, prefix='user')
        pf = ProfileForm(request.POST, prefix='person')
        if uf.is_valid() and pf.is_valid():
            user = uf.save()
            person = pf.save(commit=False)
            person.user = user
            person.save()
            username = person.user.username
            password = request.POST['user-password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('walang:home')
        else:
            print uf.errors
            print pf.errors
            return self.render_to_response({'userform':uf, 'profileform': pf, 'view': self})

    def get(self, request):
        uf = UserForm(prefix='user')
        pf = ProfileForm(prefix='profile')
        return render(request, SignUpView.template_name,
                                  dict(userform=uf,
                                       profileform=pf))

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        return self.response_class(request=self.request, template=self.template_name, context=context, using=None,
                                   **response_kwargs)
