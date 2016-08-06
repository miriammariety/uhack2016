from . import views
from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.WalangHomeView.as_view(), name='home'),
    url(r'^services/(?P<service>\w+)$', views.ServiceView.as_view(), name='services')

]
