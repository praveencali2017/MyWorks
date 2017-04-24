from django.conf.urls import url
from meetuprecommendationengine.views import loadpage,loadDefaultData,sendQueryOnSearchSelect
urlpatterns = [
    url(r'^main/$', loadpage,name="dashboard"),
    url(r'^loadDefaultQuestions/$', loadDefaultData, name='loaddefaultdata'),
    url(r'^onSelectOfList/$', sendQueryOnSearchSelect, name='queryonselect'),

]
