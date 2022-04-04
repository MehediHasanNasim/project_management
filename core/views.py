from django.shortcuts import render, redirect, HttpResponseRedirect


def home(request):
    diction= {}
    return render(request, 'core/home.html', context=diction) 

