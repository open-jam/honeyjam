import os
from typing import Callable
from uuid import uuid4

from django.utils.deconstruct import deconstructible


@deconstructible
class UploadToPathAndRename:

    def __init__(self, path: str = '', prefix: str = '', original_name_field: str = None, name_generator: Callable = None):
        self._path = path
        self._prefix = prefix
        self._original_name_field = original_name_field
        self._name_generator = name_generator

    def __call__(self, instance, filename):
        # Step 1. 원본 이름 저장 필드가 지정되면 해당 필드에 저장한다.
        if self._original_name_field is not None:
            setattr(instance, self._original_name_field, filename)

        # Step 2. 파일 이름을 만든다.
        if self._name_generator:
            name = self._name_generator(instance, filename)

        else:
            _, ext = os.path.splitext(filename)
            name = f'{uuid4().hex}{ext}'

        # Step 3. 지정된 경로 및 새로운 이름을 만든다.
        return os.path.join(self._path, f'{self._prefix}{name}')
