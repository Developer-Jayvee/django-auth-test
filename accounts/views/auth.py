
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, get_user_model
from ..forms import LoginForm

from core.decorators.jwt_decorator import jwt_required
# Create your views here.
import json

def login(request):

    if(request.method == "POST"): 
        return postLogin(request)

    return render(request,'accounts/index.html')
def postLogin(request):
    form = LoginForm(request.POST)
    response = { 'data' : user , 'message' : None , 'error': None , 'status' : 200  }
    if(form.is_valid()):

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(
            username = username,
            password = password
        )   
        if( user is None):
            response['status'] = 401
            response['error'] = 'Invalid Credentials'
    else:
        response['status'] = 401
        response['error'] = 'Please fill up the fields correctly'
        form = LoginForm()
    return render(request,'accounts/index.html' , response, status=response['status'])

@jwt_required
def profile(request):
    return render(request,'accounts/profile.html')

def signup(request):

    if(request.method == "POST"):
        return postSignup(request)
    
    return render(request,'accounts/signup.html')

def postSignup(request):
    User = get_user_model()
    username = request.POST.get('username')
    password = request.POST.get('password')
    confirm_password = request.POST.get('password_confirm')

    response = { 'data' : None , 'message' : None , 'error': True , 'status' : 200  }                                    

    if ( User.objects.filter(username= username).exists()):
        response['status'] = 403
        response['message'] = 'Username is already used. Please user another one'

        return render(request,'accounts/signup.html' , response)

    if( password != confirm_password):
        response['status'] = 403
        response['message'] = 'Password do not much'

        return render(request,'accounts/signup.html' , response)

    response['error'] = False

    response['data'] = User.objects.create_user(username=username, email=None , password=password)
    print(response)
    return render(request,'accounts/index.html' , response)