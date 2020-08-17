from infras.network.constants.api_status_code import ApiStatusCodes
from infras.network.constants.http_status_code import HttpStatusCodes
from libs.base.exceptions import ErrorException
from libs.base.test_case import BaseTestCase as TestCase
from libs.django.views.api.mixins import ResponseMixin


class ResponseMixinTestCase(TestCase):

    def setUp(self):
        class Example(ResponseMixin):
            pass

        self.mixin_object = Example()

    def test_make_code(self):
        ok_status = self.mixin_object.make_response_code(ApiStatusCodes.C_200_OK)
        self.assertFalse(ok_status.has_code())
        self.assertIsNone(ok_status.get_code())
        self.assertEqual(ok_status.get_status(), HttpStatusCodes.C_200_OK)

        ok_status_with_message_status = self.mixin_object.make_response_code(ApiStatusCodes.C_200_OK, 'success')
        self.assertTrue(ok_status_with_message_status.has_message())
        self.assertIsNotNone(ok_status_with_message_status.get_message())
        self.assertEqual(ok_status_with_message_status.get_status(), HttpStatusCodes.C_200_OK)

        custom_code_status = self.mixin_object.make_response_code(ApiStatusCodes.X_400_DUPLICATE_API)
        self.assertTrue(custom_code_status.has_code())
        self.assertIsNotNone(custom_code_status.get_code())
        self.assertEqual(custom_code_status.get_status(), HttpStatusCodes.C_400_BAD_REQUEST)

    def test_make_last_modified(self):
        _tmp_last_modified = 1000
        _tmp_e_tag = 'tagtag'

        last_modified = self.mixin_object.make_last_modified(last_modified=_tmp_last_modified, e_tag=_tmp_e_tag)
        self.assertEqual(last_modified.last_modified, _tmp_last_modified)
        self.assertEqual(last_modified.e_tag, _tmp_e_tag)

        empty_last_modified = self.mixin_object.make_last_modified()
        self.assertIsNone(empty_last_modified.last_modified)
        self.assertIsNone(empty_last_modified.e_tag)

    def test_success_response(self):
        with self.assertRaises(ErrorException):
            self.mixin_object.success_response(data={'message': 'keyword exception test'})

        response = self.mixin_object.success_response(data={'echo_text': 'textext'})
        self.assertDictEqual(response.data, {'echo_text': 'textext'})
        self.assertEqual(response.status_code, HttpStatusCodes.C_200_OK)

        response_with_message = self.mixin_object.success_response(
            data={'echo_text': 'textext'},
            response_code=self.mixin_object.make_response_code(ApiStatusCodes.C_201_CREATED, 'created')
        )
        self.assertDictEqual(response_with_message.data, {'echo_text': 'textext', 'message': 'created'})
        self.assertEqual(response_with_message.status_code, HttpStatusCodes.C_201_CREATED)

    def test_fail_response(self):
        response = self.mixin_object.fail_response(
            response_code=self.mixin_object.make_response_code(ApiStatusCodes.C_400_BAD_REQUEST)
        )
        self.assertDictEqual(response.data, {})
        self.assertEqual(response.status_code, HttpStatusCodes.C_400_BAD_REQUEST)

        response_with_code_and_msg = self.mixin_object.fail_response(
            response_code=self.mixin_object.make_response_code(ApiStatusCodes.X_400_DUPLICATE_API, 'duplicated')
        )
        self.assertDictEqual(response_with_code_and_msg.data, {'message': 'duplicated', 'code': 'DUPLICATE_API_CALL'})
        self.assertEqual(response_with_code_and_msg.status_code, HttpStatusCodes.C_400_BAD_REQUEST)
