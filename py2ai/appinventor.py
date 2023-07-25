import base64
import io
import json
import os
import struct
from argparse import ArgumentParser
from typing import Any, Dict, Optional

from requests import Session

from py2ai.aia import AIAProject

GET_PROJECTS_REQUEST = '7|0|4|https://ai2.appinventor.mit.edu/ode/|B8929750FF80B64EC8630BFE7CA29E33|com.google.appinventor.shared.rpc.project.ProjectService|getProjectInfos|1|2|3|4|0|'
MOVE_TO_TRASH_REQUEST = '7|0|5|https://ai2.appinventor.mit.edu/ode/|B8929750FF80B64EC8630BFE7CA29E33|com.google.appinventor.shared.rpc.project.ProjectService|moveToTrash|J|1|2|3|4|1|5|%s|'
DELETE_FROM_TRASH_REQUEST = '7|0|5|https://ai2.appinventor.mit.edu/ode/|B8929750FF80B64EC8630BFE7CA29E33|com.google.appinventor.shared.rpc.project.ProjectService|deleteProject|J|1|2|3|4|1|5|%s|'
LOAD_USER_SETTINGS_REQUEST = '7|0|4|https://ai2.appinventor.mit.edu/ode/|6AE9EFC5B1F4CACA1D6118FD0D90C613|com.google.appinventor.shared.rpc.user.UserInfoService|loadUserSettings|1|2|3|4|0|'
STORE_USER_SETTINGS_REQUEST = '7|0|6|https://ai2.appinventor.mit.edu/ode/|6AE9EFC5B1F4CACA1D6118FD0D90C613|com.google.appinventor.shared.rpc.user.UserInfoService|storeUserSettings|java.lang.String/2004016611|%s|1|2|3|4|1|5|6|'
PERMUTATION = 'E151E553AE14CFBD87645C3CF1A80F2E'


def _b64_decode(s):
    while len(s) % 4:
        s = 'A' + s
    return struct.unpack('>q', base64.b64decode(s, altchars=b'$_')[1:])[0]


def _b64_encode(n):
    return (
        base64.b64encode(b'\0' + struct.pack('>q', n), altchars=b'$_')
        .decode()
        .lstrip('A')
    )


class AppInventor:
    """Handles communication with the App Inventor server (ai2.appinventor.mit.edu)."""

    def __init__(self, cookie: str):
        """
        Create an AppInventor object.
        :param cookie: The "AppInventor" cookie.
        """
        self.session = Session()
        self.cookie = cookie

    @property
    def cookie(self) -> str:
        """The AppInventor cookie"""
        return self.session.cookies['AppInventor']

    @cookie.setter
    def cookie(self, value: str) -> None:
        self.session.cookies['AppInventor'] = value

    def get_projects(self):
        """
        Retrieves a list of projects in this account.
        :return: A list of dictionaries of the form
        `{"id": 12345, "name": "ProjectName"}` that describe the projects.
        """
        r = self.session.post(
            'https://ai2.appinventor.mit.edu/ode/projects',
            data=GET_PROJECTS_REQUEST,
            headers={
                'X-GWT-Permutation': PERMUTATION,
                'Content-Type': 'text/x-gwt-rpc; charset=utf-8',
            },
        )
        r.raise_for_status()
        resp = r.text
        if not resp.startswith('//OK'):
            raise ValueError(resp)
        data = json.loads(resp[4:])[::-1]
        table = data[2]
        projects = []
        for i in range(5, len(data), 7):
            element = data[i : i + 7]
            id_b64 = element[3]
            id = _b64_decode(id_b64)
            name = table[element[5] - 1]
            projects.append({'id': id, 'name': name})
        return projects

    def download_project(self, id: int) -> AIAProject:
        """
        Downloads a given project.
        :param id: The ID of the project.
        :return: The downloaded and loaded AIAProject.
        """
        if isinstance(id, dict):
            id = id['id']
        r = self.session.get(
            f'https://ai2.appinventor.mit.edu/ode/download/project-source/{id}'
        )
        r.raise_for_status()
        buf = io.BytesIO(r.content)
        return AIAProject(buf)

    def move_to_trash(self, id: int) -> None:
        """
        Move a given project to trash.
        :param id: The ID of the project.
        """
        if isinstance(id, dict):
            id = id['id']
        r = self.session.post(
            'https://ai2.appinventor.mit.edu/ode/projects',
            data=MOVE_TO_TRASH_REQUEST % _b64_encode(id),
            headers={
                'X-GWT-Permutation': PERMUTATION,
                'Content-Type': 'text/x-gwt-rpc; charset=utf-8',
            },
        )
        r.raise_for_status()

    def delete_from_trash(self, id: int) -> None:
        """
        Deletes a project from the trash.
        :param id: The ID of the project.
        """
        if isinstance(id, dict):
            id = id['id']
        r = self.session.post(
            'https://ai2.appinventor.mit.edu/ode/projects',
            data=DELETE_FROM_TRASH_REQUEST % _b64_encode(id),
            headers={
                'X-GWT-Permutation': PERMUTATION,
                'Content-Type': 'text/x-gwt-rpc; charset=utf-8',
            },
        )
        r.raise_for_status()

    def upload_project(self, project: AIAProject, name: str) -> Dict[str, Any]:
        """
        Upload a project to the App Inventor server.
        :param project: The project to upload.
        :param name: The name of the project.
        :return: A dictionary of the form `{"id": 12345, "name": "ProjectName"}` that
        describes the created project.
        """
        ai_projects = self.get_projects()
        for ai_project in ai_projects:
            if ai_project['name'] == name:
                self.move_to_trash(ai_project['id'])
                self.delete_from_trash(ai_project['id'])
                break
        buf = io.BytesIO()
        project.save(buf)
        buf.seek(0)
        r = self.session.post(
            f'https://ai2.appinventor.mit.edu/ode/upload/project/{name}',
            files={
                'uploadProjectArchive': (
                    f'{name}.aia',
                    buf,
                    'application/octet-stream',
                )
            },
        )
        r.raise_for_status()
        text = r.text
        start = text.index('[UPLOAD RESPONSE BEGIN]') + 23
        end = text.rindex('[UPLOAD RESPONSE END]')
        text = text[start:end]
        parts = text.split('#DELIM#')
        if parts[0] != 'SUCCESS':
            raise RuntimeError(f'Upload returned status {parts[0]}', text)
        ai_id = int(parts[3])
        ai_name = parts[4]
        return {'id': ai_id, 'name': ai_name}

    def set_autoload_project(self, id: int) -> None:
        """
        Sets a given project to load automatically when the user opens App Inventor in
        their browser.
        :param id: The ID of the project.
        """
        if isinstance(id, dict):
            id = id['id']
        settings = self.get_user_settings()
        settings['GeneralSettings']['AutoloadLastProject'] = 'true'
        settings['GeneralSettings']['CurrentProjectId'] = str(id)
        self.store_user_settings(settings)

    def get_user_settings(self):
        """
        Fetches the user settings.
        :return: The user settings dict.
        """
        r = self.session.post(
            'https://ai2.appinventor.mit.edu/ode/userinfo',
            data=LOAD_USER_SETTINGS_REQUEST,
            headers={
                'X-GWT-Permutation': PERMUTATION,
                'Content-Type': 'text/x-gwt-rpc; charset=utf-8',
            },
        )
        r.raise_for_status()
        resp = r.text
        if not resp.startswith('//OK'):
            raise ValueError(resp)
        data = json.loads(resp[4:])[::-1]
        return json.loads(data[2][0])

    def store_user_settings(self, settings: dict) -> None:
        """
        Stores the user settings.
        :param settings: The user settings dict.
        """
        data = json.dumps(settings, ensure_ascii=True)
        data = data.replace('\\', '\\\\').replace('|', '\\|')
        r = self.session.post(
            'https://ai2.appinventor.mit.edu/ode/userinfo',
            data=STORE_USER_SETTINGS_REQUEST % data,
            headers={
                'X-GWT-Permutation': PERMUTATION,
                'Content-Type': 'text/x-gwt-rpc; charset=utf-8',
            },
        )
        r.raise_for_status()


