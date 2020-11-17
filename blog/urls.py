from django.urls import path
from .views import (
	PostListView,
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),#home route url
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),#id of post is a prt of route
    path('post/new', PostCreateView.as_view(),name='blog-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about,name='blog-about'),

]

# classes are looking for <app>/<model>_<viewtype>.html