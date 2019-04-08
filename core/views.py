from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import About, Education, Skill, Experience

# Create your views here.

def home(request):
    
    about = get_object_or_404(About)
    education = Education.objects.all()
    skill = Skill.objects.all()
    experience = Experience.objects.all()


    context = {
        "about" : about,
        "educations" : education,
        "skills": skill,
        "experiences" : experience
    }
    return render(request, "core/home.html", context)

