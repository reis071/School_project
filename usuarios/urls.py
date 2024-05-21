from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login, name='login'),
    #path('unlogin', views.unlogin, name='unlogin'),
]
