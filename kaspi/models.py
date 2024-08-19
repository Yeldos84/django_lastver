from django.db import models
from django.contrib.auth.models import User


class Good(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


# Create your models here.
class Magazine(models.Model):
    name = models.CharField(max_length=100)
    create_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=100)
    goods = models.ManyToManyField(to=Good,through='MagazineGood', through_fields=('magazine', 'good'))
    staff = models.ManyToManyField(to=User)

    def __str__(self):
        return self.name

class MagazineGood(models.Model):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.magazine.name} = {self.good.name}'
