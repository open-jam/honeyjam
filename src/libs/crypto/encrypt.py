import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class CryptoHelper:
    def __init__(self, key: str):
        self._key: bytes = key.encode()
        self._bs: int = 16

    def encrypt(self, message: str) -> str:
        message = message.encode()
        raw = self._pad(message)
        encryptor = self._get_cipher().encryptor()
        enc = encryptor.update(raw) + encryptor.finalize()

        return base64.b64encode(enc).decode('utf-8')

    def decrypt(self, enc: str) -> str:
        enc = base64.b64decode(enc)
        decryptor = self._get_cipher().decryptor()
        dec = decryptor.update(enc) + decryptor.finalize()
        return self._unpad(dec).decode('utf-8')

    def _get_cipher(self):
        return Cipher(algorithms.AES(self._key), modes.CBC(self._get_iv()), backend=default_backend())

    def _get_iv(self) -> bytes:
        return (chr(0) * self._bs).encode()

    def _pad(self, string: bytes) -> bytes:
        return string + (self._bs - len(string) % self._bs) * chr(self._bs - len(string) % self._bs).encode()

    @staticmethod
    def _unpad(byte_string: bytes) -> bytes:
        return byte_string[:-ord(byte_string[len(byte_string) - 1:])]
