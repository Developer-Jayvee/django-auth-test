from django.urls import path
from . import views
from .views.auth import login,profile,signup
from .views.testView import TestListView


urlpatterns = [
   path('login/',login, name='login'),
   path('profile/<int:user_id>/',profile, name='profile'),
   path('signup/',signup, name='signup'),
   path('test/',TestListView.as_view(), name='list')
]