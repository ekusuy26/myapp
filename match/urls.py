from django.urls import path
from .views import index, user

app_name = 'match'

urlpatterns = [
    path('', index.top, name='index'),
# ブラウザからアプリケーションの「/」ルートにアクセスしたとき、indexメソッドが呼ばれる
    path('login/', index.Login.as_view(), name='login'),
    path('logout/', index.Logout.as_view(), name='logout'),
    path('users/', user.gets, name='users'),
    path('users/regist/', user.regist, name='regist'),
]