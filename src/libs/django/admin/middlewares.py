from admin_ip_restrictor.middleware import AdminIPRestrictorMiddleware as BaseAdminIPRestrictorMiddleware
from django.conf import settings
from ipware import get_client_ip


class AdminIPRestrictorMiddleware(BaseAdminIPRestrictorMiddleware):
    def __init__(self, get_response=None):
        super().__init__(get_response)

        self.allowed_admin_proxy_count = getattr(settings, 'ALLOWED_ADMIN_PROXY_COUNT', 0)

    def get_ip(self, request):
        client_ip, _ = get_client_ip(request, self.allowed_admin_proxy_count)
        return client_ip
