# Generated by Django 4.2.4 on 2023-11-29 12:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0006_alter_vege_receipe_ingr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vege',
            name='receipe_ingr',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
        ),
    ]
