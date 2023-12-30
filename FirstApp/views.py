from django.shortcuts import render
from django.http import HttpResponse
from FirstApp.models import Musician, Album

# Create your views here.
def index(request):
    all_musician = Musician.objects.order_by('first_name')
    diction = {'const': 'Musician List', 'all_musician':all_musician}
    return render(request, 'FirstApp/index.html', context=diction)

