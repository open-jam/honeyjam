from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView

from apps.domains.home import urls as home_urls
from sites.urls import views

handler400 = views.handler400
handler403 = views.handler403
handler404 = views.handler404
handler500 = views.handler500

urlpatterns = [
    path('robots.txt', TemplateView.as_view(template_name="www/robots.txt", content_type="text/plain"), name="robots_file"),

    path('', include(home_urls, namespace='home')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
