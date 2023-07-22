import json
import zipfile
from typing import IO, Dict, List, Optional, Union
from .const import PROPERTIES
from .blockly import BlocklyProject
from .properties import PropertiesDict


class Screen:
    def __init__(self, bky: bytes, scm: bytes, name: str):
        self.name = name
        self.blockly = BlocklyProject.from_xml(bky.decode())
        text = scm.decode()
        self.schema = json.loads(text[text.find('{') : text.rfind('}') + 1])


class AIAProject:
    def __init__(
        self,
        file: Optional[Union[IO[bytes], str]] = None,
        package_name: Optional[str] = None,
        main_name: Optional[str] = None,
        assets: Optional[Dict[str, bytes]] = None,
    ):
        self.file = file
        self.package_name = package_name or f'appinventor.ai_unknown.project'
        self.main_name = main_name or 'Screen1'
        self.assets = assets or {}
        self.screens: List[Screen] = []
        self.properties = PropertiesDict(
            PROPERTIES.format(class_name=self.package_name, main_name=self.main_name)
        )
        self._folder = '/'.join(
            ['src', self.package_name.replace('.', '/'), self.main_name, '']
        )
        if file:
            self.load(file)

    @property
    def app_name(self):
        screen = self.get_screen(self.main_name)
        return screen.schema['Properties']['AppName']

    def get_screen(self, name: str):
        for screen in self.screens:
            if screen.name == name:
                return screen
        raise KeyError(name)

    def load(self, file: Union[IO[bytes], str]):
        self.screens = []
        self.assets = {}
        self.file = file
        with zipfile.ZipFile(file, 'r') as zf:
            with zf.open('youngandroidproject/project.properties') as fprops:
                self.properties = props = PropertiesDict(fprops.read().decode())
            main = props['main']
            self.package_name, _, self.main_name = props['main'].rpartition('.')
            self._folder = _folder = (
                'src/' + main.rpartition('.')[0].replace('.', '/') + '/'
            )
            for info in zf.infolist():
                name = info.filename
                if name.startswith(_folder) and name.endswith('.scm'):
                    scn = Screen(
                        zf.open(name[:-4] + '.bky').read(),
                        zf.open(name).read(),
                        name.rpartition('/')[2][:-4],
                    )
                    self.screens.append(scn)
                if name.startswith('assets/'):
                    asset = name.partition('/')[2]
                    with zf.open(info) as f:
                        self.assets[asset] = f.read()

    def save(self, file: Optional[Union[IO[bytes], str]] = None):
        fout = file or self.file
        if fout is None:
            raise ValueError('No file supplied and no original file found')
        with zipfile.ZipFile(fout, 'w') as zf:
            info = zipfile.ZipInfo('youngandroidproject/project.properties')
            info.file_size = len(self.properties.text.encode())
            with zf.open(info, 'w') as f:
                f.write(self.properties.text.encode())
            for scn in self.screens:
                info = zipfile.ZipInfo(self._folder + scn.name + '.bky')
                data = scn.blockly.to_xml().encode()
                info.file_size = len(data)
                with zf.open(info, 'w') as f:
                    f.write(data)
                info = zipfile.ZipInfo(self._folder + scn.name + '.scm')
                data = b'#|\n$JSON\n' + json.dumps(scn.schema).encode() + b'\n|#'
                info.file_size = len(data)
                with zf.open(info, 'w') as f:
                    f.write(data)
            for asset, value in self.assets.items():
                info = zipfile.ZipInfo('assets/' + asset)
                info.file_size = len(value)
                with zf.open(info, 'w') as f:
                    f.write(value)
        return fout
