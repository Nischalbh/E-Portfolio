from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:pk>/", views.project_details, name="project_details"),
    path("skills/", views.skills, name="skills"),
    path("education/", views.education, name="education"),
    path("certificates/", views.certificates, name="certificates"),
]
