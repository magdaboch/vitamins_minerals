from django.shortcuts import render
from django.http import HttpResponse
from .models import Vitamin

# Create your views here.
def home_page(request):
    vitamins = Vitamin.objects.all()
    return render(request, 'vitamins_list.html', {"vitamins": vitamins})