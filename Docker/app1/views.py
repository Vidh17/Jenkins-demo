from django.shortcuts import render
from django.http import *
from decimal import Decimal
from .models import Book

# Create your views here.

def home(request):
    return render(request,"homepage.html")
def regpage(request):
    return render(request,"regpage.html")

def cdisplay(request):
    bname=request.POST.get("bname")
    author=request.POST.get("author")
    price=request.POST.get("prices")
    pages=request.POST.get("pages")
    pr=Decimal(price)
    print(bname," ",author," ",price," ",pages)
    #ORM
    Book.objects.create(book_title=bname,author=author,price=pr,pages=pages)
    context={"bname":bname,"author":author,"price":pr,"pages":pages}
    return render(request,"cprocess.html",context)



