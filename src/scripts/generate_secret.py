import argparse
import os

from libs.secrets.constants import DEFAULT_SECRET_FILE_CRYPTO_KEY, SECRET_FILE_CRYPTO_KEY_ENV_NAME, SECRET_FILE_NAME
from libs.secrets.secret_generator import SecretGenerator
from libs.secrets.secret_loader import JsonFileSecretLoader

# If this file location changes, you must also change the path below.
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../'))
DEFAULT_DEV_FILE_PATH = os.path.join(ROOT_PATH, f'docs/dev/settings/{SECRET_FILE_NAME}')

args_parser = argparse.ArgumentParser()
args_parser.add_argument('-a', '--action', help='default')
args = args_parser.parse_args()

if args.action == 'default':
    _encrypt_key = os.environ.get(SECRET_FILE_CRYPTO_KEY_ENV_NAME, DEFAULT_SECRET_FILE_CRYPTO_KEY)
    SecretGenerator(ROOT_PATH, JsonFileSecretLoader(DEFAULT_DEV_FILE_PATH), _encrypt_key).generate()

else:
    args_parser.print_help()
