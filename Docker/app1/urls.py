from django.urls import path
from .import views

urlpatterns=[
    path("home",views.home,name="home"),
    path("regpage",views.regpage,name="regpage"),
    path("cdisplay",views.cdisplay,name="cdisplay"),
]