from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"), 
    path("contact/", views.contact_view, name="contact"),
    path("api/projects/", views.api_projects, name="api_projects"),
    path("api/profile/", views.api_profile, name="api_profile"),
]