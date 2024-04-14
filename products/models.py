from django.db import models
from django.conf import settings

# Create your models here.


class Products(models.Model):
    title = models.CharField(max_length=(50))
    content = models.TextField()
    add_date= models.DateTimeField(auto_now_add=True)
    edit_date= models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True)
