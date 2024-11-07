from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=255,  default="Nairobi")


    def __str__(self):
        return self.name