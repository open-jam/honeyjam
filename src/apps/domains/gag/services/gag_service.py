from django.contrib.auth.models import User

from apps.domains.gag.constants import GagType
from apps.domains.gag.models import Gag
from apps.domains.gag.repositories import GagRepository
from libs.base.exceptions import NotAllowedAccessException


class GagService:
    @classmethod
    def create_qna(cls, user: User, question: str, answer: str) -> Gag:
        gag = Gag(
            user=user,
            gag_type=GagType.QNA,
            question=question,
            answer=answer,
        )
        gag.save()

        return gag

    @classmethod
    def modify_qna(cls, user: User, gag_id: int, question: str, answer: str) -> Gag:
        gag = GagRepository.get_active_by_id(gag_id)
        if user.id != gag.user_id:
            raise NotAllowedAccessException

        gag.question = question
        gag.answer = answer
        gag.save()

        return gag

    @classmethod
    def delete_qna(cls, user: User, gag_id: int) -> Gag:
        gag = GagRepository.get_active_by_id(gag_id)
        if user.id != gag.user_id:
            raise NotAllowedAccessException

        gag.is_active = False
        gag.save()

        return gag
