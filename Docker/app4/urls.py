from django.urls import path
from .import views

urlpatterns=[
    path("home",views.home_page,name="home"),
    path("authorreg",views.author_reg,name="authorreg"),
    path("bookreg",views.book_reg,name="bookreg"),
    path("aprocess",views.adisplay,name="aprocess"),
    path("bookadd",views.book_add,name="bookadd"),
    path("genreg",views.genre_reg,name="genreg"),
    path("gprocess",views.gdisplay,name="gprocess"),
    path("alldetails",views.alldata,name="alldetails"),
    path("publicreg",views.public_reg,name="publicreg"),
    path("pubprocess",views.pdisplay,name="pubprocess"),
    path("bookdetails",views.alldetails,name="bookdetails"),
    
]