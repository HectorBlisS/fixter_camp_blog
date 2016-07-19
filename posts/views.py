from django.shortcuts import render
from django.views.generic import View
from .models import Post
from django.contrib.auth.models import User


class Blog(View):
	def get(self,request):
		template_name = 'blog.html'
		user = User.objects.get(username="pokemon")
		posts = user.blog_posts.all()
		context = {
			'entradas':posts
		}
		return render(request,template_name,context)
