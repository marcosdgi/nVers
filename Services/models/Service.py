from django.db import models


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images')

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.name
