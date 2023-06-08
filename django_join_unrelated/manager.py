from django.db.models import Manager

from .query import UnrelatedJoinQuerySet


class UnrelatedJoinManager(Manager.from_queryset(UnrelatedJoinQuerySet)):  # type: ignore[misc]
    pass
