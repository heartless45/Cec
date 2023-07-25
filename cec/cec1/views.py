from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'1.html')

def india(request):
	return render(request,'india.html')

def Australia(request):
	return render(request,'Australia.html')

def America(request):
	return render(request,'America.html')


def Gandhinagar(request):
	return render(request,'Gandhinagar.html')

def Karnataka(request):
	return render(request,'Karnataka.html')

def Maharashtra(request):
	return render(request,'Maharashtra.html')


def new(request):
	return render(request,'New.html')

def queen(request):
	return render(request,'Queens.html')

def Ts(request):
	return render(request,'Tsamnia.html')


def Cali(request):
	return render(request,'California.html')

def Flor(request):
	return render(request,'Florida.html')

def Geo(request):
	return render(request,'Georgia.html')