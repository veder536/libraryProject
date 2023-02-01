from email.message import Message
import imp
from multiprocessing import context
from re import A
from time import process_time_ns
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.urls import reverse

from .decorators import admin_only
from django.views.decorators.http import require_POST, require_GET
from .models import Author, Book, Booking, EmailVerification, Rent, BookReview, AdminMessage
from django.db.models import Q
from .forms import AuthorForm, BookForm, RentForm, BookReviewForm


# Create your views here.

def home(request):

    
    return render(request, 'base/home.html')

# @admin_only
# def test(request):
#     print('here', request.user)
#     return render(request, 'base/login_registration.html')

@admin_only
def createBook(request):
    form = BookForm()
    if request.method == 'POST':
        print(request.POST)
        form = BookForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('base:home')

    
    context = {'form': form}
    return render(request, 'base/create-book.html', context)


@admin_only
def createAuthor(request):
    form = AuthorForm()
    if request.method == 'POST':
        print(request.POST)
        form = AuthorForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('base:home')
    

    context = {'form': form}
    return render(request, 'base/create-author.html', context)
# def test(request):
#     print('here', request)
#     return redirect('home')

@admin_only
def authorlist(request):
    author_list = Author.objects.all()
    context = {'authors': author_list}
    return render(request, 'base/author-list.html', context)


def showauthor(request, pk):
    
    author_info = Author.objects.filter(id = pk)
    
    context = {'author': author_info}
    return render(request, 'base/show-author.html', context)

def showbook(request, pk):
    # formreview = BookReviewForm()
    book_info = Book.objects.filter(id = pk)
    rented_copies = Rent.objects.filter(book_id = pk).count()
    # book_copies_now = book_info.available_copies - rented_copies
    rented_by = Booking.objects.filter(book_id = pk)
    written_reviews = BookReview.objects.filter(book = pk, show = True)
    user_pending_reviews = BookReview.objects.filter(book = pk, show = False, user = request.user)
    print(rented_by)
    for user in rented_by:
        print(user.user.username)
    context = {'book': book_info, 'rented_by': rented_by, 'writtenReviews': written_reviews,
               'userpendingreviews': user_pending_reviews}
    return render(request, 'base/show-book.html', context)
    

@admin_only
def booklist(request):
    
    book_list = Book.objects.all()
    context = {'books': book_list}
    return render(request, 'base/book-list.html', context)
@admin_only
def editbook(request, pk):

    # eg wignis saxelia ameria ro vqmnidi da author name davawere
    book = Book.objects.get(id = pk)
    form = BookForm(instance=book)
    if request.method == 'POST':
        print('aq 1')
        form = BookForm(request.POST, instance=book)
        print(form.errors.as_data())
        if form.is_valid():
            
            
            form.save()
            return redirect('base:booklist')
    context = {'form':form}
    return render(request, 'base/edit-book.html', context)
@admin_only
def editauthor(request, pk):

    author = Author.objects.get(id = pk)
    form = AuthorForm(instance=author)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('base:booklist')
    context = {'form':form}
    return render(request, 'base/edit-author.html', context)
@admin_only
def deleteauthor(request, pk):
    author = Author.objects.get(id = pk)
    author.delete()
    return redirect('base:authorlist')
def deletebook(request, pk):
    book = Book.objects.get(id = pk)
    book.delete()
    return redirect('base:authorlist')
@admin_only 
def search(request):

    search_querry = request.GET.get('search')
    search_for = request.GET.get('search_for')
    print(search_querry, search_for)
    if search_for == 'book':
        books = Book.objects.filter(
            Q(name__icontains=search_querry)
            
        )
    
        context = {'books': books}
        return render(request, 'base/search.html', context)
    elif search_for == 'author':
        authors = Author.objects.filter(
            Q(name__icontains=search_querry)
        )
        context = {'authors': authors}
        return render(request, 'base/search.html', context)    
    elif search_for == 'all':
        book = Book.objects.filter(
            Q(name__icontains=search_querry)
        )
        author = Author.objects.filter(
            Q(name__icontains=search_querry)
        )
        context = {'books': book, 'authors': author}
        return render(request, 'base/search.html', context)


def rentbook(request, pk):
    book = Book.objects.get(id=pk)
    # print(book)
    # rent_book = Booking.objects.create(
    #     user = request.user,
    #     book = book
    # )
    # book.save()
    return redirect('base:booklist')

@require_GET
def verify_email(request, code ):
    
   
    to_verify = EmailVerification.objects.get(code = code)
    to_verify.used = True
    to_verify.save()
    return redirect('base:home')


# from django.contrib.auth.decorators import user_passes_test

# def has_verified_email(user):
#     return EmailVerification.objects.filter(user=user, used=True).exists()

# @user_passes_test(has_verified_email)
# def add_comment(request):
#     pass

# def change_rent(request, pku, pkb):
#     rent = Rent.objects.get(user_id = pku, book_id = pkb)
#     form = RentForm(instance=rent)
#     if request.method == 'POST':
#         form = RentForm(request.POST, instance=rent)
#         print(form.errors.as_data())
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('base:showbook', kwargs={'pk' : pkb})) # keyword arguments
#     context = {'form': form}
#     return render(request, 'base/edit-rent.html', context)

    # rent 
def delete_booking(request, pk):
    booking = Booking.objects.get(id = pk)
    booking.delete()
    return redirect('base:home')    
    # delete rent

def reviews(request):
    reviews_querry = BookReview.objects.filter(show = False)
    context = {"reviews": reviews_querry}
    return render(request, 'base/reviews.html', context)
  
def writereview(request, pk):
    body = request.POST['body']
    book = Book.objects.get(id=pk) 
    review = BookReview.objects.create(
        user = request.user,
        book = book,
        body = body
    )
    return redirect(reverse('base:showbook', kwargs={'pk' : pk}))


def aproovereview(request, pk):
    review = BookReview.objects.get(id = pk)
    review.show = True
    review.save()
    return redirect('base:reviews')

def editreview(request, pk):
    author = BookReview.objects.get(id = pk)
    form = BookReviewForm(instance=author)
    if request.method == 'POST':
        form = BookReviewForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            author.show = False
            author.save()
            return redirect('base:booklist')

    context = {'form': form}
    return render(request, 'base/edit-review.html', context)

def deletereview(request, pk):
    review = BookReview.objects.get(id = pk)
    review.delete()
    return redirect('base:reviews')


def questions(request):
    questions_querry = AdminMessage.objects.filter(answer__isnull = True)
    context = {'questions': questions_querry}
    return render(request, 'base/admin-questions.html', context)

def write_question(request):
    if request.method == 'POST':
        question = request.POST['question']
        write_question = AdminMessage.objects.create(
            user = request.user,
            question = question
        )
        return redirect('base:writequestion')
    return render(request, 'base/write-question.html')

def write_answer(request, pk):
    admin_message = AdminMessage.objects.get(id = pk)
    if request.method == 'POST':
        answer = request.POST['answer']
        print('here')
        print(answer)
        admin_message.repsonse_by = request.user.id
        admin_message.answer = answer
        admin_message.save()
        return redirect('base:reviews')
    context = {'question': admin_message}
    return render(request, 'base/write-answer.html', context)

def answers(request):
    questions = AdminMessage.objects.filter(user = request.user, answer__isnull = False)
    return render(request, 'base/user-side-question.html', context={"questions": questions})

