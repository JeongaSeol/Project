
#from coronaProject.coronaApp.models import coronaDistrict
from django.urls import path
from coronaApp import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('coronaWeek', views.coronaWeek, name='coronaWeek'),
    path('coronaMonth', views.coronaMonth, name='coronaMonth'),
    path('corona3Month', views.corona3Month, name='corona3Month'),
    path('corona6Month', views.corona6Month, name='corona6Month'),
    path('districtcorona', views.districtcorona, name='districtcorona'),
    path('vaccine', views.vaccine, name='vaccine'),
    path('board', views.board, name='board'),
    path('addBoard/', views.addBoard, name='addBoard'),
    path('deleteBoard/',views.deleteBoard,name='deleteBoard'),
    path('createdb1', views.createdb1, name='createdb1'),
    path('createdb2', views.createdb2, name='createdb2'),
    path('createdb3',views.createdb3, name='createdb3'),
    path('createdb4',views.createdb4, name='createdb4'),
]