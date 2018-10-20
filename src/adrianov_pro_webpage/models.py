from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Page(models.Model):
    question = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    content = models.TextField()