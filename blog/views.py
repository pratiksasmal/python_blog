from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
# Create your views here.

def home(request):
	context ={
		'posts': Post.objects.all()
	}
	return render(request,'blog/home.html',context)

#using classes
class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'# classes are looking for <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted'] # to order posts acc to date

class PostDetailView(DetailView):
	model = Post

#using functon
def about(request):
	return render(request,'blog/about.html',{'title': 'About'})
	

