from django.db import models

from django_join_unrelated import UnrelatedJoinManager


class Person(models.Model):
    first_name = models.CharField('First name', max_length=128)
    last_name = models.CharField('Last name', max_length=128)
    birth_place = models.CharField('Birth place', max_length=128)

    class Meta:
        verbose_name = 'Person'


class Jedi(models.Model):
    first_name = models.CharField('First name', max_length=128)
    last_name = models.CharField('Last name', max_length=128)
    force = models.IntegerField('Force')

    objects = UnrelatedJoinManager()

    class Meta:
        verbose_name = 'Jedi'
