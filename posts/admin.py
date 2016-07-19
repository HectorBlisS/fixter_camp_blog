from django.contrib import admin
from .models import Post 


class PostAdmin(admin.ModelAdmin):
	list_display = (
		'titulo',
		'slug',
		'status',
		'creado',
		)
	list_filter = ('status','creado','actualizado')
	search_fields = ('titulo','cuerpo','creado','slug')
	prepopulated_fields = {'slug':('titulo',)}
	date_hierchy = 'creado'
	ordering = ['status','creado']


admin.site.register(Post, PostAdmin)