from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post

# posts = [
# 	{
# 		'author': 'Johnson',
# 		'title': 'Blog Post 1',
# 		'content': 'First Post Content',
# 		'date_posted': 'Jan 05, 2020'
# 	},
# 	{
# 		'author': 'Johnson2',
# 		'title': 'Blog Post 2',
# 		'content': 'First Post Content',
# 		'date_posted': 'Jan 05, 2020'
# 	}
# ]

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
 
