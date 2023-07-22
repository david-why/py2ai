from requests import Session
import json, base64, struct, io
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
    r = base64.b64decode(s, altchars=b'$_')
    return struct.unpack('l', r[::-1][:-1])[0]


def _b64_encode(n):
    return (
        base64.b64encode(b'\0' + struct.pack('>q', n), altchars=b'$_')
        .decode()
        .lstrip('A')
    )
    r = base64.b64encode(r, altchars=b'$_').decode()
    return r.lstrip('A')


class AppInventor:
    def __init__(self, cookie: str):
        self.session = Session()
        self.session.cookies['AppInventor'] = cookie

    def get_projects(self):
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

    def download_project(self, id: int):
        if isinstance(id, dict):
            id = id['id']
        r = self.session.get(
            f'https://ai2.appinventor.mit.edu/ode/download/project-source/{id}'
        )
        r.raise_for_status()
        buf = io.BytesIO(r.content)
        return AIAProject(buf)

    def move_to_trash(self, id: int):
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

    def delete_from_trash(self, id: int):
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

    def upload_project(self, project: AIAProject, name: str):
        ai_projects = self.get_projects()
        for ai_project in ai_projects:
            if ai_project['name'] == name:
                self.move_to_trash(ai_project['id'])
                self.delete_from_trash(ai_project['id'])
                break
        buf = io.BytesIO()
        project.save(buf)
        buf.seek(0)
        open('test.out', 'wb').write(buf.getvalue())
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

    def set_autoload_project(self, id: int):
        if isinstance(id, dict):
            id = id['id']
        settings = self.get_user_settings()
        settings['GeneralSettings']['AutoloadLastProject'] = 'true'
        settings['GeneralSettings']['CurrentProjectId'] = str(id)
        self.store_user_settings(settings)

    def get_user_settings(self):
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

    def store_user_settings(self, settings: dict):
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
