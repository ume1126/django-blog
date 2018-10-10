from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('logout/', views.logoutview, name='logoutview'),
    path('login/', views.loginview, name='loginview'),
]
