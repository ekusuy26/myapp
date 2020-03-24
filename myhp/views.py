from django.shortcuts import render
from match.models import Image


def top(request):
    return render(request, 'myhp/main.html', {})