from multiprocessing.connection import answer_challenge
from tkinter import CASCADE
from django.db import models
from platformdirs import user_cache_dir
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, max_length=8)
    death_date = models.DateField(null=True, max_length=8)
    birth_place = models.CharField(max_length=200)

    
    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ManyToManyField(Author)
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=200)
    relise_date = models.DateField(null=True, max_length=8)
    relise_country = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    available_copies = models.IntegerField(null=True)
    book_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
# time stamps
# user rom daregistrirdeba, sheqmni EmailVerification obieqts.
# import random. 
# path('verify/<str:code>', views.verify_email, name="verify_email"), 
# saiti.com/verify/asdasdasdasd/
class EmailVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    expiry_date = models.DateField(max_length=8, null=True)
    used = models.BooleanField(default=False)
    
    
class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    body = models.CharField(max_length=200)
    show =  models.BooleanField(default=False)
    # modereted by

    def __str__(self):
        return self.body

class AdminMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True)
    repsonse_by = models.CharField(max_length=1000000, null=True, blank = True)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200, null = True, blank = True)

class Rent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    check_out = models.DateTimeField(auto_now_add=True)
    check_in = models.DateField(null=True, max_length=8, blank=True)
    return_date = models.DateField(null=True, max_length=8, blank=True)
    