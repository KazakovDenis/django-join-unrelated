from django.db import models

from django_join_unrelated import UnrelatedJoinManager


class User(models.Model):
    first_name = models.CharField('First name', max_length=128)
    last_name = models.CharField('Last name', max_length=128)
    birth_date = models.DateTimeField('Birth date')

    class Meta:
        verbose_name = 'User'


class Person(models.Model):
    first_name = models.CharField('First name', max_length=128)
    last_name = models.CharField('Last name', max_length=128)
    salary = models.PositiveIntegerField('Salary')

    objects = UnrelatedJoinManager()

    class Meta:
        verbose_name = 'Person'
