from django.urls import path
from cip_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cip_app/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]