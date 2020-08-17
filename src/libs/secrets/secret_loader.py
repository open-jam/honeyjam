import json
from typing import Dict


class BaseSecretLoader:
    def get_secrets(self) -> Dict:
        raise NotImplementedError


class JsonFileSecretLoader(BaseSecretLoader):
    def __init__(self, secret_file_path: str):
        self._secret_file_path = secret_file_path

    def get_secrets(self) -> Dict:
        with open(self._secret_file_path) as file:
            return json.loads(file.read())
