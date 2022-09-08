from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail')
]