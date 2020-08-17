from ipware.ip import get_ip
from ipware.utils import is_private_ip


def is_private_ip_from_request(request) -> bool:
    return is_private_ip(get_ip(request))
