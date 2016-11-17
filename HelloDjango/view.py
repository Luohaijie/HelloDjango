

from django.http import HttpResponse

def add(request,a,b):
	c = int(a)+int(b)
	return HttpResponse(str(c))

from django.shortcuts import render

def hello(request):
	context = {}
	context['hello'] = 'hello python!'
	return render(request, 'hello.html', context)

from TestModel.models import Test
def testdb(request):
	test = Test(name="小王")
	test.save()
	return HttpResponse('hello 小王')
