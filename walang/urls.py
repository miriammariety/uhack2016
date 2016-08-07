from . import views
from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.WalangHomeView.as_view(), name='home'),
    url(r'^signup$', views.SignUpView.as_view(), name='signup'),
    url(r'login$', views.LoginView.as_view(), name='login'),
    url(r'logout$', views.UserLogoutView.as_view(), name='logout'),
    url(r'^services/(?P<service>\w+)$', views.ServiceView.as_view(), name='services')
]
