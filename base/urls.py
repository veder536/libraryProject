import imp
from django import urls
from django.urls import path
from . import views

app_name="base"

urlpatterns = [
    path('', views.home, name="home"),
    # path("test/", views.test, name="test"),
    path('create-book/', views.createBook, name="create-book"),
    path('create-author/', views.createAuthor, name="create-author"),
    path('author-list/', views.authorlist, name="authorlist"),
    path('edit-author/<str:pk>', views.editauthor, name="editauthor"),
    path('show-author/<str:pk>', views.showauthor, name="showauthor"),
    path('delete-author/<str:pk>', views.deleteauthor, name="deleteauthor"),
    path('book-list/', views.booklist, name="booklist"),
    path('show-book/<str:pk>', views.showbook, name="showbook"),
    path('edit-book/<str:pk>', views.editbook, name="editbook"),
    path('delete-book/<str:pk>', views.deletebook, name="deletebook"),
    path('search/', views.search, name='search'),
    path('verify/<str:code>', views.verify_email, name="verify_email"), 
    path('rent-book/<str:pk>', views.rentbook, name='rentbook'),
    path('delete-booking/<str:pku>', views.delete_booking,name='deletebooking'),
    path('reviews', views.reviews, name="reviews"),
    path('write-review/<str:pk>', views.writereview, name="writereview"),
    path('aproove-review/<str:pk>', views.aproovereview, name="aproove-review"),
    path('edit-review/<str:pk>', views.editreview, name="editreview"),
    path('delete-review/<str:pk>', views.deletereview, name="deletereview"),
    path('questions/', views.questions, name="questions"),
    path('write-question/>', views.write_question, name="writequestion"),
    path('write-answer/<str:pk>', views.write_answer, name="writeanswer"),
    path('answers/', views.answers, name="answers"),
    

    # path('login/', views.loginPage, name="login")
]