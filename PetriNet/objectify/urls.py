from django.conf.urls import url
from . import views
from views import PetriNetView

urlpatterns = [
#    url(r'^$', views.index, name='index'),
#     url(r'^pnet/$', 'objectify.views.show_pnet'),
     url(r'^add/$', 'objectify.views.add_unit'),
     url(r'^save/$', 'objectify.views.save_unit'),
    url(r'^edit/$', PetriNetView.as_view(), name='PetriNetView'),
]
