import json
import zipfile
from typing import IO, Any, Dict, List, Optional, Union

from .blockly import BlocklyProject
from .const import PROPERTIES
from .properties import PropertiesDict


class Screen:
    """Represents a screen in a .aia project."""

    def __init__(self, bky: bytes, scm: bytes, name: str) -> None:
        """
        Create a new Screen.
        :param bky: The raw data read from the .bky file. This is the XML of the blocks.
        :param scm: The raw data read from the .scm file. This is the schema.
        :param name: The name of the screen.
        """
        self.name = name
        self.blockly = BlocklyProject.from_xml(bky.decode())
        text = scm.decode()
        self.schema: Dict[str, Any] = json.loads(
            text[text.find('{') : text.rfind('}') + 1]
        )


class AIAProject:
    """Represents a .aia project."""

    def __init__(
        self,
        file: Optional[Union[IO[bytes], str]] = None,
        package_name: Optional[str] = None,
        main_name: Optional[str] = None,
        assets: Optional[Dict[str, bytes]] = None,
    ) -> None:
        """
        Create a new AIAProject. You should supply either "file" or everything else.
        :param file: The file to read the data from, or None if this is a new project.
        :param package_name: The Java-style package name of the project. Usually in the
        format "appinventor.ai_username.project_name". Defaults to
        "appinventor.ai_unknown.project".
        :param main_name: The name of the main screen. Defaults to "Screen1".
        :param assets: A dictionary of assets to include in the project.
        """
        self.file = file
        self.package_name = package_name or f'appinventor.ai_unknown.project'
        self.main_name = main_name or 'Screen1'
        self.assets = assets or {}
        self.screens: List[Screen] = []
        self.properties = PropertiesDict(
            PROPERTIES.format(class_name=self.package_name, main_name=self.main_name)
        )
        self._folder = '/'.join(['src', self.package_name.replace('.', '/'), ''])
        if file:
            self.load(file)

    @property
    def app_name(self) -> str:
        """The app name as written in the main screen"""
        screen = self.get_screen(self.main_name)
        return screen.schema['Properties']['AppName']

    def get_screen(self, name: str) -> Screen:
        """
        Retrieves a screen from the project.
        :param name: The name of the screen.
        :return: The Screen with the given name.
        """
        for screen in self.screens:
            if screen.name == name:
                return screen
        raise KeyError(name)

    def load(self, file: Union[IO[bytes], str]) -> None:
        """
        Load the project. This will replace the current project.
        :param file: The file to load from.
        """
        self.screens = []
        self.assets = {}
        self.file = file
        with zipfile.ZipFile(file, 'r') as zf:
            with zf.open('youngandroidproject/project.properties') as fprops:
                self.properties = props = PropertiesDict(fprops.read().decode())
            self.package_name, _, self.main_name = props['main'].rpartition('.')
            self._folder = _folder = 'src/' + self.package_name.replace('.', '/') + '/'
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

    def save(
        self, file: Optional[Union[IO[bytes], str]] = None
    ) -> Union[IO[bytes], str]:
        """
        Save the project.
        :param file: The file to save to. If not given, saves to the last loaded file.
        :return: The file.
        """
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
