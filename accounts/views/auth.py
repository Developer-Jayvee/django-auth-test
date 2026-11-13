
from django.shortcuts import render

# Create your views here.

def login_view(request):
    print(request.method)
    return render(request,'accounts/index.html')


