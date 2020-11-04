from django.urls import path
from notes import views
from .views import (
    NotesListView,
    NotesDetailView,
    NotesCreateView,
    NotesUpdateView,
    NotesDeleteView,
    UserNotesListView,
    # Latest_post
)

urlpatterns = [
    path('', NotesListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserNotesListView.as_view(),
         name='user_posts'),
    path('post/<int:pk>/', NotesDetailView.as_view(), name='post-detail'),
    path('post/new/', NotesCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', NotesUpdateView.as_view(),
         name='post-update'),
    path('post/<int:pk>/delete/', NotesDeleteView.as_view(),
         name='post-delete'),
    path('about/', views.about, name='blog-about'),
    #     path('latest_post/', Latest_post.as_view(), name='latest_post'),
]
