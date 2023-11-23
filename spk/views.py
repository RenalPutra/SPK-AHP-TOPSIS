from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from mysite import views


def welcome(request):
    template_name = "login.html"
    
    if request.user.is_authenticated:
        return redirect(views.index)
    
    return render(request, template_name)


# def barangmasuk(request):
#     template_name = "formbarangmasuk.html"
#     return render(request, template_name)


# def tbdatabarang(request):
#     template_name = "tbdatabarang.html"
#     return render(request, template_name)
