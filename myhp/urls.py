from django.urls import path
from . import views

app_name='myhp'

urlpatterns = [
    path('top/', views.top, name='top'),
    path('index/', views.index, name='index'),
    path('show/create/', views.create, name='create'),
    path('show/<int:id>', views.show, name='show'),
]