from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from dash.forms import RegisterForm
from dash.models import MyUser


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        else:
            print(str(form.errors))
            return render(response, "registration/register.html", {"form":form, "errors": form.errors})

        return redirect("/")
    
    else:
        form = RegisterForm()

        return render(response, "registration/register.html", {"form":form})



def home(request):
    pass

    return render(request, "dash/home.html")

