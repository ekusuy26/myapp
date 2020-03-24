from django.shortcuts import render, loader, redirect
from django.http import HttpResponse

from match.forms import RegistForm

def regist(request):
    if request.method == 'GET':
        form = RegistForm()
    else:
        form = RegistForm(request.POST, request.FILES)
        if form.is_valid():
            print('user_regist is_valid')
            form.save(request.POST)
            return redirect('/login/')
        else:
            print('user_regist false is_valid')

    template = loader.get_template('regist.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def gets(request):
    template = loader.get_template('users.html')
    context = {
        'form': '',
    }
    return HttpResponse(template.render(context, request))