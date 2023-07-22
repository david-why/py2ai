from enum import Enum


class Instant:
    pass


class AI2Enum(Enum):
    pass


class FileScope(AI2Enum):
    App = 'App'
    Asset = 'Asset'
    Cache = 'Cache'
    Legacy = 'Legacy'
    Private = 'Private'
    Shared = 'Shared'


Color = int
