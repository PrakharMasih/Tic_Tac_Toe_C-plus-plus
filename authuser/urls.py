from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home , name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('one/', views.one, name='one'),
    path('two/', views.two, name='two'),
    path('three/', views.three, name='three'),
    path('four/', views.four, name='four'),
    path('five/', views.five, name='five'),
    path('six/', views.six, name='six'),
    path('seven/', views.seven, name='seven'),
    path('eight/', views.eight, name='eight'),
    path('index/', views.index, name='index'),
]
