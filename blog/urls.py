from django.urls import path
from .views import *
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name = 'home'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('about/', views.about, name = 'about'),

    ### Rest API urls
    # path('api/post/', views.post_list),
    # path('api/post/<int:pk>/', views.post_detail),
    # path('api/post/', PostListAPIView.as_view()),
    # path('api/post/<int:pk>/', PostDetailAPIView.as_view()),
    # path('api/post/', PostListMixinAPIView.as_view()),
    # path('api/post/<int:pk>/', PostDetailMixinAPIView.as_view()),
    path('api/post/', PostListGenericAPIView.as_view()),
    path('api/post/new', PostCreateGenericAPIView.as_view()),
    path('api/post/<int:pk>/', PostDetailGenericAPIView.as_view()),
]

### To add format of data in the url
urlpatterns = format_suffix_patterns(urlpatterns)