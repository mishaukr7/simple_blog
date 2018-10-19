from django.urls import path, include

from . import views

app_name = 'posts'

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('posts/<int:post>', views.PostDetailView.as_view(), name='post'),
    path('posts/comment/<int:post>', views.add_comment, name='add_comment'),
    
]