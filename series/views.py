from re import template
import re
from django.http import request
from django.shortcuts import render, redirect

def dashboard(request):
    template_name = "back/dashboard.html"
    context = {
        'title':'Dashboard'
    }
    return render(request, template_name, context)