if __name__ == '__main__':
    ap = ArgumentParser(description='authenticate and manage projects on app inventor')
    ap.add_argument(
        '-S',
        '--session',
        help='session storage file, default "./.ai_session"',
        default='.ai_session',
    )

    sp = ap.add_subparsers(
        metavar='SUBCOMMAND', help='subcommand to execute', required=True
    )

    auth = sp.add_parser('auth', help='log in with your cookie')
    auth.set_defaults(cmd='auth')
    auth.add_argument('cookie', help='the AppInventor cookie')

    ls = sp.add_parser('ls', help='list your projects')
    ls.set_defaults(cmd='ls')

    download = sp.add_parser('download', help='download a project')
    download.set_defaults(cmd='download')
    download.add_argument('id', help='project id to download', type=int)
    download.add_argument('file', help='file to save .aia project')

    upload = sp.add_parser('upload', help='upload a project')
    upload.set_defaults(cmd='upload')
    upload.add_argument('file', help='.aia project to upload')
    upload.add_argument('--name', '-n', help='project name, defaults to file name')
    upload.add_argument(
        '--autoload',
        '-a',
        help='autoload the project in app inventor',
        action='store_true',
    )

    args = ap.parse_args()

    session: str = args.session
    if os.path.exists(session):
        with open(session) as f:
            data = json.load(f)
    else:
        data = {}
    if args.cmd == 'auth':
        cookie: str = args.cookie
        data['appinventor'] = cookie
    elif args.cmd == 'ls':
        ai = AppInventor(data['appinventor'])
        projects = ai.get_projects()
        print('Project count:', len(projects))
        for project in projects:
            name = project['name']
            id = project['id']
            print(f'* {name} ({id})')
    elif args.cmd == 'download':
        id: int = args.id
        file: str = args.file
        ai = AppInventor(data['appinventor'])
        project = ai.download_project(id)
        project.save(file)
    elif args.cmd == 'upload':
        file: str = args.file
        name: Optional[str] = args.name
        autoload: bool = args.autoload
        ai = AppInventor(data['appinventor'])
        if name is None:
            name = os.path.splitext(file)[0]
        project = AIAProject(file)
        ai_project = ai.upload_project(project, name)
        if autoload:
            ai.set_autoload_project(ai_project['id'])
    with open(session, 'w') as f:
        json.dump(data, f)
