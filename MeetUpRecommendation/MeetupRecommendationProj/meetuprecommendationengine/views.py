from django.shortcuts import render
from django.http import HttpResponse
from meetuprecommendationengine.models import NeoDatabaseHelper
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
@csrf_exempt
def loadpage(request):
    bc=NeoDatabaseHelper()
    bc.loadGroupsAndTopics()
    return render(request,'dashboardPage.html')
@csrf_exempt
def loadDefaultData(request):
    bc = NeoDatabaseHelper()
    return HttpResponse(bc.loadDefaultQuestions())
@csrf_exempt
def sendQueryOnSearchSelect(request):
    try:
        bc = NeoDatabaseHelper()
        result=bc.sendQueryOnSearchSelect(request.body.decode('utf-8'))
        return HttpResponse(result)
    except:
        return HttpResponse()

