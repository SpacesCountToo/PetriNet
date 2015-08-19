from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
from forms import *

from models import Unit,Connection

# Create your views here.

class PetriNetView(TemplateView):
    template_name = 'objectify/pnet.html'

    def get_context_data(self, **kwargs):
        context = super(PetriNetView, self).get_context_data(**kwargs)
        context['nodes'] = Unit.objects.all()
        context['wires'] = Connection.objects.all()
        context['nodect'] = range(
            max(
                [unit.level for unit in Unit.objects.all()]
            ) + 1
        )
        context['saveset'] = SaveUnitFormSet()
        return context
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        # for posted in self.request.POST:
        #     print '%s:%s' % (posted,self.request.POST[posted])
        print context['saveset']
        formset = SaveUnitFormSet(self.request.POST)
        if formset.is_valid():
            for form in formset:
                instance = form.save(commit=False)
                print instance
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
                        print 'saving %s data:' % instance.human_readable_name
                        print 'x-val = %f\ny-val = %f' % \
                              (instance.x_val,instance.y_val)

                        instance.save()

        return self.render_to_response(context)
    # def get(self, request, *args, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     return self.render_to_response(context)

# def show_pnet(request):
#     return render_to_response('objectify/pnet.html',
#                               {'nodes':Unit.objects.all(),
#                                'wires':Connection.objects.all()},
#                               context_instance=RequestContext(request))
#
def add_unit(request):
    if request.method == 'POST':
        print request.POST
        add_unit_form = AddUnitForm(request.POST)
        if add_unit_form.is_valid():
            new_obj = add_unit_form.save(commit=False)
            new_obj.save()
            return HttpResponseRedirect('/objectify/add/')
    else:
        add_unit_form = AddUnitForm()
    return render(request,
                  'objectify/add_unit.html',
                  {'form':add_unit_form})

def save_unit(request):
    instances =  Unit.objects.all()
    formset = SaveUnitFormSet()
    # print instances
    # if request.method == 'POST':
    #     print request.POST
    #     for instance in instances:
    #         formset['%s' % instance.uuid_name] = \
    #             SaveUnitForm(request.POST,instance=instance)
    #         if formset['%s' % instance.uuid_name].is_valid():
    #             formset['%s' % instance.uuid_name].save()
    #         return HttpResponseRedirect('objectify/save/')
    # else:

    return render(request,
                  'objectify/save_units.html',
                  {'form':formset}
                 )
#