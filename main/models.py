from django.db import models

# Create your models here.
from django.db import models

class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    query = models.TextField()

    def __str__(self):
        return self.name

