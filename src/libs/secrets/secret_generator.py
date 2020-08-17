import json
import os

from libs.crypto.encrypt import CryptoHelper
from libs.secrets.constants import SECRET_FILE_NAME
from libs.secrets.secret_loader import BaseSecretLoader


class SecretGenerator:
    def __init__(self, root_path: str, secret_loader: BaseSecretLoader, encrypt_key: str):
        self._encrypt_key = encrypt_key
        self._root_path = root_path
        self._secret_loader = secret_loader
        self._secrets = {}

    def generate(self) -> None:
        self._load_secrets()
        self._merge_with_env()
        self._save_secrets()

    def _load_secrets(self) -> None:
        self._secrets = self._secret_loader.get_secrets()

    def _merge_with_env(self) -> None:
        secrets = {}
        for key in self._secrets.keys():
            secrets[key] = os.environ[key.upper()] if key.upper() in os.environ else self._secrets[key]

        self._secrets = secrets

    def _save_secrets(self) -> None:
        self._save_file(SECRET_FILE_NAME, self._encrypt(json.dumps(self._secrets)))

    def _save_file(self, file_name: str, content: str) -> None:
        file_path = os.path.join(self._root_path, file_name)
        with open(file_path, 'w') as file:
            file.write(content)

    def _encrypt(self, string: str) -> str:
        return CryptoHelper(self._encrypt_key).encrypt(string)
