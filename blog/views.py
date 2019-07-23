from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(Request):

	blogs = Blog.objects
	return render(Request, 'blog/blogs.html',{"blogs":blogs})

def detail(Request, blog_id):

	detailed_blog = get_object_or_404(Blog, pk= blog_id)
	return render(Request, 'blog/detail.html', {"blog": detailed_blog})