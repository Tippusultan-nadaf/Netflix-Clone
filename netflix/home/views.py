from django.shortcuts import render, HttpResponse
from home.models import contactus
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,"index.html")
    # return HttpResponse("this is home page")
def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")
    
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        date=datetime.today()
        print(name,email,phone,date)
        ins=contactus(name=name,email=email,phone=phone,date=date)
        ins.save()
    return render(request,"contact.html")
    