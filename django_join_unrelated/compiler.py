from typing import List

from django.db.models.sql import compiler
from django.db.models.sql.compiler import SQLCompiler
from django.db.models.sql.constants import INNER
from django.db.models.sql.datastructures import Join

from .exception import JoinError


class JoinField:

    def __init__(self, columns: List[str]):
        self._joining_columns = columns

    def get_joining_columns(self) -> List[List[str]]:
        return [self._joining_columns]

    def get_extra_restriction(self, alias: str, remote_alias: str, *args, **kwargs) -> None:
        pass


class SQLUnrelatedJoinCompiler(SQLCompiler):
    join_cls = Join

    def setup_unrelated_joins(self, join_type: str = INNER, nullable: bool = False, **join_fields) -> None:
        self.setup_query()

        if not self.query.model:
            raise JoinError('Unable to setup joins with no parent model.')

        for from_field, to_field in join_fields.items():
            alias = to_field.field.model._meta.db_table
            join = self.join_cls(
                table_name=alias,
                parent_alias=self.query.model._meta.db_table,
                table_alias=alias,
                join_type=join_type,
                join_field=JoinField([from_field, to_field.field.column]),  # type: ignore[arg-type]
                nullable=nullable,
            )
            self.query.alias_map[alias] = join
            self.query.alias_refcount[alias] = 1


setattr(compiler, 'SQLUnrelatedJoinCompiler', SQLUnrelatedJoinCompiler)
