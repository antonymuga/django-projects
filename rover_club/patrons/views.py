from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Patron

# Create your views here.

def patrons(request):
    mypatrons = Patron.objects.all().values()
    template = loader.get_template('all_patrons.html')
    context = {
            'mypatrons': mypatrons,
            }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mypatron = Patron.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
            'mypatron': mypatron,
            }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mypatrons = Patron.objects.values_list('fname')
    template = loader.get_template('template.html')
    context = {
            'mypatrons': mypatrons,
            }
    return HttpResponse(template.render(context, request))
