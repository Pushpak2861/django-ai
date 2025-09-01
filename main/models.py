from django.db import models
from django.conf import settings
# Create your models here.


class Document(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.CASCADE)
    title = models.CharField(default="Title",max_length=30)
    content = models.TextField(blank=True , null=True)
    created_at = models.DateTimeField(auto_now_add=True) # db auto update the field when its added
    updated_at = models.DateTimeField(auto_now=True) # db auto update the field whenever the field is updated

    def save(self , *args , **kwargs):
        super().save(*args,**kwargs)
