from drf_yasg import openapi
from drf_yasg.codecs import SaneYamlDumper, _OpenAPICodec
from drf_yasg.renderers import _SpecRenderer
from drf_yasg.views import get_schema_view
from ruamel import yaml

SchemaView = get_schema_view(
    info=openapi.Info(
        title='',
        default_version='v1',
    ),
)


def yaml_sane_dump(data):
    return yaml.dump(data, Dumper=SaneYamlDumper, default_flow_style=False, allow_unicode=True)


class UnicodeCodec(_OpenAPICodec):
    media_type = 'application/yaml'

    def _dump_dict(self, spec):
        return yaml_sane_dump(spec)


class YamlUnicodeRenderer(_SpecRenderer):
    media_type = 'application/yaml'
    format = '.yaml'
    codec_class = UnicodeCodec


class CustomSchemaView(SchemaView):
    renderer_classes = (YamlUnicodeRenderer,)

    @classmethod
    def without_ui(cls, cache_timeout=0, cache_kwargs=None):
        return cls.as_cached_view(cache_timeout, cache_kwargs, renderer_classes=cls.renderer_classes)
