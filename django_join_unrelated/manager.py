from django.db.models import Manager

from .query import JoinQuerySet


class JoinManager(Manager.from_queryset(JoinQuerySet)):  # type: ignore[misc]
    pass
