from django.urls import path
from . import views
from .views.auth import login_view,profile,signup
from .views.testView import TestListView


urlpatterns = [
   path('login/',login_view, name='login'),
   path('profile/',profile, name='profile'),
   path('signup/',signup, name='signup'),
   path('test/',TestListView.as_view(), name='list')
]