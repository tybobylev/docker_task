from django.http import HttpResponse
from django.shortcuts import render
from .models import f_table

def index(request):
    # return render("Hello, world.")
    context = {}
    context['flights'] = f_table.objects.all()
    return render(request, 'index.html', context)
