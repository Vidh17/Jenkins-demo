from django.shortcuts import render,redirect
from django.http import *
from .models import *
from decimal import Decimal

# Create your views here.
def home_page(request):
    return render(request,"home.html")

def book_reg(request):
    au=Author.objects.all()
    ge=Genre.objects.all()
    pu=Publisher.objects.all()

    return render(request,"bookreg.html",{"author":au,"genres":ge,"public":pu})

def author_reg(request):
    return render(request,"authorreg.html")

def adisplay(request):
    author_id=request.POST.get("author_id")
    aname=request.POST.get("name")
    aemail=request.POST.get("email")
    amobile=request.POST.get("mobile")
    acity=request.POST.get("city")
    print(aname," ",aemail," ",amobile," ",acity)
    #ORM
    Author.objects.create(author_id=author_id,name=aname,email=aemail,mobile=amobile,city=acity,)
    context={"aname":aname,"aemail":aemail,"amobile":amobile,"acity":acity}
    return render(request,"aprocess.html",context)

def book_add(request):
    if request.method =="POST":
       title=request.POST.get("title")
       author_id=request.POST.get("author")
       pages=request.POST.get("pages")
       price=request.POST.get("price")
       genre_ids=request.POST.getlist("genre")
       publisher_id=request.POST.get("publisher")
       pr=Decimal(price)
       print(title," ",author_id," ",title," ",pages,"",pr,genre_ids,publisher_id)

       author=Author.objects.get(author_id=author_id)    #ORM
       pub =Publisher.objects.get(pub_id=publisher_id)
       book=Book.objects.create(title=title,author=author,pages=pages,price=pr,publish=pub)
       book.genres.set(Genre.objects.filter(genre_id__in=genre_ids))

       return redirect ("bookadd")
    return redirect ("bookadd") 

def genre_reg(request):
    return render(request,"genrereg.html")

def gdisplay(request):
    genre_id=request.POST.get("genre_id")
    genrename=request.POST.get("genrename")
    print(genrename)
    Genre.objects.create(genre_id=genre_id,genrename=genrename)
    context={"genre_name":genrename,}
    return render(request,"gprocess.html",context)

def alldata(request):
    author=Author.objects.all()
    return render(request,"bookall.html",{"author":author})

def public_reg(request):
    return render(request,"publicreg.html")

def pdisplay(request):
    pub_id=request.POST.get("pub_id")
    pubname=request.POST.get("pubname")
    pubcity=request.POST.get("pubcity")
    pubemail=request.POST.get("pubemail")

    print(pubname)
    Publisher.objects.create(pub_id=pub_id,pubname=pubname,pubcity=pubcity,pubemail=pubemail)
    context={"pubname":pubname,"pubcity":pubcity,"pubemail":pubemail}
    return render(request,"pubprocess.html",context)

def alldetails(request):
        book=Book.objects.all()
        return render(request,"bookdetails.html",{"book":book})