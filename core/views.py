from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request ,"index.html")

def product_detials(request):
    return render(request , 'product.html')

def store(request):
    return render(request , 'store.html')

def checkout(request):
    return render(request , 'checkout.html')