import pytest

from app.core.models import Jedi, Person


pytestmark = [pytest.mark.django_db]


def test_join_just_works():
    assert Jedi.objects.join(first_name=Person.first_name)


def test_join_filtering():
    # Obi-Wan only
    assert Jedi.objects.join(first_name=Person.first_name).count() == 1
