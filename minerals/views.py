from django.shortcuts import render
from django.http import HttpResponse
from .models import Mineral

# Create your views here.
def home_page(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals_list.html', {"minerals": minerals})