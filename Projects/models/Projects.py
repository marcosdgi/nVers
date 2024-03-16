from django.db import models
from django.utils import timezone


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='images')

    class Meta:
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name
