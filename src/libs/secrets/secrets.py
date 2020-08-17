import os

from libs.secrets.constants import DEFAULT_SECRET_FILE_CRYPTO_KEY, SECRET_FILE_CRYPTO_KEY_ENV_NAME
from libs.secrets.secret_handler import SecretHandler

# If this file location changes, you must also change the path below.
_root_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../../'))
# In production, the key below must be changed.
_decrypt_key = os.environ.get(SECRET_FILE_CRYPTO_KEY_ENV_NAME, DEFAULT_SECRET_FILE_CRYPTO_KEY)

Secrets = SecretHandler.instance(_root_path, _decrypt_key)
