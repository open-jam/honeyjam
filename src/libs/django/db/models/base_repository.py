from typing import Callable, Dict, List, Optional, Type

from django.db.models import Manager

from libs.django.db.models.base_model import BaseModel

DEFAULT_LIMIT = 1000


class BaseRepository:
    model_class: Type[BaseModel]

    @classmethod
    def get_queryset(cls) -> Manager:
        return cls.model_class.objects

    @classmethod
    def create(cls, entities: List, is_bulk: bool = False, bulk_bundle_count: int = 1000):
        if is_bulk:
            # Be careful! There is no pk
            cls.get_queryset().bulk_create(entities, batch_size=bulk_bundle_count)

        else:
            for entity in entities:
                entity.save(force_insert=True)

        return entities

    @staticmethod
    def update(entities: List, update_fields: List = None):
        for entity in entities:
            entity.save(update_fields=update_fields)

    @classmethod
    def delete(cls, entities: List):
        for entity in entities:
            entity.delete()

    @classmethod
    def delete_by_ids(cls, ids: List):
        cls.get_queryset().filter(id__in=ids).delete()

    @classmethod
    def soft_delete(cls, entities: List):
        for entity in entities:
            entity.is_deleted = True
            entity.save(update_fields=['is_deleted', ])

    @classmethod
    def find(cls, offset: int = 0, limit: int = DEFAULT_LIMIT) -> List:
        return cls.get_queryset().all().order_by('id')[offset:offset + limit]

    @classmethod
    def find_all(cls) -> List:
        return cls.get_queryset().all()

    @classmethod
    def find_by_ids(cls, ids: List) -> List:
        return cls.get_queryset().filter(id__in=ids)

    @classmethod
    def get_by_id(cls, model_id: int, with_select_for_update: bool = False):
        qs = cls.get_queryset()
        if with_select_for_update:
            qs = qs.select_for_update()
        return qs.get(id=model_id)

    @classmethod
    def get_or_create(cls, defaults: Optional[Dict] = None, **kwargs):
        return cls.get_queryset().get_or_create(defaults=defaults, **kwargs)

    @classmethod
    def update_or_create(cls, defaults: Optional[Dict] = None, **kwargs):
        return cls.get_queryset().update_or_create(defaults=defaults, **kwargs)

    @classmethod
    def roll(cls, stop_condition_lambda: Callable, limit: int = DEFAULT_LIMIT):
        entities = cls.find(0, limit)
        target_ids = []
        for entity in entities:
            if stop_condition_lambda(entity):
                break
            target_ids.append(entity.pk)
        cls.delete_by_ids(target_ids)
