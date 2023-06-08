from django.db import models

from django_join_unrelated import UnrelatedJoinManager


class User(models.Model):
    name = models.CharField('First name', max_length=128)

    class Meta:
        verbose_name = 'User'


class Person(models.Model):
    name = models.CharField('First name', max_length=128)

    objects = UnrelatedJoinManager()

    class Meta:
        verbose_name = 'Person'
