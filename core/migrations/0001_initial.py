# Generated by Django 2.2 on 2019-04-06 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Acerca de mi')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('entity', models.CharField(max_length=200, verbose_name='Entidad')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Fecha obtenido')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Enlace')),
            ],
            options={
                'verbose_name': 'educacion',
                'verbose_name_plural': 'educaciones',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Puesto')),
                ('entity', models.CharField(max_length=200, verbose_name='Organización')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Fecha inicio')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Fecha final')),
                ('functions', models.TextField(verbose_name='Funciones')),
            ],
        ),
        migrations.CreateModel(
            name='Tecnology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'tecnología',
                'verbose_name_plural': 'categorías',
            },
        ),
        migrations.CreateModel(
            name='Type_Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Tipo de Habilidad')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Habilidad')),
                ('type_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Type_Skill')),
            ],
            options={
                'verbose_name': 'skill',
                'verbose_name_plural': 'skills',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Descripción')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Enlace')),
                ('repository', models.URLField(blank=200, null=True, verbose_name='Repositorio')),
                ('tecnologies', models.ManyToManyField(to='core.Tecnology', verbose_name='Tecnologías')),
            ],
            options={
                'verbose_name': 'proyecto',
                'verbose_name_plural': 'proyectos',
            },
        ),
    ]
