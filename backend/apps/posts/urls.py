from django.urls import path
from .views import (
    ListPosts,
    CreatePost,
    GetPost,
    EditPost,
    DeletePost
)



urlpatterns = [
    path('list/', ListPosts.as_view()),
    path('create/', CreatePost.as_view()),
    path('get/<str:slug>/', GetPost.as_view()),    
    path('edit/<str:slug>/', EditPost.as_view()),    
    path('delete/<str:slug>/', DeletePost.as_view())    
]
