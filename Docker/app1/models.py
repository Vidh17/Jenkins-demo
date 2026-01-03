from django.db import models
from django.db.models import Model

# Create your models here
class Book(models.Model):
    book_id=models.AutoField(primary_key=True)
    book_title=models.TextField()
    author=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    pages=models.TextField()

    class meta:
        dp_table="book_master"

