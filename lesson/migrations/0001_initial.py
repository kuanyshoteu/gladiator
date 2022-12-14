# Generated by Django 4.0.6 on 2022-08-13 08:57

from django.db import migrations, models
import django.db.models.deletion
import lesson.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('content', '0001_initial'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('logo_image', models.ImageField(blank=True, null=True, upload_to=lesson.models.upload_location)),
                ('type_of', models.CharField(default='theory', max_length=10)),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='task.task')),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, default='name', null=True)),
                ('order', models.IntegerField(default=0)),
                ('logo_image', models.ImageField(blank=True, null=True, upload_to=lesson.models.upload_location)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to=lesson.models.upload_location)),
            ],
            options={
                'ordering': ['order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='ExercisePaperOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('type_of', models.CharField(default='main', max_length=10)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.exercise')),
                ('lemma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.paper')),
            ],
        ),
        migrations.AddField(
            model_name='exercise',
            name='theory',
            field=models.ManyToManyField(through='lesson.ExercisePaperOrder', to='content.paper'),
        ),
    ]
