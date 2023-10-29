from django.http import Http404
from django.http import HttpResponse
from django.template import loader

from .models import Page

def index(request):
    template = loader.get_template('main.html')
    context = {}

    return HttpResponse("UNDER CONSTRUCTION.")
    #return HttpResponse(template.render(context, request))

def page(request, category, url):
    try:
        page = Page.objects.get(category__name=category, url=url)
    except Page.DoesNotExist:
        raise Http404("Page does not exist")

    template = loader.get_template('page.html')
    context = {
        'page': page
    }

    return HttpResponse("UNDER CONSTRUCTION.")
    #return HttpResponse(template.render(context, request))

def page404(request):
    template = loader.get_template('404.html')

    return HttpResponse("UNDER CONSTRUCTION.")
    #return HttpResponse(template.render({}, request))

def page500(request):
    template = loader.get_template('500.html')

    return HttpResponse("UNDER CONSTRUCTION.")
    #return HttpResponse(template.render({}, request))