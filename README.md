# django-join-unrelated
![Python version](https://img.shields.io/badge/Python-3.8%2B-blue)
[![Tests](https://github.com/KazakovDenis/django-join-unrelated/actions/workflows/cicd.yml/badge.svg)](https://github.com/KazakovDenis/django-join-unrelated/actions/workflows/cicd.yml)

### Use SQL Join with Django ORM models having no relations.

If you have models in your project that share the same data but have no relations, 
you might face a situation when you need to join them. But Django does not provide 
this functionality yet.
  
With `django-join-unrelated` you can do the following 
(models defined [here](https://github.com/KazakovDenis/django-join-unrelated/blob/main/app/core/models.py)):
```python
from app.core.models import Jedi, Person

Person.objects.create(first_name='Padme', last_name='Amidala', birth_place='Naboo')
Person.objects.create(first_name='Obi-Wan', last_name='Kenobi', birth_place='Stewjon')
Jedi.objects.create(first_name='Obi-Wan', last_name='Kenobi', force=100)
Jedi.objects.create(first_name='Mace', last_name='Windu', force=80)

Jedi.objects.join(first_name=Person.first_name).values_list('first_name')
# <UnrelatedJoinQuerySet [('Obi-Wan',)]>

print(Jedi.objects.join(first_name=Person.first_name).values_list('first_name').query)
# SELECT "core_jedi"."first_name" FROM "core_jedi" INNER JOIN core_person ON ("core_jedi"."first_name" = core_person."first_name")
```

`django-join-unrelated` tries to keep all QuerySet power where it is possible:
```python
Jedi.objects.join(first_name=Person.first_name).filter(last_name='Kenobi')
# <UnrelatedJoinQuerySet [<Jedi: Jedi object (1)>]>

Jedi.objects.join(first_name=Person.first_name).filter(last_name='Windu')
# <UnrelatedJoinQuerySet []>
```

## Installation
You can install `django-join-unrelated` using pip:

```
pip install django-join-unrelated
```

## Usage
Just import `UnrelatedJoinManager` and set it as an attribute to your models:

```python
from django.db import models
from django_join_unrelated import UnrelatedJoinManager

class Jedi(models.Model):
    first_name = models.CharField('First name', max_length=128)
    last_name = models.CharField('Last name', max_length=128)
    force = models.IntegerField('Force')

    objects = UnrelatedJoinManager()

    class Meta:
        verbose_name = 'Jedi'
```