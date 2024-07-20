from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up),
    path('login/', views.login),
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),
    
]