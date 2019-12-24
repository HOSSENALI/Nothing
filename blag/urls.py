from django.urls import path

from blag import views

urlpatterns = [

    path('', views.home, name='home'),
    path('add', views.add, name='add'),

]
