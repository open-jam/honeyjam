from django.test import TestCase

from libs.crypto.encrypt import CryptoHelper


class CryptoHelperTestCase(TestCase):
    def setUp(self):
        self.crypto_helper = CryptoHelper('---dummy--key---')

    def test_encrypt_and_decrypt(self):
        plain_text = 'Hello, World'
        encrypted_text = self.crypto_helper.encrypt(plain_text)
        decrypted_text = self.crypto_helper.decrypt(encrypted_text)
        self.assertEqual(plain_text, decrypted_text)
