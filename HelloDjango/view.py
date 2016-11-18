
from HelloDjango.weather import weatherfind

def weather(request,cityname):
	if cityname==None:
		cityname = '成都'
	info = weatherfind(cityname.encode('utf-8'))
	if isinstance(info, str):
		return HttpResponse(info)
	else:
		'''
		weatherinfo = ''
		for s in info[:6]:
			 weatherinfo += s+'\n'
		'''
		context = {}
		context['title'] = cityname+'天气预报'
		context['weatherinfo'] = info[:6]
		return render(request, 'weather.html', context)

from django.http import HttpResponse

def add(request,a,b):
	c = int(a)+int(b)
	return HttpResponse(str(c))


from django.shortcuts import render

def hello(request):
	context = {}
	context['hello'] = 'hello python!'
	context['title'] = 'Hello'
	return render(request, 'hello.html', context)

from TestModel.models import Test
def testdb(request):
	test = Test(name="小王")
	test.save()
	return HttpResponse('hello 小王')
