from django.urls import path
from .views import *
from . import views

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name = 'home'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name = 'about'),
]
