from typing import List

from apps.domains.gag.models import Gag
from libs.django.db.models.base_repository import BaseRepository


class GagRepository(BaseRepository):
    model_class = Gag

    @classmethod
    def find_active(cls, offset: int, limit: int) -> List[Gag]:
        return cls.get_queryset().filter(is_active=True).order_by('-id')[offset:offset + limit]

    @classmethod
    def get_active_by_id(cls, gag_id: int) -> Gag:
        return cls.get_queryset().get(is_active=True, id=gag_id)
