from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
posts = [
	{
    'author':'Pratik',
    'title': 'blogpost 1',
    'content':'a day in my life',
    'date': '12/02/20',
	},
	{
    'author':'ritik',
    'title': 'blogpost 2',
    'content':'my life',
    'date': '24/08/20',
	}
]
def home(request):
	context ={
		'posts': posts
	}
	return render(request,'blog/home.html',context)

def about(request):
	return render(request,'blog/about.html',{'title': 'About'})
	

