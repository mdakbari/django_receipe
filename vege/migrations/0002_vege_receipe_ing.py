# Generated by Django 4.2.4 on 2023-11-29 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vege',
            name='receipe_ing',
            field=models.TextField(blank=True, null=True),
        ),
    ]