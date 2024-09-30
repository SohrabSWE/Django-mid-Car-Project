
from django.urls import path 
from . import views

urlpatterns = [
    path('add/', views.addPostCreateView.as_view(), name='add_post'),
    path('edit/<int:id>/', views.editPostUpdateView.as_view(), name='edit_post'),      
    path('delete/<int:id>/', views.deletePostView.as_view(), name='delete_post'),
    path('details/<int:id>/', views.DetailPostView.as_view(), name='detail_post'),
]