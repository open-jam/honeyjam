import reversion
from django.contrib.auth.models import User
from django.db import models

from apps.domains.gag.constants import GagType
from libs.django.db.models.base_model import BaseModel


@reversion.register()
class Gag(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_gag', verbose_name='유저')

    gag_type = models.IntegerField(choices=GagType.get_choices(), default=GagType.QNA, verbose_name='개그 타입')

    question = models.TextField(null=True, blank=True, verbose_name='문')
    answer = models.TextField(null=True, blank=True, verbose_name='답')

    is_active = models.BooleanField(default=True, verbose_name='활성화 여부')

    class Meta:
        db_table = 'gag'
        verbose_name = '개그'
        verbose_name_plural = '개그 목록'
