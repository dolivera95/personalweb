from django.contrib import admin
from .models import About, Education, Experience, Project, Skill, Tecnology, Type_Skill

# Register your models here.
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass

@admin.register(Tecnology)
class TecnologyAdmin(admin.ModelAdmin):
    pass

@admin.register(Type_Skill)
class Type_SkillAdmin(admin.ModelAdmin):
    pass

