from django.shortcuts import render


def home(request):
    return render(request, "Portfolio/home.html")


def about(request):
    return render(request, "Portfolio/about.html")


def projects(request):
    return render(request, "Portfolio/projects.html")


def skills(request):
    return render(request, "Portfolio/skills.html")


def education(request):
    return render(request, "Portfolio/education.html")


def certificates(request):
    return render(request, "Portfolio/certificates.html")


def project_details(request, pk=None):
    return render(request, "Portfolio/project_details.html")
