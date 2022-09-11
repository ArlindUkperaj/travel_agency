from django.urls import path

from . import views


app_name = "pages" 

urlpatterns = [
    path("", views.homepage, name="homepage"), 
    path("about/", views.about_us, name="about"), 
    path("contact/", views.contact_us, name="contact"), 
]
