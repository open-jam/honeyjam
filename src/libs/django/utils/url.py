import urllib.parse
from typing import Dict

from django.urls import reverse


def reverse_with_query(view_name: str, kwargs: Dict = None, query_kwargs: Dict = None):
    url = reverse(view_name, kwargs=kwargs)

    if not query_kwargs:
        return url

    return f'{url}?{urllib.parse.urlencode(query_kwargs)}'
