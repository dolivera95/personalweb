from django.db import models

# Create your models here.

# Model about tag of tecnologies
class Tecnology(models.Model):
    name = models.CharField(verbose_name = "Nombre", max_length = 200)

    class Meta:
        verbose_name = "tecnología"
        verbose_name_plural = "categorías"
    
    def __str__(self):
        return self.name

# Model about projects
class Project(models.Model):
    title = models.CharField(verbose_name = "Título", max_length = 200)
    content = models.TextField(verbose_name = "Descripción")
    tecnologies = models.ManyToManyField(Tecnology, verbose_name = "Tecnologías")
    url = models.URLField(verbose_name = "Enlace", max_length = 200, null = True, blank = True)
    repository = models.URLField(verbose_name = "Repositorio", max_length = 200, null = True, blank = 200)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"

    def __str__(self):
        return self.title

# Model about "about-me"
class About(models.Model):
    title = models.CharField(verbose_name = "Título", max_length = 200, null = True, blank = True)
    content = models.TextField(verbose_name = "Acerca de mi")

    class Meta:
        verbose_name = "sobre mi"
        verbose_name_plural = "sobre mi"

    def __str__(self):
        return self.title

# Model about educations
class Education(models.Model):
    title = models.CharField(verbose_name = "Título", max_length = 200) 
    entity = models.CharField(verbose_name = "Entidad", max_length = 200)
    date = models.DateField(verbose_name = "Fecha obtenido", null = True, blank = True)
    url = models.URLField(verbose_name= "Enlace", max_length = 200, null = True, blank = True)

    class Meta:
        verbose_name = "educacion"
        verbose_name_plural = "educaciones"

    def __str__(self):
        return self.title

# Model about kind of skills
class Type_Skill(models.Model):
    title = models.CharField(verbose_name = "Tipo de Habilidad", max_length = 200)

    class Meta:
        verbose_name = "Tipo de Habilidad"
        verbose_name_plural = "Tipos de Habilidades"

    def __str__(self):
        return self.title
        

# Model about skills
class Skill(models.Model):
    title = models.CharField(verbose_name = "Habilidad", max_length = 200)
    level = models.CharField(verbose_name ="Nivel", max_length = 200, null = True, blank = True)
    type_skill = models.ForeignKey(Type_Skill, on_delete = models.CASCADE)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
        ordering = ['type_skill', '-level']

    def __str__(self):
        return self.title

# Model about experiences
class Experience(models.Model):
    title = models.CharField(verbose_name = "Puesto", max_length = 200)
    entity = models.CharField(verbose_name = "Organización", max_length = 200)
    start_date = models.DateField(verbose_name = "Fecha inicio", null = True, blank = True)
    end_date = models.DateField(verbose_name = "Fecha final", null = True, blank = True)
    functions = models.TextField(verbose_name = "Funciones")

    class Meta:
        verbose_name = "Experiencia"
        verbose_name_plural = "Experiencias"
        ordering = ['-end_date']

    def __str__(self):
        return self.title




    
