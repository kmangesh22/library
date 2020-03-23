from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Author
# Create your views here.
def index(request):
    context={
        "authors":Author.objects.all()
    }
    return render(request,"library/index.html",context=context)


def register(request):
    context = {
        "message":"Hello"
    }
    if request.method == "POST":
        name=request.POST.get("name")
        branch=request.POST.get("branch")
        year=request.POST.get("year")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm password")
        if not name:
            context["message"] = "provide a valid name"
            return render(request,"library/register.html",context)    
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"library/register.html",context)    