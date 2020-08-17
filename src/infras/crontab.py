import os
import urllib.request

from django.core.management import call_command
from uwsgidecorators import timer, cron

from libs.deploy.deployer import Deployer


@timer(10)
def self_kill_if_update_available(signum: int):
    Deployer.run()


@timer(10)
def ping_healthcheck(signum: int):
    hc_ping_token = os.environ.get('HC_PING_TOKEN', None)
    if hc_ping_token is None:
        return

    urllib.request.urlopen(f'https://hc-ping.com/{hc_ping_token}')


@cron(0, 0, 0, -1, -1)
def clearsessions(signum: int):
    call_command('clearsessions')
