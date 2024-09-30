
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),
    path('pass_change/', views.PassChangeView.as_view(), name='pass_change'),
]