from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('recipe.html')
    return HttpResponse(template.render())