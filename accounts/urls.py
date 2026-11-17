from django.urls import path
from . import views
from .views.auth import login,profile,signup


urlpatterns = [
   path('login/',login, name='login'),
   path('profile/',profile, name='profile'),
   path('signup/',signup, name='signup')
]