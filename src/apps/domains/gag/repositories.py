from typing import List

from apps.domains.gag.models import Gag
from libs.django.db.models.base_repository import BaseRepository


class GagRepository(BaseRepository):
    model_class = Gag

    @classmethod
    def find_active(cls) -> List[Gag]:
        return cls.get_queryset().filter(is_active=True).order_by('-id')
