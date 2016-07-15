from django.shortcuts import render,HttpResponse
from django.views.generic import View


class Home(View):
	def get(self,request):
		template_name = 'home.html'
		pers = marvel()
		img = pers['data']['results'][0]['thumbnail']['path']
		ext = pers['data']['results'][0]['thumbnail']['extension']
		img = img+'.'+ext

		context = {
		'descripcion':pers['data']['results'][0]['description'],
		'nombre':pers['data']['results'][0]['name'],
		'img':img,

		}
		return render(request,template_name,context)
		# return HttpResponse(desc)














def marvel():
	import requests
	import hashlib

	ts = '1'
	public_key = '49b00060252ec6df688a67b44b75cc0e'
	private_key = 'd1eca4ab9b76596debb63de6f68be3e0e8bca898'
	ha = hashlib.md5((ts+private_key+public_key).encode()).hexdigest()
	url = 'http://gateway.marvel.com/v1/public/'

	personaje = requests.get(
		url+'characters',
		params = {
		'apikey':public_key,
		'ts':ts,
		'hash':ha,
		'name':'Iron man'
		}).json()

	descripcion = personaje['data']['results'][0]['description']
	return personaje
	# img = personaje['data']['results'][0]['thumbnail']['path']
	# img = img +'.jpg'
	# print(descripcion,'\nimagen: \n'+img)
	# import webbrowser
	# webbrowser.open(img)

