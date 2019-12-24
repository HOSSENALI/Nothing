from django.urls import path

from Travelo import views

urlpatterns = [

    path('', views.index, name='index'),

]
