
from django.urls import path
from portapp import views
urlpatterns = [

    path('', views.home, name='home'),
  
    
]
