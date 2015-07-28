from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View
from forms import AddUnitForm

from models import Unit,Connection

# Create your views here.
def add_unit(request):
    if request.method == 'POST':
        formset = AddUnitForm(request.POST)
        if formset.is_valid():
            new_obj = formset.save(commit=False)
            new_obj.save()
            return HttpResponseRedirect('/objectify/pnet/')
    else:
        formset = AddUnitForm()
    return render(request,
                  'objectify/add_unit.html',
                  {'form':formset})

def show_pnet(request):
    return render_to_response('objectify/pnet.html',
                          {'nodes':Unit.objects.all(),
                           'wires':Connection.objects.all()},
                          context_instance=RequestContext(request))

def index(request):
    return HttpResponse('<h1>Hello World!</h1>')