from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=400, verbose_name='Malumot turi')
    def __str__(self):
        return self.name

class Malumot(models.Model):
    name = models.CharField(max_length=400, verbose_name='malumot')
    raqami = models.CharField(max_length=4, verbose_name='raqami')
    turi = models.ForeignKey(Category, on_delete=models.PROTECT)
