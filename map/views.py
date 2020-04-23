from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html', {'title': 'Home'})



def about(request):
	return render(request, 'about.html', {'title': 'About-us'})

def map(request):
	return render(request, 'map.html', {'title': 'Map-spread'})

def information(request):
	return render(request, 'information.html', {'title': 'information'})

def citations(request):
	return render(request, 'citations.html', {'title': 'blog'})

