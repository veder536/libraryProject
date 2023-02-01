# from .models import Room


# class RoomForm(ModelForm):
#     class Meta:
#         model = Room
#         fields = '__all__'
from cProfile import label
from dataclasses import field, fields
from tabnanny import check
from django.forms import ModelForm, TextInput
from .models import Author, Booking, Rent, BookReview, Book
from django.forms.widgets import DateInput
from django import forms

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'birth_place', 'birth_date', 'death_date')
        labels = {
            'birth_date': ('birthdate'),
            'death_date': ('deathdate')
        }
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'birth_place': TextInput(attrs={'class': 'form-control'}),
            'birth_date': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'death_date': DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }
        

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('author', 'name', 'code', 'relise_date', 'relise_country', 'genre', 'is_available', 'book_image', 'available_copies')
        labels = {
            'relise_date': ('relisedate')
        }
        widgets = {
            # 'relise_date': DateInput(attrs={'type': 'date'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'code': TextInput(attrs={'class': 'form-control'}),
            'relise_date': DateInput(attrs={'type': 'date' ,'class': 'form-control'}),
            'relise_country': TextInput(attrs={'class': 'form-control'}),
            'genre': TextInput(attrs={'class': 'form-control'}),
            'is_available': TextInput(attrs={'class': 'form-control'}),
            'available_copies': TextInput(attrs={'type': 'range' ,'class': 'form-range', 'min': '0', 'max': '10'})
        }
class RentForm(ModelForm):
    check_in = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=False)
    return_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=False)
    class Meta:
        model = Rent
        fields = ('user', 'book')
        widgets = {
            'check_out': DateInput(attrs={'type': 'date' ,'class': 'form-control'}),

        }
class BookReviewForm(ModelForm):
    class Meta:
        model = BookReview
        fields = ('body',)
        widgets = {'body': DateInput(attrs={'class': 'form-control'})}
        