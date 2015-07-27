from django.shortcuts import render_to_response,RequestContext
from django.http import HttpResponse
from django.views.generic import View
from models import Unit,Connection

# Create your views here.
class Graph(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse('hallo werldpool')

def show_pnet(request):
    return render_to_response("objectify/pnet.html",
                          {'nodes':Unit.objects.all(),
                           'wires':Connection.objects.all()},
                          context_instance=RequestContext(request))

def index(request):
    return HttpResponse("<h1>Hello World!</h1>")