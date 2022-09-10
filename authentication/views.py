import email
from re import T
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, logout as logout_user, login as login_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.http import JsonResponse
from base.models import EmailVerification
from django.urls import reverse
from authentication.utils import generate_random_verification_code, send_mail


@require_POST
def login(request):
    print("entered login view")
    email = request.POST.get('email')
    print(email)
    password = request.POST.get('password')
    print(password)

    user = authenticate(request, username=email, password=password)

    if user is not None:
        login_user(request, user)
        return redirect('base:home')
    else:
        return redirect('base:home')

@require_POST
def logout(request):
    logout_user(request)
    return redirect('base:home')

@require_POST
def register_user(request):
    email_new = request.POST['email']
    usernmae_new = request.POST['username']
    password_new = request.POST['password']
    print(password_new)
    if User.objects.filter(username = usernmae_new).exists():
        return JsonResponse({"message": "user already exists"}, status=409)
    else:
        
        new_user = User.objects.create(username = usernmae_new, email = email_new)
        new_user.set_password(password_new)
        new_user.save()
        
        code = generate_random_verification_code()
        create_code = EmailVerification.objects.create(code=code, user = new_user)

        verification_link = request.build_absolute_uri(reverse("base:verify_email", kwargs={"code": code}))
        send_mail(email_new, verification_link)



        
        return JsonResponse({"message": "user created"}, status=200)
    
    
    
