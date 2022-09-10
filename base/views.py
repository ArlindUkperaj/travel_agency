from audioop import reverse
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm 


def homepage(request):
    page_title = 'Homepage'
    context = {
        'page_title': page_title
    }
    return render(request, 'base/homepage.html', context )


def about(request):
    page_title = 'About'
    context = {
        'page_title': page_title
    }
    return render(request, 'base/about.html', context)


def contact_us(request):
    page_title = 'Contact us'
    context = {
        'page_title': page_title
    }
    return render(request, 'base/contact_us.html', context)


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(reverse("base:homepage.html"))
			# return redirect("base:homepage.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="base/register.html", context={"register_form":form})



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect(reverse("base:homepage"))
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="base/login.html", context={"login_form":form})