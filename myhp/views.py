from django.shortcuts import render
from match.models import UserInfo


def top(request):
    return render(request, 'myhp/main.html', {})