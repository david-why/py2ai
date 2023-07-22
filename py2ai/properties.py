from typing import Dict


class PropertiesDict(Dict[str, str]):
    def __init__(self, text: str) -> None:
        for line in text.splitlines():
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            key, _, value = line.partition('=')
            key = key.strip()
            value = value.strip()
            self[key] = value

    @property
    def text(self) -> str:
        s = ''
        for key, value in self.items():
            s += f'{key}={value}\n'
        return s.strip()
