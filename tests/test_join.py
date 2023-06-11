import pytest

from app.core.models import Jedi, Person
from django_join_unrelated.exception import JoinError


pytestmark = [pytest.mark.django_db]


def test_join_just_works():
    assert Jedi.objects.join(first_name=Person.first_name)


def test_join_filtering():
    # Obi-Wan only
    assert Jedi.objects.join(first_name=Person.first_name).count() == 1


def test_join_on_self_forbidden():
    with pytest.raises(JoinError):
        Jedi.objects.join(first_name=Jedi.first_name)
