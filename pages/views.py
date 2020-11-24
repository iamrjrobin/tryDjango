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
    my_context = {
        "my_text": "This is my text",
        "my_number": 234,
        "my_list": [2342,3434,54345, "abc", "etry"],
        "my_html": "<h1>Hello world</h1>"
    }

    return render(request, "about.html", my_context)