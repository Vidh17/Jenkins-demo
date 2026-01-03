from django.db import models
from django.db.models import Model


# Create your models here.
class Author(models.Model):
    author_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}from{self.city}"
    
class Genre(models.Model):
    genre_id=models.AutoField(primary_key=True)
    genrename=models.CharField(max_length=100)   

    def __str__(self):
       return f"{self.genrename}"
    
class Publisher(models.Model):
   pub_id=models.AutoField(primary_key=True)
   pubname=models.CharField(max_length=100)
   pubcity=models.CharField(max_length=100)
   pubemail=models.CharField(max_length=100)
   def __str__(self):
       return f"{self.pubname}"

class Book(models.Model):
    book_id=models.AutoField(primary_key=True)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    title=models.TextField()
    pages=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    genres=models.ManyToManyField(Genre)
    publish=models.ForeignKey(Publisher,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return f"{self.title}"
    

    

    






    