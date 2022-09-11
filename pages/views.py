from django.shortcuts import render


def homepage(request):
    return render(request, "pages/homepage.html")

def about_us(request):
    return render(request, "pages/about_us.html")

def contact_us(request):
    return render(request, "pages/contact_us.html")
