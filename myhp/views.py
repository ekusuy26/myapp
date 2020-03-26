from django.shortcuts import render
from match.models import UserInfo


def top(request):
    return render(request, 'myhp/main.html', {})


def index(request):
    images = UserInfo.objects.all()
    return render(request, 'myhp/index.html', {'images': images})

def show(request):
    aaa = 3
    images = UserInfo.objects.get(pk=aaa)
    return render(request, 'myhp/show.html', {'images': images})