from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.db.models import Manager


class EqualizeMixin:
    equal_fields = ()

    def __eq__(self, other):
        equal_fields = self._get_equal_fields()
        for field in equal_fields:
            if getattr(self, field) != getattr(other, field):
                return False
        return True

    def _get_equal_fields(self):
        if not self.equal_fields:
            raise NotImplementedError()

        return self.equal_fields

    def merge(self, other):
        equal_fields = self._get_equal_fields()
        for field in equal_fields:
            if getattr(self, field) != getattr(other, field):
                setattr(self, field, getattr(other, field))


class ChangeMixin:
    def _change(self, **kwargs):
        is_changed = False

        for key, value in kwargs.items():
            if getattr(self, key) == value:
                continue

            setattr(self, key, value)
            is_changed = True

        return is_changed


class BaseModel(ChangeMixin, models.Model):
    create_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='등록일')
    update_time = models.DateTimeField(auto_now=True, verbose_name='수정일')

    objects = Manager()

    equal_fields = ()

    class Meta:
        abstract = True


class BaseUserModel(BaseModel, AbstractUser):
    class Meta:
        abstract = True
