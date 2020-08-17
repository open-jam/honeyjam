import json
import os
import subprocess

from requests import get

from libs.utils.slack import slack_notify


class Deployer:
    boot_up = False

    @classmethod
    def run(cls):
        # 일단 하드코딩으로 작성한다.
        work_dir = os.environ['WORK_DIR']

        # Step 1. Local hash json 읽기
        with open(f'{work_dir}/hash.txt') as json_file:
            local_data = json.load(json_file)
        local_hash = local_data['commit']['sha']

        # Step 2. 현재 github hash json 가져오기
        github_repo = os.environ['GITHUB_REPO']
        github_owner = os.environ['GITHUB_OWNER']
        github_access_token = os.environ['GITHUB_ACCESS_TOKEN']
        url = f'https://api.github.com/repos/{github_owner}/{github_repo}/branches/master'

        headers = {'Authorization': f'token {github_access_token}', 'Accept': 'application/vnd.github.v3+json'}
        res = get(url, headers=headers)
        current_hash = res.json()
        current_hash = current_hash['commit']['sha']

        if not cls.boot_up:
            cls.boot_up = True
            slack_notify(channel='#deploy', attachments=[{
                'color': '#36a64f',
                'title': '배포 완료',
                'title_link': f'https://github.com/{github_owner}/{github_repo}/commit/{current_hash}',
                'fallback': '배포완료 알림',
                'text': '배포가 완료되었습니다.'
            }])

        # Step 3. 새버전이 없으면 아무일도 하지 않는다.
        if local_hash == current_hash:
            return

        slack_notify('#deploy', '[배포] 배포가 시작됩나다.')

        # Step 4. 새로운 버젼이 나왔으면 설치학고 reload
        subprocess.call('/deploy/deploy-master.sh', cwd=work_dir, shell=True)
        subprocess.call('make install-package', cwd=work_dir, shell=True)
        subprocess.call('make build', cwd=work_dir, shell=True)
        subprocess.call('make migrate', cwd=work_dir, shell=True)

        # pylint:disable=import-error, import-outside-toplevel
        import uwsgi
        uwsgi.reload()
