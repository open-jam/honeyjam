import json
import os

from libs.crypto.encrypt import CryptoHelper
from libs.secrets.constants import SECRET_FILE_NAME
from libs.secrets.exceptions import ImproperlyConfigured


class SecretHandler:
    _instance = None

    def __init__(self, root_path: str, decrypt_key: str):
        self._decrypt_key = decrypt_key
        self._root_path = root_path
        self._secrets = {}
        self._load()

    @classmethod
    def instance(cls, root_path: str, decrypt_key: str) -> 'SecretHandler':
        if cls._instance is None:
            cls._instance = cls(root_path, decrypt_key)

        elif decrypt_key and decrypt_key != cls._instance.decrypt_key:
            raise ImproperlyConfigured('Decrypt key is different from was set previously.')

        return cls._instance

    def get(self, key: str) -> str:
        try:
            return self._secrets[key]

        except KeyError:
            raise ImproperlyConfigured('Set the {} environment variable!'.format(key))

    def _load(self) -> None:
        file_path = os.path.join(self._root_path, SECRET_FILE_NAME)
        self._secrets = json.loads(self._decrypt(self._file_load(file_path)))

    def _decrypt(self, string: str) -> str:
        return CryptoHelper(self._decrypt_key).decrypt(string)

    @staticmethod
    def _file_load(file_path: str):
        try:
            with open(file_path) as file:
                return file.read()

        except (OSError, IOError):
            raise ImproperlyConfigured('There is no setting file %s' % file_path)
