# Generated by Django 4.2.4 on 2023-10-12 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_student_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]
