from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pnet/$', 'objectify.views.show_pnet'),
    url(r'^add/$', 'objectify.views.add_unit'),
]
