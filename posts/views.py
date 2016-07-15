from django.shortcuts import render
from django.views.generic import View
from .models import Post


class Blog(View):
	def get(self,request):
		template_name = 'blog.html'
		posts = Post.objects.all() 
		context = {
			'entradas':posts
		}
		return render(request,template_name,context)
