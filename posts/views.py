from django.shortcuts import render
from django.views.generic import View
from .models import Post
from django.contrib.auth.models import User


class ListView(View):
	def get(self,request):
		template_name = 'blog.html'
		user = User.objects.get(username="pokemon")
		posts = user.blog_posts.all()
		context = {
			'entradas':posts
		}
		return render(request,template_name,context)

class DetailView(View):
	def get(self,request,slug):
		template_name = "detalle.html"
		post = Post.objects.get(slug=slug)
		context = {
		'post':post
		}
		return render(request,template_name,context)


class NuevoPost(View):
	def get(self,request):
		template_name = 'nuevo.html'
		context = {}
		return render(request,template_name,context)

	def post(self,request):
		titulo = request.POST.get('titulo')
		cuerpo = request.POST.get('cuerpo')
		post = Post()
		post.titulo = titulo
		post.cuerpo = cuerpo
		post.autor = request.user
		post.save()


		template_name = 'nuevo.html'
		context = {'guardado':True}

		return render(request,template_name,context) 







