import os

from django.core.exceptions import ValidationError
from django.db.models import FilePathField


class RelativeFilePathField(FilePathField):
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value

        return os.path.join(self.path, value[1:] if value[0] == '/' else value)

    def get_db_prep_value(self, value, connection, prepared=False):
        if value is None:
            return None

        if not value.startswith(self.path):
            raise ValidationError

        return value.replace(self.path, '', 1)
