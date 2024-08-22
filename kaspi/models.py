import datetime

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from django.contrib.postgres.fields import DateTimeRangeField, ArrayField

class Good(models.Model):
    name = models.CharField(max_length=100)
    discription = models.CharField(max_length=100)
    price = models.IntegerField()
    reserving = DateTimeRangeField(verbose_name='Reserving time', default=(datetime.datetime.now(), '2024-12-31'))
    array_field = ArrayField(base_field=models.CharField(max_length=10), default=[])


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


# Signal
@receiver(post_save, sender=Good)
def post_save_dispatcher(sender, **kwargs):
    data = kwargs['instance']
    print(f'{data.name} is created!')

@receiver(post_delete, sender=Good)
def post_delete_dispatcher(sender, **kwargs):
    data = kwargs['instance']
    print(f'{data.name} is deleted!')