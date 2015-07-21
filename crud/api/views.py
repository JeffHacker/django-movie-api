from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.


def hello(request):
    return HttpResponse("Hello")


def api_movie_list_view(request):
    json_object = json.dumps({"name", "Jeff"})
    return  HttpResponse(json_object)
