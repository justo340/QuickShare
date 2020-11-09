from django.urls import path
from notes import views
from .views import (
    NotesListView,
    VideoListView,
    NotesDetailView,
    NotesCreateView,
    NotesUpdateView,
    NotesDeleteView,
    UserNotesListView,
    VideoCreateView,
    VideoUpdateView,
    VideoDeleteView,
    VideoDetailView,
    UserVideoListView,
    # Latest_post
)

urlpatterns = [
    path('', NotesListView.as_view(), name='blog-home-Doc'),
    path('vid/', VideoListView.as_view(), name='blog-home-Vid'),
    path('user/<str:username>/doc', UserNotesListView.as_view(),
         name='user_doc_posts'),
    path('user/<str:username>/vid', UserVideoListView.as_view(),
         name='user_vid_posts'),
    path('post/doc/<int:pk>/', NotesDetailView.as_view(),
         name='post-Doc-detail'),
    path('post/vid/<int:pk>/', VideoDetailView.as_view(),
         name='post-Vid-detail'),
    path('post/doc/new/', NotesCreateView.as_view(), name='post-create-doc'),
    path('post/video/new/', VideoCreateView.as_view(),
         name='post-create-video'),
    path('post/doc/<int:pk>update/', NotesUpdateView.as_view(),
         name='post-Doc-update'),
    path('post/vid/<int:pk>/update/', VideoUpdateView.as_view(),
         name='post-Vid-update'),
    path('post/doc/<int:pk>/delete/', NotesDeleteView.as_view(),
         name='post-Doc-delete'),
    path('post/vid/<int:pk>/delete/', VideoDeleteView.as_view(),
         name='post-Vid-delete'),
    path('about/', views.about, name='blog-about'),
    #     path('read/', views.readFile, name='read')
    #     path('latest_post/', Latest_post.as_view(), name='latest_post'),
]
