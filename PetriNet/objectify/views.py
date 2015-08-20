from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
from forms import *

from models import Unit,Connection

# Create your views here.

class PetriNetView(TemplateView):
    template_name = 'objectify/main.html'

    def get_context_data(self, **kwargs):
        context = super(PetriNetView, self).get_context_data(**kwargs)
        context['nodes'] = Unit.objects.all()
        context['wires'] = Connection.objects.all()
        context['nodect'] = range(
            max(
                [unit.level for unit in Unit.objects.all()]
            ) + 1
        )
        context['saveUnitSet'] = SaveUnitFormSet()
        context['saveConnSet'] = AddConnectionForm()
        return context
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        try:
            self.save_unit(self.request.POST)
        except:
            self.save_conn(self.request.POST)
        return self.render_to_response(context)

    def save_unit(self, request):
        formset = SaveUnitFormSet(request)
        if formset.is_valid():
            for form in formset:
                instance = form.save(commit=False)
                # print instance
                if instance.human_readable_name == '':
                    pass
                else:
                    if instance.x_val == \
                        Unit.objects.get(uuid_name=instance.uuid_name).x_val and \
                        instance.y_val == \
                        Unit.objects.get(uuid_name=instance.uuid_name).y_val:
                        pass
                    else:
                        instance.x_val=int(instance.x_val)
                        instance.y_val=int(instance.y_val)
                        # print 'saving %s data:' % instance.human_readable_name
                        # print 'x-val = %f\ny-val = %f' % \
                        #       (instance.x_val,instance.y_val)
                    instance.save()

    def save_conn(self, request):
        form = AddConnectionForm(request)
        if form.is_valid():
            print "Form valid"
            instance = form.save(commit=False)
            new_conn = Connection(source=instance.source,
                                  destination=instance.destination)
            print new_conn.id
            new_conn.save()
            print new_conn.id
            # instance.save()

def add_unit(request):
    if request.method == 'POST':
        print request.POST
        add_unit_form = AddUnitForm(request.POST)
        if add_unit_form.is_valid():
            new_obj = add_unit_form.save(commit=False)
            print new_obj
            new_obj.save()
            return HttpResponseRedirect('/objectify/add/')
    else:
        add_unit_form = AddUnitForm()
    return render(request,
                  'objectify/add_unit.html',
                  {'form':add_unit_form})

