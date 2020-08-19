from django.contrib.auth.models import User
from django.test import TestCase

from apps.domains.gag.repositories import GagRepository
from apps.domains.gag.services.gag_service import GagService


class GagServiceTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User(email='test@test.com')
        self.user.save()

    def test_gag_create(self):
        question = 'test-question'
        answer = 'test-answer'
        gag = GagService.create_qna(self.user, question, answer)

        self.assertEqual(gag.user_id, self.user.pk)
        self.assertEqual(gag.question, question)
        self.assertEqual(gag.answer, answer)
        self.assertTrue(gag.is_active)

        gag_from_repository = GagRepository.get_by_id(gag.id)
        self.assertEqual(gag.user_id, gag_from_repository.user_id)
        self.assertEqual(gag.question, gag_from_repository.question)
        self.assertEqual(gag.answer, gag_from_repository.answer)
        self.assertTrue(gag_from_repository.is_active)

    def test_gag_modify(self):
        gag = GagService.create_qna(self.user, 'q', 'a')

        question = 'test-question'
        answer = 'test-answer'

        gag = GagService.modify_qna(self.user, gag.id, question, answer)

        self.assertEqual(gag.user_id, self.user.pk)
        self.assertEqual(gag.question, question)
        self.assertEqual(gag.answer, answer)

        gag_from_repository = GagRepository.get_by_id(gag.id)
        self.assertEqual(gag.user_id, gag_from_repository.user_id)
        self.assertEqual(gag.question, gag_from_repository.question)
        self.assertEqual(gag.answer, gag_from_repository.answer)

    def test_gag_delete(self):
        gag = GagService.create_qna(self.user, 'q2', 'a2')

        gag = GagService.delete_qna(self.user, gag.id)
        self.assertFalse(gag.is_active)
