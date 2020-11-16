from django.urls import path
from .views import PostListView , PostDetailView
from . import views

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),#home route url
    path('post/<int:pk>', PostDetailView.as_view(),name='blog-detail'),#id of post is a prt of route
    path('about/', views.about,name='blog-about'),
]

# classes are looking for <app>/<model>_<viewtype>.html