from django.shortcuts import render
from django.http import HttpResponse
from meetuprecommendationengine.models import NeoDatabaseHelper
# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
def loadpage(request):
    bc=NeoDatabaseHelper()
    return render(request,'dashboardPage.html',{"searchtxt":bc.loadGroups()})
def callcategories(request):
    bc = NeoDatabaseHelper()
    return HttpResponse(bc.createCategories(request))
