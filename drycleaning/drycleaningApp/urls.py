from django.conf.urls import url
from drycleaningApp import views

urlpatterns = [
    url(r'^about_us$', views.about_us, name='about_us'),
    url(r'^$', views.home, name='home'),
    url(r'^message$', views.my_messages, name='my_messages'),
    url(r'^billing_policy$', views.billing_policy, name='billing_policy'),
    url(r'^terms_agreement$', views.terms_agreement, name='terms_agreement'),
]
