# Generated by Django 4.2.4 on 2023-11-29 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0003_remove_vege_receipe_ing'),
    ]

    operations = [
        migrations.AddField(
            model_name='vege',
            name='receipe_ingr',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
