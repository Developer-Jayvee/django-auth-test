from django.views.generic import ListView
from ..models import UserProfile
class TestListView(ListView):
    model = UserProfile