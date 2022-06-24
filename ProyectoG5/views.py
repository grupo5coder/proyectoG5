
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from django.template import Template, context
from django.template.loader import get_template

def index (request):
    return render(request,'index.html')
