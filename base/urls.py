from django.urls import path
from . import views

app_name = "base" 

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about', views.about, name='about_page'),
    path('contact_us', views.contact_us, name='contact_us'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login")    
]
