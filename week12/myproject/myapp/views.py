from django.shortcuts import render

def home(request):
    context={
        "pk":request.user.pk,
        "username": request.user.username
    }
    return render(request, "home.html",context)