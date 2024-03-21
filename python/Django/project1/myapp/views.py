from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def square(request):
    
    return render(request,'index.html')

def squareNum(request):
 if request.method=='POST':
  n1= int (request.POST.get('num1'))
  square=n1*n1


 return render(request,'squarenum.html',data=square)

