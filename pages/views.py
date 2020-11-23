from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwags):
    # print(args,kwags)
    # print(request.user)
    # return HttpResponse("<h>Hello mello<h/>")
    return render(request,"home.html",{})

def contact_view(request,*arg, **kwars):
    return render(request, "contact.html",{})

def about_view(request,*arg, **kwars):
    return render(request, "about.html",{})