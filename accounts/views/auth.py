
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, get_user_model, login
from ..forms import LoginForm
from django.contrib import messages
from core.decorators.jwt_decorator import jwt_required

from django.core.exceptions import ValidationError
# Create your views here.
import json

def login_view(request):

    if(request.method == "POST"): 
        return postLogin(request)

    return render(request,'accounts/index.html')
def postLogin(request):
    form = LoginForm(request.POST)
    if(form.is_valid()):

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(
            username = username,
            password = password
        )   
        if( user is not None):
            login(request,user)
            return redirect('profile')
            
    else:
        messages.error(request,'Invalid Credentials')
        form = LoginForm()

    return redirect('login');

@jwt_required
def profile(request):
    return render(request,'accounts/profile.html')

def signup(request):

    if(request.method == "POST"):
        return postSignup(request)
    
    return render(request,'accounts/signup.html')

def postSignup(request):
    try:
        User = get_user_model()
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password_confirm')


        if ( User.objects.filter(username= username).exists()):
            raise ValidationError('Username is already')


        if( password != confirm_password):
             raise ValidationError('Password do not match')

        User.objects.create_user(username=username, email=None , password=password)
        messages.success(request,"Account created successfully")
        return redirect('login')


    except ValidationError as e:
        return render(request,'accounts/signup.html' , { "error": e.messages})