from django.urls import path
from clickBoard.views import clickBoard 

urlpatterns = [ 
    path(r'api/clipboardObjects', clickBoard.as_view()),
]
