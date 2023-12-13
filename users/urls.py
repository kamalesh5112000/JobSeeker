from django.urls import path

from users import views



urlpatterns = [
    path('users/', views.users,name='users'),
    path('users/userSignup/', views.userSignup,name='userSignup'),
    
    
]