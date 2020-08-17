from typing import Dict, List


class BaseConstant:
    __slots__ = []

    _LIST = []
    _STRING_MAP = {}
    _PARAM_MAP = {}

    @classmethod
    def get_list(cls) -> List:
        return cls._LIST

    @classmethod
    def get_choices(cls) -> List:
        return [(item, cls._STRING_MAP[item]) for item in cls._LIST]

    @classmethod
    def to_string(cls, item) -> str:
        return cls._STRING_MAP[item]

    @classmethod
    def to_key_from_string(cls, string: str) -> int:
        for k, v in cls._STRING_MAP.items():
            if v == string:
                return k

        raise NotImplementedError(string)

    @classmethod
    def get_string_map(cls) -> Dict:
        return cls._STRING_MAP

    @classmethod
    def get_param_choices(cls):
        return [(cls._PARAM_MAP[item], item) for item in cls._LIST]

    @classmethod
    def to_param(cls, item):
        return cls._PARAM_MAP[item]

    @classmethod
    def to_key_from_param(cls, string: str) -> int:
        for k, v in cls._PARAM_MAP.items():
            if v == string:
                return k

        raise NotImplementedError(string)
