from django.urls import path
from . import views
from.views import auth


urlpatterns = [
   path('login/',auth.login_view, name='login'),
]