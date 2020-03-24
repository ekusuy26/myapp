from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from ..models import UserInfo
from ..forms import LoginForm

# Create your views here.
def top(request):
   return render(request, 'index.html')

class Login(LoginView):
   form_class = LoginForm
   template_name = 'login.html'

class Logout(LoginRequiredMixin, LogoutView):
   template_name = 'index.html'