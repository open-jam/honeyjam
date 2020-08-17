import os
import uuid


def upload_to(prefix: str):
    def _upload_to(instance, filename: str):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join(prefix, filename)

    return _upload_to
