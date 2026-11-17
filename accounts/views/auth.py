
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate

from core.decorators.jwt_decorator import jwt_required
# Create your views here.
import json

def login(request):

    if(request.method == "POST"): 
        return postLogin(request)

    return render(request,'accounts/index.html')
def postLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(
        username = username,
        password = password
    )   

    response = { 'data' : user , 'message' : None , 'error': None , 'status' : 200  }

    if( user is None):
        response['status'] = 401
        response['error'] = 'Invalid Credentials'
    return render(request,'accounts/index.html' , response, status=response['status'])

@jwt_required
def profile(request):
    return render(request,'accounts/profile.html')

def signup(request):
    return render(request,'accounts/signup.html')