from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    seller_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name= models.CharField(max_length=100)
    price= models.IntegerField()
    desc = models.CharField(max_length=200)
    images= models.ImageField(blank=True, upload_to='images')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('myapp:products')