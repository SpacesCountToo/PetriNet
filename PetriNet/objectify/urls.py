from django.conf.urls import url
from . import views
from views import PetriNetView

urlpatterns = [
     url(r'^add/$', 'objectify.views.add_unit'),
    url(r'^edit/$', PetriNetView.as_view(), name='PetriNetView'),
]
