# Generated by Django 4.0.6 on 2022-08-13 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='lemma',
            new_name='paper',
        ),
    ]
