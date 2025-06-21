from django.urls import path
from . import views

urlpatterns = [
    path("", views.ContactUs, name="contactus"),
    path('contact2/', views.Contact2, name="contact2"),
]