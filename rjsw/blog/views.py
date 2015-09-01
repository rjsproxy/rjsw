from django.shortcuts import render

# Create your views here.


def BaseView(request):
	return render(request, 'blog/base.html')

