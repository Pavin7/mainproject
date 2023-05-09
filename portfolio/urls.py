from django.urls import path
from . import views

urlpatterns = [

    path("",views.fun),
    path("about/",views.abt,name= "about")


]