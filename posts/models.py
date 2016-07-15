from django.db import models


class Post(models.Model):
	titulo = models.CharField(max_length=100)
	cuerpo = models.TextField()
	fecha = models.DateField(auto_now=True)


