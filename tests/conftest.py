import pytest

from app.core.models import Jedi, Person


@pytest.fixture(scope='session')
def _session_db(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        yield


@pytest.fixture(scope='session', autouse=True)
def _setup_models(_session_db):
    Person.objects.create(first_name='Padme', last_name='Amidala', birth_place='Naboo')
    Person.objects.create(first_name='Obi-Wan', last_name='Kenobi', birth_place='Stewjon')
    Jedi.objects.create(first_name='Obi-Wan', last_name='Kenobi', force=100)
    Jedi.objects.create(first_name='Mace', last_name='Windu', force=80)
