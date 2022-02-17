from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    sourceLink = models.CharField(max_length=200, null=True, blank=True)
    def __str__ (self):
        return self.name