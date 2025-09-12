from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Profile
from .forms import ContactForm

# DRF imports
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProjectSerializer, ProfileSerializer

# --- WEB VIEWS ---

def home_view(request):
    """
    Main web view that displays the projects and profile information.
    """
    projects = Project.objects.all()
    profile = Profile.objects.first()  # assuming only one profile
    return render(request, "portfolio/home.html", {"projects": projects, "profile": profile})


def contact_view(request):
    """
    Contact page view.
    Handles GET to show the form and POST to process the contact submission.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "portfolio/contact.html", {"form": form})


# --- REST API VIEWS WITH DRF ---

@api_view(['GET', 'POST'])
def api_projects(request):
    """
    API endpoint for projects.
    GET: Returns a list of all projects.
    POST: Creates a new project with the provided data.
    """
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def api_profile(request):
    """
    API endpoint for profile information.
    GET: Returns the profile (assuming only one exists).
    POST: Updates the profile with the provided data.
    """
    profile = Profile.objects.first()
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
