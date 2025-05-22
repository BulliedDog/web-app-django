from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.
def my_view(request):
    return HttpResponse()

class basic_view(TemplateView):
    template_name = "basic_view"

def basic_response(request):
    if request.method == "GET":
        return HttpResponse()