from django.contrib.auth.models import User

from apps.domains.gag.constants import GagType
from apps.domains.gag.models import Gag


class GagCreateService:
    @classmethod
    def create_qna(cls, user: User, question: str, answer: str):
        gag = Gag(
            user=user,
            gag_type=GagType.QNA,
            question=question,
            answer=answer,
        )
        gag.save()

        return gag
