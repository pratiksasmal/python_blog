from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):#create new posts
	model = Post
	fields = ['title', 'content']
	#userpassestestmixin checks for certain test conditions b4 allowing edits
	#overwriting the form valid method

	def form_valid(self, form): #overriding form valid method
		form.instance.author = self.request.user
		return super().form_valid(form) #runnning on parent class

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostUpdateView(LoginRequiredMixin, UpdateView):#create new posts
	model = Post
	fields = ['title', 'content']
	#overwriting the form valid method

	def form_valid(self, form): #overriding form valid method
		form.instance.author = self.request.user
		return super().form_valid(form) #runnning on parent class 


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

#using functon
def about(request):
	return render(request,'blog/about.html',{'title': 'About'})
	

