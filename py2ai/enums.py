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


class AI2Helper:
    pass


class AlignHorizontal(AI2Helper):
    Left = 1
    Right = 2
    Center = 3


class AlignVertical(AI2Helper):
    Top = 1
    Center = 2
    Bottom = 3


class TextAlignment(AI2Helper):
    left = 0
    center = 1
    right = 2


class Dimension(AI2Helper):
    Automatic = -1
    FillParent = -2


Color = int
