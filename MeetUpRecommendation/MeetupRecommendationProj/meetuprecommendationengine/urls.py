from django.conf.urls import url
from meetuprecommendationengine.views import loadpage,callcategories
urlpatterns = [
    url(r'^main/$', loadpage,name="dashboard"),
    url(r'^getcategories/$', callcategories, name='callcategories'),
]
