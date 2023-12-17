from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete
import os
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
class Vege(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name= models.CharField(max_length=100)
    receipe_desc = models.TextField()
    receipe_img = models.ImageField(upload_to='receipe')
    receipe_ingr = models.TextField(default=timezone.now, null=True)

@receiver(pre_delete, sender=Vege)
def delete_subcategory_images(sender, instance, **kwargs):
    image_path = os.path.join(settings.MEDIA_ROOT, str(instance.receipe_img))
    if os.path.exists(image_path):
        os.remove(image_path)
