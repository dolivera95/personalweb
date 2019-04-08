from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import About, Education, Skill, Experience, Project

# Create your views here.

# Function-Based View to have all information about: aboutme, education, skill, etc.
def home(request):
    
    about = get_object_or_404(About)
    education = Education.objects.all()
    skill = Skill.objects.all()
    experience = Experience.objects.all()
    project = Project.objects.all()


    context = {
        "about" : about,
        "educations" : education,
        "skills" : skill,
        "experiences" : experience,
        "projects" : project
    }
    return render(request, "core/home.html", context)

