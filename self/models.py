from django.db import models

# Create your models here.
class Self(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateField()
    image = models.ImageField(upload_to='self/images/')


    #def __str__(self):
    #   return self.title
