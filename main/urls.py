from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('privacy/', views.privacy, name='privacy'),
    path('login/', views.user_login, name='login'),
    path('reg/', views.register, name='reg'),
    path('addpost/', views.add_post, name='addpost'),
    path('<int:id>/', views.article_details, name='article_details')
]