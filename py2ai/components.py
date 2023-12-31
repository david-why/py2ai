from . import enums
from typing import Any, Callable, ClassVar

class Component:
    __data__: ClassVar[dict]

    def __init__(self, *, children=None, **kwargs):
        self._children = children
        for prop in self.__data__['properties']:
            if not prop['bo']:
                setattr(self, prop['name'], kwargs.pop(prop['name']))
        if kwargs:
            raise ValueError(kwargs)

class Button(Component):
    """Button with the ability to detect clicks. Many aspects of its appearance can be changed, as well
as whether it is clickable (Enabled). Its properties can be changed in the Designer or in the
Blocks Editor."""
    __data__ = {'desc': 'Button with the ability to detect clicks. Many aspects of its appearance can be changed, as well\nas whether it is clickable (Enabled). Its properties can be changed in the Designer or in the\nBlocks Editor.', 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the Button's background color as an alpha-red-green-blue\ninteger.  If an Image has been set, the color\nchange will not be visible until the Image is removed."}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the Button should be active and clickable.'}, {'name': 'FontBold', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the text of the Button should be bold.\nSome fonts do not support bold.'}, {'name': 'FontItalic', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the text of the Button should be italic.\nSome fonts do not support italic.'}, {'name': 'FontSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text font size of the Button, measured in sp(scale-independent pixels).'}, {'name': 'FontTypeface', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the text font face of the Button as default, serif, sans\nserif, monospace, or custom font typeface. To add a custom typeface,\nupload a .ttf file to the project's media."}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the Button's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the Button's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Image', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the path of the Button's image. If there is both an Image and a\nBackgroundColor specified, only the Image will be visible."}, {'name': 'Shape', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies the shape of the Button. The valid values for this property are 0 (default),\n1 (rounded), 2 (rectangle), and 3 (oval). The Shape will not be visible if an\nImage is used.'}, {'name': 'ShowFeedback', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies if a visual feedback should be shown when a Button with an assigned\nImage is pressed.'}, {'name': 'Text', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text displayed by the Button.'}, {'name': 'TextAlignment', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the alignment of the Button's text. Valid values are:\n0 (normal; e.g., left-justified if text is written left to right),\n1 (center), or\n2 (opposite; e.g., right-justified if text is written left to right)."}, {'name': 'TextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text color of the Button as an alpha-red-green-blue\ninteger.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the Button should be visible on the screen.  Value is true\nif the Button is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the Button, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the Button as a percentage\nof the Screen's Width."}], 'events': [{'name': 'Click', 'args': [], 'desc': 'Indicates that the user tapped and released the Button.'}, {'name': 'GotFocus', 'args': [], 'desc': 'Indicates the cursor moved over the Button so it is now possible\nto click it.'}, {'name': 'LongClick', 'args': [], 'desc': 'Indicates that the user held the Button down.'}, {'name': 'LostFocus', 'args': [], 'desc': 'Indicates the cursor moved away from the Button so it is now no\nlonger possible to click it.'}, {'name': 'TouchDown', 'args': [], 'desc': 'Indicates that the Button was pressed down.'}, {'name': 'TouchUp', 'args': [], 'desc': 'Indicates that the Button has been released.'}], 'methods': []}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., Enabled: bool=..., FontBold: bool=..., FontItalic: bool=..., FontSize: int=..., FontTypeface: str=..., Height: int=..., Image: str=..., Shape: int=..., ShowFeedback: bool=..., Text: str=..., TextAlignment: int=..., TextColor: enums.Color=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the Button's background color as an alpha-red-green-blue
integer.  If an Image has been set, the color
change will not be visible until the Image is removed."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Specifies whether the Button should be active and clickable."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontBold(self) -> bool:
        """Specifies whether the text of the Button should be bold.
Some fonts do not support bold."""
        raise NotImplementedError

    @FontBold.setter
    def FontBold(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontItalic(self) -> bool:
        """Specifies whether the text of the Button should be italic.
Some fonts do not support italic."""
        raise NotImplementedError

    @FontItalic.setter
    def FontItalic(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontSize(self) -> int:
        """Specifies the text font size of the Button, measured in sp(scale-independent pixels)."""
        raise NotImplementedError

    @FontSize.setter
    def FontSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the Button's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the Button's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Image(self) -> str:
        """Specifies the path of the Button's image. If there is both an Image and a
BackgroundColor specified, only the Image will be visible."""
        raise NotImplementedError

    @Image.setter
    def Image(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def ShowFeedback(self) -> bool:
        """Specifies if a visual feedback should be shown when a Button with an assigned
Image is pressed."""
        raise NotImplementedError

    @ShowFeedback.setter
    def ShowFeedback(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Text(self) -> str:
        """Specifies the text displayed by the Button."""
        raise NotImplementedError

    @Text.setter
    def Text(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def TextColor(self) -> enums.Color:
        """Specifies the text color of the Button as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @TextColor.setter
    def TextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the Button should be visible on the screen.  Value is true
if the Button is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the Button, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the Button as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def on_Click(self, callback: Callable[[], None], /) -> None:
        """Click()

Indicates that the user tapped and released the Button."""
        raise NotImplementedError

    @staticmethod
    def on_any_Click(callback: Callable[['Button', bool], None], /) -> None:
        """Click()

Indicates that the user tapped and released the Button."""
        raise NotImplementedError

    def on_GotFocus(self, callback: Callable[[], None], /) -> None:
        """GotFocus()

Indicates the cursor moved over the Button so it is now possible
to click it."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotFocus(callback: Callable[['Button', bool], None], /) -> None:
        """GotFocus()

Indicates the cursor moved over the Button so it is now possible
to click it."""
        raise NotImplementedError

    def on_LongClick(self, callback: Callable[[], None], /) -> None:
        """LongClick()

Indicates that the user held the Button down."""
        raise NotImplementedError

    @staticmethod
    def on_any_LongClick(callback: Callable[['Button', bool], None], /) -> None:
        """LongClick()

Indicates that the user held the Button down."""
        raise NotImplementedError

    def on_LostFocus(self, callback: Callable[[], None], /) -> None:
        """LostFocus()

Indicates the cursor moved away from the Button so it is now no
longer possible to click it."""
        raise NotImplementedError

    @staticmethod
    def on_any_LostFocus(callback: Callable[['Button', bool], None], /) -> None:
        """LostFocus()

Indicates the cursor moved away from the Button so it is now no
longer possible to click it."""
        raise NotImplementedError

    def on_TouchDown(self, callback: Callable[[], None], /) -> None:
        """TouchDown()

Indicates that the Button was pressed down."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchDown(callback: Callable[['Button', bool], None], /) -> None:
        """TouchDown()

Indicates that the Button was pressed down."""
        raise NotImplementedError

    def on_TouchUp(self, callback: Callable[[], None], /) -> None:
        """TouchUp()

Indicates that the Button has been released."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchUp(callback: Callable[['Button', bool], None], /) -> None:
        """TouchUp()

Indicates that the Button has been released."""
        raise NotImplementedError

class CheckBox(Component):
    """CheckBox components can detect user taps and can change their boolean state in response."""
    __data__ = {'desc': 'CheckBox components can detect user taps and can change their boolean state in response.', 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the background color of the CheckBox as an alpha-red-green-blue\ninteger.'}, {'name': 'Checked', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Set to true if the box is checked, false otherwise.'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the CheckBox should be active and clickable.'}, {'name': 'FontBold', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies whether the text of the CheckBox should be bold.\nSome fonts do not support bold.'}, {'name': 'FontItalic', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies whether the text of the CheckBox should be italic.\nSome fonts do not support italic.'}, {'name': 'FontSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text font size of the CheckBox, measured in sp(scale-independent pixels).'}, {'name': 'FontTypeface', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies the text font face of the CheckBox as default, serif, sans\nserif, or monospace.'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the CheckBox's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the CheckBox's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Text', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text displayed by the CheckBox.'}, {'name': 'TextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text color of the CheckBox as an alpha-red-green-blue\ninteger.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the CheckBox should be visible on the screen.  Value is true\nif the CheckBox is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the CheckBox, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the CheckBox as a percentage\nof the Screen's Width."}], 'events': [{'name': 'Changed', 'args': [], 'desc': 'User tapped and released the CheckBox.'}, {'name': 'GotFocus', 'args': [], 'desc': 'CheckBox became the focused component.'}, {'name': 'LostFocus', 'args': [], 'desc': 'CheckBox stopped being the focused component.'}], 'methods': []}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., Checked: bool=..., Enabled: bool=..., FontBold: bool=..., FontItalic: bool=..., FontSize: int=..., FontTypeface: str=..., Height: int=..., Text: str=..., TextColor: enums.Color=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the background color of the CheckBox as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Checked(self) -> bool:
        """Set to true if the box is checked, false otherwise."""
        raise NotImplementedError

    @Checked.setter
    def Checked(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Specifies whether the CheckBox should be active and clickable."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontSize(self) -> int:
        """Specifies the text font size of the CheckBox, measured in sp(scale-independent pixels)."""
        raise NotImplementedError

    @FontSize.setter
    def FontSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the CheckBox's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the CheckBox's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Text(self) -> str:
        """Specifies the text displayed by the CheckBox."""
        raise NotImplementedError

    @Text.setter
    def Text(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def TextColor(self) -> enums.Color:
        """Specifies the text color of the CheckBox as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @TextColor.setter
    def TextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the CheckBox should be visible on the screen.  Value is true
if the CheckBox is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the CheckBox, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the CheckBox as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def on_Changed(self, callback: Callable[[], None], /) -> None:
        """Changed()

User tapped and released the CheckBox."""
        raise NotImplementedError

    @staticmethod
    def on_any_Changed(callback: Callable[['CheckBox', bool], None], /) -> None:
        """Changed()

User tapped and released the CheckBox."""
        raise NotImplementedError

    def on_GotFocus(self, callback: Callable[[], None], /) -> None:
        """GotFocus()

CheckBox became the focused component."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotFocus(callback: Callable[['CheckBox', bool], None], /) -> None:
        """GotFocus()

CheckBox became the focused component."""
        raise NotImplementedError

    def on_LostFocus(self, callback: Callable[[], None], /) -> None:
        """LostFocus()

CheckBox stopped being the focused component."""
        raise NotImplementedError

    @staticmethod
    def on_any_LostFocus(callback: Callable[['CheckBox', bool], None], /) -> None:
        """LostFocus()

CheckBox stopped being the focused component."""
        raise NotImplementedError

class DatePicker(Component):
    """A button that, when clicked on, launches a popup dialog to allow the user to select a date on
the Gregorian Calendar."""
    __data__ = {'desc': 'A button that, when clicked on, launches a popup dialog to allow the user to select a date on\nthe Gregorian Calendar.', 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the DatePicker's background color as an alpha-red-green-blue\ninteger.  If an Image has been set, the color\nchange will not be visible until the Image is removed."}, {'name': 'Day', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the Day of the month that was last picked using the DatePicker.'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the DatePicker should be active and clickable.'}, {'name': 'FontBold', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the text of the DatePicker should be bold.\nSome fonts do not support bold.'}, {'name': 'FontItalic', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the text of the DatePicker should be italic.\nSome fonts do not support italic.'}, {'name': 'FontSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text font size of the DatePicker, measured in sp(scale-independent pixels).'}, {'name': 'FontTypeface', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the text font face of the DatePicker as default, serif, sans\nserif, monospace, or custom font typeface. To add a custom typeface,\nupload a .ttf file to the project's media."}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the DatePicker's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the DatePicker's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Image', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the path of the DatePicker's image. If there is both an Image and a\nBackgroundColor specified, only the Image will be visible."}, {'name': 'Instant', 'type': 'enums.Instant', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns instant of the date that was last picked using the DatePicker.'}, {'name': 'Month', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the number of the Month that was last picked using the DatePicker.'}, {'name': 'MonthInText', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the name of the Month that was last picked using the DatePicker.'}, {'name': 'Shape', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies the shape of the DatePicker. The valid values for this property are 0 (default),\n1 (rounded), 2 (rectangle), and 3 (oval). The Shape will not be visible if an\nImage is used.'}, {'name': 'ShowFeedback', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies if a visual feedback should be shown when a DatePicker with an assigned\nImage is pressed.'}, {'name': 'Text', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text displayed by the DatePicker.'}, {'name': 'TextAlignment', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the alignment of the DatePicker's text. Valid values are:\n0 (normal; e.g., left-justified if text is written left to right),\n1 (center), or\n2 (opposite; e.g., right-justified if text is written left to right)."}, {'name': 'TextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text color of the DatePicker as an alpha-red-green-blue\ninteger.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the DatePicker should be visible on the screen.  Value is true\nif the DatePicker is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the DatePicker, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the DatePicker as a percentage\nof the Screen's Width."}, {'name': 'Year', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the Year that was last picked using the DatePicker.'}], 'events': [{'name': 'AfterDateSet', 'args': [], 'desc': 'Event that runs after the user chooses a Date in the dialog.'}, {'name': 'GotFocus', 'args': [], 'desc': 'Indicates the cursor moved over the DatePicker so it is now possible\nto click it.'}, {'name': 'LostFocus', 'args': [], 'desc': 'Indicates the cursor moved away from the DatePicker so it is now no\nlonger possible to click it.'}, {'name': 'TouchDown', 'args': [], 'desc': 'Indicates that the DatePicker was pressed down.'}, {'name': 'TouchUp', 'args': [], 'desc': 'Indicates that the DatePicker has been released.'}], 'methods': [{'name': 'LaunchPicker', 'args': [], 'returns': None, 'desc': 'Launches the DatePicker dialog. The AfterDateSet event will be run after the user\nconfirms their selection.'}, {'name': 'SetDateToDisplay', 'args': [{'name': 'year', 'type': 'int'}, {'name': 'month', 'type': 'int'}, {'name': 'day', 'type': 'int'}], 'returns': None, 'desc': 'Allows the user to set the date to be displayed when the date picker opens.\nValid values for the month field are 1-12 and 1-31 for the day field.'}, {'name': 'SetDateToDisplayFromInstant', 'args': [{'name': 'instant', 'type': 'enums.Instant'}], 'returns': None, 'desc': 'Allows the user to set the date from the instant to be displayed when the date picker opens.'}]}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., Enabled: bool=..., FontBold: bool=..., FontItalic: bool=..., FontSize: int=..., FontTypeface: str=..., Height: int=..., Image: str=..., Shape: int=..., ShowFeedback: bool=..., Text: str=..., TextAlignment: int=..., TextColor: enums.Color=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the DatePicker's background color as an alpha-red-green-blue
integer.  If an Image has been set, the color
change will not be visible until the Image is removed."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Day(self) -> int:
        """Returns the Day of the month that was last picked using the DatePicker."""
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Specifies whether the DatePicker should be active and clickable."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontBold(self) -> bool:
        """Specifies whether the text of the DatePicker should be bold.
Some fonts do not support bold."""
        raise NotImplementedError

    @FontBold.setter
    def FontBold(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontItalic(self) -> bool:
        """Specifies whether the text of the DatePicker should be italic.
Some fonts do not support italic."""
        raise NotImplementedError

    @FontItalic.setter
    def FontItalic(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontSize(self) -> int:
        """Specifies the text font size of the DatePicker, measured in sp(scale-independent pixels)."""
        raise NotImplementedError

    @FontSize.setter
    def FontSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the DatePicker's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the DatePicker's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Image(self) -> str:
        """Specifies the path of the DatePicker's image. If there is both an Image and a
BackgroundColor specified, only the Image will be visible."""
        raise NotImplementedError

    @Image.setter
    def Image(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Instant(self) -> enums.Instant:
        """Returns instant of the date that was last picked using the DatePicker."""
        raise NotImplementedError

    @property
    def Month(self) -> int:
        """Returns the number of the Month that was last picked using the DatePicker."""
        raise NotImplementedError

    @property
    def MonthInText(self) -> str:
        """Returns the name of the Month that was last picked using the DatePicker."""
        raise NotImplementedError

    @property
    def ShowFeedback(self) -> bool:
        """Specifies if a visual feedback should be shown when a DatePicker with an assigned
Image is pressed."""
        raise NotImplementedError

    @ShowFeedback.setter
    def ShowFeedback(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Text(self) -> str:
        """Specifies the text displayed by the DatePicker."""
        raise NotImplementedError

    @Text.setter
    def Text(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def TextColor(self) -> enums.Color:
        """Specifies the text color of the DatePicker as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @TextColor.setter
    def TextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the DatePicker should be visible on the screen.  Value is true
if the DatePicker is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the DatePicker, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the DatePicker as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Year(self) -> int:
        """Returns the Year that was last picked using the DatePicker."""
        raise NotImplementedError

    def LaunchPicker(self, /) -> None:
        """Launches the DatePicker dialog. The AfterDateSet event will be run after the user
confirms their selection."""
        raise NotImplementedError

    def SetDateToDisplay(self, year: int, month: int, day: int, /) -> None:
        """Allows the user to set the date to be displayed when the date picker opens.
Valid values for the month field are 1-12 and 1-31 for the day field."""
        raise NotImplementedError

    def SetDateToDisplayFromInstant(self, instant: enums.Instant, /) -> None:
        """Allows the user to set the date from the instant to be displayed when the date picker opens."""
        raise NotImplementedError

    def on_AfterDateSet(self, callback: Callable[[], None], /) -> None:
        """AfterDateSet()

Event that runs after the user chooses a Date in the dialog."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterDateSet(callback: Callable[['DatePicker', bool], None], /) -> None:
        """AfterDateSet()

Event that runs after the user chooses a Date in the dialog."""
        raise NotImplementedError

    def on_GotFocus(self, callback: Callable[[], None], /) -> None:
        """GotFocus()

Indicates the cursor moved over the DatePicker so it is now possible
to click it."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotFocus(callback: Callable[['DatePicker', bool], None], /) -> None:
        """GotFocus()

Indicates the cursor moved over the DatePicker so it is now possible
to click it."""
        raise NotImplementedError

    def on_LostFocus(self, callback: Callable[[], None], /) -> None:
        """LostFocus()

Indicates the cursor moved away from the DatePicker so it is now no
longer possible to click it."""
        raise NotImplementedError

    @staticmethod
    def on_any_LostFocus(callback: Callable[['DatePicker', bool], None], /) -> None:
        """LostFocus()

Indicates the cursor moved away from the DatePicker so it is now no
longer possible to click it."""
        raise NotImplementedError

    def on_TouchDown(self, callback: Callable[[], None], /) -> None:
        """TouchDown()

Indicates that the DatePicker was pressed down."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchDown(callback: Callable[['DatePicker', bool], None], /) -> None:
        """TouchDown()

Indicates that the DatePicker was pressed down."""
        raise NotImplementedError

    def on_TouchUp(self, callback: Callable[[], None], /) -> None:
        """TouchUp()

Indicates that the DatePicker has been released."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchUp(callback: Callable[['DatePicker', bool], None], /) -> None:
        """TouchUp()

Indicates that the DatePicker has been released."""
        raise NotImplementedError

class Image(Component):
    """Component for displaying images and basic animations."""
    __data__ = {'desc': 'Component for displaying images and basic animations.', 'properties': [{'name': 'AlternateText', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'A written description of what the image looks like.'}, {'name': 'Animation', 'type': 'str', 'ro': False, 'do': False, 'bo': True, 'desc': 'This is a limited form of animation that can attach a small number of motion types to images.\nThe allowable motions are ScrollRightSlow, ScrollRight, ScrollRightFast,\nScrollLeftSlow, ScrollLeft, ScrollLeftFast, and Stop.'}, {'name': 'Clickable', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the image should be clickable or not.'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the Image's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the Image's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Picture', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the path of the Image's Picture."}, {'name': 'RotationAngle', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'The angle at which the image picture appears rotated. This rotation does not appear on the designer screen, only on the device.'}, {'name': 'ScalePictureToFit', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the image should be resized to match the size of the ImageView.'}, {'name': 'Scaling', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': 'This property determines how the picture scales according to the Height or Width of the Image. Scale proportionally (0) preserves the picture aspect ratio. Scale to fit (1) matches the Image area, even if the aspect ratio changes.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the Image should be visible on the screen.  Value is true\nif the Image is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the Image, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the Image as a percentage\nof the Screen's Width."}], 'events': [{'name': 'Click', 'args': [], 'desc': 'An event that occurs when an image is clicked.'}], 'methods': []}

    def __init__(self, /, *, parent: Component=..., AlternateText: str=..., Clickable: bool=..., Height: int=..., Picture: str=..., RotationAngle: int=..., ScalePictureToFit: bool=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def AlternateText(self) -> str:
        """A written description of what the image looks like."""
        raise NotImplementedError

    @AlternateText.setter
    def AlternateText(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Animation(self) -> str:
        """This is a limited form of animation that can attach a small number of motion types to images.
The allowable motions are ScrollRightSlow, ScrollRight, ScrollRightFast,
ScrollLeftSlow, ScrollLeft, ScrollLeftFast, and Stop."""
        raise NotImplementedError

    @Animation.setter
    def Animation(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Clickable(self) -> bool:
        """Specifies whether the image should be clickable or not."""
        raise NotImplementedError

    @Clickable.setter
    def Clickable(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the Image's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the Image's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Picture(self) -> str:
        """Specifies the path of the Image's Picture."""
        raise NotImplementedError

    @Picture.setter
    def Picture(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def RotationAngle(self) -> int:
        """The angle at which the image picture appears rotated. This rotation does not appear on the designer screen, only on the device."""
        raise NotImplementedError

    @RotationAngle.setter
    def RotationAngle(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def ScalePictureToFit(self) -> bool:
        """Specifies whether the image should be resized to match the size of the ImageView."""
        raise NotImplementedError

    @ScalePictureToFit.setter
    def ScalePictureToFit(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Scaling(self) -> int:
        """This property determines how the picture scales according to the Height or Width of the Image. Scale proportionally (0) preserves the picture aspect ratio. Scale to fit (1) matches the Image area, even if the aspect ratio changes."""
        raise NotImplementedError

    @Scaling.setter
    def Scaling(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the Image should be visible on the screen.  Value is true
if the Image is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the Image, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the Image as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def on_Click(self, callback: Callable[[], None], /) -> None:
        """Click()

An event that occurs when an image is clicked."""
        raise NotImplementedError

    @staticmethod
    def on_any_Click(callback: Callable[['Image', bool], None], /) -> None:
        """Click()

An event that occurs when an image is clicked."""
        raise NotImplementedError

class Label(Component):
    """Labels are components used to show text."""
    __data__ = {'desc': 'Labels are components used to show text.', 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the label's background color as an alpha-red-green-blue\ninteger."}, {'name': 'FontBold', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies whether the label's text should be bold.\nSome fonts do not support bold."}, {'name': 'FontItalic', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies whether the label's text should be italic.\nSome fonts do not support italic."}, {'name': 'FontSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the label's text's font size, measured in sp(scale-independent pixels)."}, {'name': 'FontTypeface', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the label's text's font face as default, serif, sans\nserif, or monospace."}, {'name': 'HTMLContent', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the content of the Label as HTML. This is only useful if the\nHTMLFormat property is true.'}, {'name': 'HTMLFormat', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the label's text's format"}, {'name': 'HasMargins', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the label should have margins.\nThis margin value is not well coordinated with the\ndesigner, where the margins are defined for the arrangement, not just for individual\nlabels.'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the Label's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the Label's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Text', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text displayed by the label.'}, {'name': 'TextAlignment', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the alignment of the label's text: center, normal\n(e.g., left-justified if text is written left to right), or\nopposite (e.g., right-justified if text is written left to right)."}, {'name': 'TextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the label's text color as an alpha-red-green-blue\ninteger."}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the Label should be visible on the screen.  Value is true\nif the Label is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the Label, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the Label as a percentage\nof the Screen's Width."}], 'events': [], 'methods': []}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., FontBold: bool=..., FontItalic: bool=..., FontSize: int=..., FontTypeface: str=..., HTMLFormat: bool=..., HasMargins: bool=..., Height: int=..., Text: str=..., TextAlignment: int=..., TextColor: enums.Color=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the label's background color as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def FontSize(self) -> int:
        """Specifies the label's text's font size, measured in sp(scale-independent pixels)."""
        raise NotImplementedError

    @FontSize.setter
    def FontSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HTMLContent(self) -> str:
        """Returns the content of the Label as HTML. This is only useful if the
HTMLFormat property is true."""
        raise NotImplementedError

    @property
    def HasMargins(self) -> bool:
        """Specifies whether the label should have margins.
This margin value is not well coordinated with the
designer, where the margins are defined for the arrangement, not just for individual
labels."""
        raise NotImplementedError

    @HasMargins.setter
    def HasMargins(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the Label's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the Label's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Text(self) -> str:
        """Specifies the text displayed by the label."""
        raise NotImplementedError

    @Text.setter
    def Text(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def TextColor(self) -> enums.Color:
        """Specifies the label's text color as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @TextColor.setter
    def TextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the Label should be visible on the screen.  Value is true
if the Label is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the Label, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the Label as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

class ListPicker(Component):
    """A button that, when clicked on, displays a list of texts for the user to choose among. The texts
can be specified through the Designer or Blocks Editor by setting the
ElementsFromString  property to their string-separated concatenation
(for example, choice 1, choice 2, choice 3) or by setting the Elements
property to a List in the Blocks editor."""
    __data__ = {'desc': 'A button that, when clicked on, displays a list of texts for the user to choose among. The texts\ncan be specified through the Designer or Blocks Editor by setting the\nElementsFromString  property to their string-separated concatenation\n(for example, choice 1, choice 2, choice 3) or by setting the Elements\nproperty to a List in the Blocks editor.', 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the ListPicker's background color as an alpha-red-green-blue\ninteger.  If an Image has been set, the color\nchange will not be visible until the Image is removed."}, {'name': 'Elements', 'type': 'list', 'ro': False, 'do': False, 'bo': True, 'desc': 'Specifies the list of choices to display.'}, {'name': 'ElementsFromString', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Set the list of choices from a string of comma-separated values.'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the ListPicker should be active and clickable.'}, {'name': 'FontBold', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the text of the ListPicker should be bold.\nSome fonts do not support bold.'}, {'name': 'FontItalic', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the text of the ListPicker should be italic.\nSome fonts do not support italic.'}, {'name': 'FontSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text font size of the ListPicker, measured in sp(scale-independent pixels).'}, {'name': 'FontTypeface', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the text font face of the ListPicker as default, serif, sans\nserif, monospace, or custom font typeface. To add a custom typeface,\nupload a .ttf file to the project's media."}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the ListPicker's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the ListPicker's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Image', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the path of the ListPicker's image. If there is both an Image and a\nBackgroundColor specified, only the Image will be visible."}, {'name': 'ItemBackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'The background color of the ListPicker items.'}, {'name': 'ItemTextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'The text color of the ListPicker items.'}, {'name': 'Selection', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'The selected item. When directly changed by the programmer, the SelectionIndex\nproperty is also changed to the first item in the ListPicker with the given value.\nIf the value is not in Elements, SelectionIndex will be set to 0.'}, {'name': 'SelectionIndex', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': 'Selection index property setter method.'}, {'name': 'Shape', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies the shape of the ListPicker. The valid values for this property are 0 (default),\n1 (rounded), 2 (rectangle), and 3 (oval). The Shape will not be visible if an\nImage is used.'}, {'name': 'ShowFeedback', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies if a visual feedback should be shown when a ListPicker with an assigned\nImage is pressed.'}, {'name': 'ShowFilterBar', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'If true, the ListPicker will show a search filter bar.'}, {'name': 'Text', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text displayed by the ListPicker.'}, {'name': 'TextAlignment', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the alignment of the ListPicker's text. Valid values are:\n0 (normal; e.g., left-justified if text is written left to right),\n1 (center), or\n2 (opposite; e.g., right-justified if text is written left to right)."}, {'name': 'TextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text color of the ListPicker as an alpha-red-green-blue\ninteger.'}, {'name': 'Title', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Optional title displayed at the top of the list of choices.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the ListPicker should be visible on the screen.  Value is true\nif the ListPicker is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the ListPicker, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the ListPicker as a percentage\nof the Screen's Width."}], 'events': [{'name': 'AfterPicking', 'args': [], 'desc': 'Event to be raised after the ListPicker activity returns its\nresult and the properties have been filled in.'}, {'name': 'BeforePicking', 'args': [], 'desc': 'Event to raise when the ListPicker is clicked or the picker is shown\nusing the Open method.  This event occurs before the picker is displayed, and\ncan be used to prepare the picker before it is shown.'}, {'name': 'GotFocus', 'args': [], 'desc': 'Indicates the cursor moved over the ListPicker so it is now possible\nto click it.'}, {'name': 'LostFocus', 'args': [], 'desc': 'Indicates the cursor moved away from the ListPicker so it is now no\nlonger possible to click it.'}, {'name': 'TouchDown', 'args': [], 'desc': 'Indicates that the ListPicker was pressed down.'}, {'name': 'TouchUp', 'args': [], 'desc': 'Indicates that the ListPicker has been released.'}], 'methods': [{'name': 'Open', 'args': [], 'returns': None, 'desc': 'Opens the ListPicker, as though the user clicked on it.'}]}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., ElementsFromString: str=..., Enabled: bool=..., FontBold: bool=..., FontItalic: bool=..., FontSize: int=..., FontTypeface: str=..., Height: int=..., Image: str=..., ItemBackgroundColor: enums.Color=..., ItemTextColor: enums.Color=..., Selection: str=..., Shape: int=..., ShowFeedback: bool=..., ShowFilterBar: bool=..., Text: str=..., TextAlignment: int=..., TextColor: enums.Color=..., Title: str=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the ListPicker's background color as an alpha-red-green-blue
integer.  If an Image has been set, the color
change will not be visible until the Image is removed."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Elements(self) -> list:
        """Specifies the list of choices to display."""
        raise NotImplementedError

    @Elements.setter
    def Elements(self, value: list, /) -> None:
        raise NotImplementedError

    @property
    def ElementsFromString(self) -> str:
        """Set the list of choices from a string of comma-separated values."""
        raise NotImplementedError

    @ElementsFromString.setter
    def ElementsFromString(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Specifies whether the ListPicker should be active and clickable."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontBold(self) -> bool:
        """Specifies whether the text of the ListPicker should be bold.
Some fonts do not support bold."""
        raise NotImplementedError

    @FontBold.setter
    def FontBold(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontItalic(self) -> bool:
        """Specifies whether the text of the ListPicker should be italic.
Some fonts do not support italic."""
        raise NotImplementedError

    @FontItalic.setter
    def FontItalic(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontSize(self) -> int:
        """Specifies the text font size of the ListPicker, measured in sp(scale-independent pixels)."""
        raise NotImplementedError

    @FontSize.setter
    def FontSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the ListPicker's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the ListPicker's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Image(self) -> str:
        """Specifies the path of the ListPicker's image. If there is both an Image and a
BackgroundColor specified, only the Image will be visible."""
        raise NotImplementedError

    @Image.setter
    def Image(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def ItemBackgroundColor(self) -> enums.Color:
        """The background color of the ListPicker items."""
        raise NotImplementedError

    @ItemBackgroundColor.setter
    def ItemBackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def ItemTextColor(self) -> enums.Color:
        """The text color of the ListPicker items."""
        raise NotImplementedError

    @ItemTextColor.setter
    def ItemTextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Selection(self) -> str:
        """The selected item. When directly changed by the programmer, the SelectionIndex
property is also changed to the first item in the ListPicker with the given value.
If the value is not in Elements, SelectionIndex will be set to 0."""
        raise NotImplementedError

    @Selection.setter
    def Selection(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def SelectionIndex(self) -> int:
        """Selection index property setter method."""
        raise NotImplementedError

    @SelectionIndex.setter
    def SelectionIndex(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def ShowFeedback(self) -> bool:
        """Specifies if a visual feedback should be shown when a ListPicker with an assigned
Image is pressed."""
        raise NotImplementedError

    @ShowFeedback.setter
    def ShowFeedback(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def ShowFilterBar(self) -> bool:
        """If true, the ListPicker will show a search filter bar."""
        raise NotImplementedError

    @ShowFilterBar.setter
    def ShowFilterBar(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Text(self) -> str:
        """Specifies the text displayed by the ListPicker."""
        raise NotImplementedError

    @Text.setter
    def Text(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def TextColor(self) -> enums.Color:
        """Specifies the text color of the ListPicker as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @TextColor.setter
    def TextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Title(self) -> str:
        """Optional title displayed at the top of the list of choices."""
        raise NotImplementedError

    @Title.setter
    def Title(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the ListPicker should be visible on the screen.  Value is true
if the ListPicker is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the ListPicker, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the ListPicker as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def Open(self, /) -> None:
        """Opens the ListPicker, as though the user clicked on it."""
        raise NotImplementedError

    def on_AfterPicking(self, callback: Callable[[], None], /) -> None:
        """AfterPicking()

Event to be raised after the ListPicker activity returns its
result and the properties have been filled in."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterPicking(callback: Callable[['ListPicker', bool], None], /) -> None:
        """AfterPicking()

Event to be raised after the ListPicker activity returns its
result and the properties have been filled in."""
        raise NotImplementedError

    def on_BeforePicking(self, callback: Callable[[], None], /) -> None:
        """BeforePicking()

Event to raise when the ListPicker is clicked or the picker is shown
using the Open method.  This event occurs before the picker is displayed, and
can be used to prepare the picker before it is shown."""
        raise NotImplementedError

    @staticmethod
    def on_any_BeforePicking(callback: Callable[['ListPicker', bool], None], /) -> None:
        """BeforePicking()

Event to raise when the ListPicker is clicked or the picker is shown
using the Open method.  This event occurs before the picker is displayed, and
can be used to prepare the picker before it is shown."""
        raise NotImplementedError

    def on_GotFocus(self, callback: Callable[[], None], /) -> None:
        """GotFocus()

Indicates the cursor moved over the ListPicker so it is now possible
to click it."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotFocus(callback: Callable[['ListPicker', bool], None], /) -> None:
        """GotFocus()

Indicates the cursor moved over the ListPicker so it is now possible
to click it."""
        raise NotImplementedError

    def on_LostFocus(self, callback: Callable[[], None], /) -> None:
        """LostFocus()

Indicates the cursor moved away from the ListPicker so it is now no
longer possible to click it."""
        raise NotImplementedError

    @staticmethod
    def on_any_LostFocus(callback: Callable[['ListPicker', bool], None], /) -> None:
        """LostFocus()

Indicates the cursor moved away from the ListPicker so it is now no
longer possible to click it."""
        raise NotImplementedError

    def on_TouchDown(self, callback: Callable[[], None], /) -> None:
        """TouchDown()

Indicates that the ListPicker was pressed down."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchDown(callback: Callable[['ListPicker', bool], None], /) -> None:
        """TouchDown()

Indicates that the ListPicker was pressed down."""
        raise NotImplementedError

    def on_TouchUp(self, callback: Callable[[], None], /) -> None:
        """TouchUp()

Indicates that the ListPicker has been released."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchUp(callback: Callable[['ListPicker', bool], None], /) -> None:
        """TouchUp()

Indicates that the ListPicker has been released."""
        raise NotImplementedError

class ListView(Component):
    """This is a visible component that displays a list of text and image elements in your Screen to
display. Simple lists of strings may be set using the ElementsFromString property.
More complex lists of elements containing multiple strings and/or images can be created using the
ListData and ListViewLayout properties."""
    __data__ = {'desc': 'This is a visible component that displays a list of text and image elements in your Screen to\ndisplay. Simple lists of strings may be set using the ElementsFromString property.\nMore complex lists of elements containing multiple strings and/or images can be created using the\nListData and ListViewLayout properties.', 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'The color of the ListView background.'}, {'name': 'Elements', 'type': 'list', 'ro': False, 'do': False, 'bo': True, 'desc': 'Specifies the list of choices to display.'}, {'name': 'ElementsFromString', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Set the list of choices specified as a string with the elements separated by commas\nsuch as: Cheese,Fruit,Bacon,Radish.'}, {'name': 'FontSizeDetail', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the ListView item's text font size"}, {'name': 'FontTypeface', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the label's text's font face as default, serif, sans\nserif, or monospace."}, {'name': 'FontTypefaceDetail', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the label's text's font face as default, serif, sans\nserif, or monospace."}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the ListView's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the ListView's vertical height as a percentage\nof the Screen's Height."}, {'name': 'ImageHeight', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the image height of ListView layouts containing images'}, {'name': 'ImageWidth', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the image width of ListView layouts containing images'}, {'name': 'ListData', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies data to be displayed in the ListView elements. This property sets the\nelements specified in ListViewLayout. For example, if the chosen\nlayout is Image,MainText this property will allow any number of elements to be\ndefined, each containing a filename for Image and a string for MainText.\nDesigner only property.'}, {'name': 'ListViewLayout', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies type of layout for ListView row. Designer only property.'}, {'name': 'Orientation', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the layout's orientation. This may be: Vertical, which displays elements\nin rows one after the other; or Horizontal, which displays one element at a time and\nallows the user to swipe left or right to brows the elements."}, {'name': 'Selection', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Returns the text in the ListView at the position of SelectionIndex.'}, {'name': 'SelectionColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'The color of the item when it is selected.'}, {'name': 'SelectionDetailText', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the Secondary or Detail text in the ListView at the position set by SelectionIndex'}, {'name': 'SelectionIndex', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': 'The index of the currently selected item, starting at 1. If no item is selected, the value\nwill be 0. If an attempt is made to set this to a number less than 1 or greater than the\nnumber of items in the ListView, SelectionIndex will be set to 0, and\nSelection will be set to the empty text.'}, {'name': 'ShowFilterBar', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Sets visibility of the filter bar. true will show the bar,\nfalse will hide it.'}, {'name': 'TextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'The text color of the ListView items.'}, {'name': 'TextColorDetail', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the color of the secondary text in a ListView layout'}, {'name': 'TextSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the ListView item's text font size"}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the ListView should be visible on the screen.  Value is true\nif the ListView is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the ListView, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the ListView as a percentage\nof the Screen's Width."}], 'events': [{'name': 'AfterPicking', 'args': [], 'desc': 'Simple event to be raised after the an element has been chosen in the list.\nThe selected element is available in the Selection property.'}], 'methods': [{'name': 'CreateElement', 'args': [{'name': 'mainText', 'type': 'str'}, {'name': 'detailText', 'type': 'str'}, {'name': 'imageName', 'type': 'str'}], 'returns': 'dict', 'desc': 'Creates a'}, {'name': 'GetDetailText', 'args': [{'name': 'listElement', 'type': 'dict'}], 'returns': 'str', 'desc': 'Get the Detail Text of a ListView element.'}, {'name': 'GetImageName', 'args': [{'name': 'listElement', 'type': 'dict'}], 'returns': 'str', 'desc': 'Get the filename of the image of a ListView element that has been uploaded to Media.'}, {'name': 'GetMainText', 'args': [{'name': 'listElement', 'type': 'dict'}], 'returns': 'str', 'desc': 'Get the Main Text of a ListView element.'}, {'name': 'Refresh', 'args': [], 'returns': None, 'desc': 'Reload the ListView to reflect any changes in the data.'}]}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., ElementsFromString: str=..., FontSizeDetail: int=..., FontTypeface: str=..., FontTypefaceDetail: str=..., Height: int=..., ImageHeight: int=..., ImageWidth: int=..., ListData: str=..., ListViewLayout: int=..., Orientation: int=..., Selection: str=..., SelectionColor: enums.Color=..., ShowFilterBar: bool=..., TextColor: enums.Color=..., TextColorDetail: enums.Color=..., TextSize: int=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """The color of the ListView background."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Elements(self) -> list:
        """Specifies the list of choices to display."""
        raise NotImplementedError

    @Elements.setter
    def Elements(self, value: list, /) -> None:
        raise NotImplementedError

    @property
    def ElementsFromString(self) -> str:
        """Set the list of choices specified as a string with the elements separated by commas
such as: Cheese,Fruit,Bacon,Radish."""
        raise NotImplementedError

    @ElementsFromString.setter
    def ElementsFromString(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def FontSizeDetail(self) -> int:
        """Specifies the ListView item's text font size"""
        raise NotImplementedError

    @FontSizeDetail.setter
    def FontSizeDetail(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the ListView's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the ListView's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def ImageHeight(self) -> int:
        """Specifies the image height of ListView layouts containing images"""
        raise NotImplementedError

    @ImageHeight.setter
    def ImageHeight(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def ImageWidth(self) -> int:
        """Specifies the image width of ListView layouts containing images"""
        raise NotImplementedError

    @ImageWidth.setter
    def ImageWidth(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Orientation(self) -> int:
        """Specifies the layout's orientation. This may be: Vertical, which displays elements
in rows one after the other; or Horizontal, which displays one element at a time and
allows the user to swipe left or right to brows the elements."""
        raise NotImplementedError

    @Orientation.setter
    def Orientation(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Selection(self) -> str:
        """Returns the text in the ListView at the position of SelectionIndex."""
        raise NotImplementedError

    @Selection.setter
    def Selection(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def SelectionColor(self) -> enums.Color:
        """The color of the item when it is selected."""
        raise NotImplementedError

    @SelectionColor.setter
    def SelectionColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def SelectionDetailText(self) -> str:
        """Returns the Secondary or Detail text in the ListView at the position set by SelectionIndex"""
        raise NotImplementedError

    @property
    def SelectionIndex(self) -> int:
        """The index of the currently selected item, starting at 1. If no item is selected, the value
will be 0. If an attempt is made to set this to a number less than 1 or greater than the
number of items in the ListView, SelectionIndex will be set to 0, and
Selection will be set to the empty text."""
        raise NotImplementedError

    @SelectionIndex.setter
    def SelectionIndex(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def ShowFilterBar(self) -> bool:
        """Sets visibility of the filter bar. true will show the bar,
false will hide it."""
        raise NotImplementedError

    @ShowFilterBar.setter
    def ShowFilterBar(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def TextColor(self) -> enums.Color:
        """The text color of the ListView items."""
        raise NotImplementedError

    @TextColor.setter
    def TextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def TextColorDetail(self) -> enums.Color:
        """Specifies the color of the secondary text in a ListView layout"""
        raise NotImplementedError

    @TextColorDetail.setter
    def TextColorDetail(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def TextSize(self) -> int:
        """Specifies the ListView item's text font size"""
        raise NotImplementedError

    @TextSize.setter
    def TextSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the ListView should be visible on the screen.  Value is true
if the ListView is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the ListView, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the ListView as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def CreateElement(self, mainText: str, detailText: str, imageName: str, /) -> dict:
        """Creates a"""
        raise NotImplementedError

    def GetDetailText(self, listElement: dict, /) -> str:
        """Get the Detail Text of a ListView element."""
        raise NotImplementedError

    def GetImageName(self, listElement: dict, /) -> str:
        """Get the filename of the image of a ListView element that has been uploaded to Media."""
        raise NotImplementedError

    def GetMainText(self, listElement: dict, /) -> str:
        """Get the Main Text of a ListView element."""
        raise NotImplementedError

    def Refresh(self, /) -> None:
        """Reload the ListView to reflect any changes in the data."""
        raise NotImplementedError

    def on_AfterPicking(self, callback: Callable[[], None], /) -> None:
        """AfterPicking()

Simple event to be raised after the an element has been chosen in the list.
The selected element is available in the Selection property."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterPicking(callback: Callable[['ListView', bool], None], /) -> None:
        """AfterPicking()

Simple event to be raised after the an element has been chosen in the list.
The selected element is available in the Selection property."""
        raise NotImplementedError

class Notifier(Component):
    """The Notifier component displays alert messages and creates Android log entries through
an assortment of methods."""
    __data__ = {'desc': 'The Notifier component displays alert messages and creates Android log entries through\nan assortment of methods.', 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the background color for alerts (not dialogs).'}, {'name': 'NotifierLength', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies the length of time that the alert is shown â\x80\x93 either "short" or "long".'}, {'name': 'TextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text color for alerts (not dialogs).'}], 'events': [{'name': 'AfterChoosing', 'args': [{'name': 'choice', 'type': 'str'}], 'desc': 'Event after the user has made a selection for\nShowChooseDialog.'}, {'name': 'AfterTextInput', 'args': [{'name': 'response', 'type': 'str'}], 'desc': 'Event raised after the user has responded to ShowTextDialog.'}, {'name': 'ChoosingCanceled', 'args': [], 'desc': 'Event raised when the user cancels choosing an option.\nShowChooseDialog.'}, {'name': 'TextInputCanceled', 'args': [], 'desc': 'Event raised when the user cancels\nShowPasswordDialog, or\nShowTextDialog.'}], 'methods': [{'name': 'DismissProgressDialog', 'args': [], 'returns': None, 'desc': 'Dismisses the alert created by the ShowProgressDialog block'}, {'name': 'LogError', 'args': [{'name': 'message', 'type': 'str'}], 'returns': None, 'desc': 'Writes an error message to the Android system log. See the Google Android documentation for\nhow to access the log.'}, {'name': 'LogInfo', 'args': [{'name': 'message', 'type': 'str'}], 'returns': None, 'desc': 'Writes an information message to the Android log.'}, {'name': 'LogWarning', 'args': [{'name': 'message', 'type': 'str'}], 'returns': None, 'desc': 'Writes a warning message to the Android log. See the Google Android documentation for how to\naccess the log.'}, {'name': 'ShowAlert', 'args': [{'name': 'notice', 'type': 'str'}], 'returns': None, 'desc': 'Display a temporary notification.'}, {'name': 'ShowChooseDialog', 'args': [{'name': 'message', 'type': 'str'}, {'name': 'title', 'type': 'str'}, {'name': 'button1Text', 'type': 'str'}, {'name': 'button2Text', 'type': 'str'}, {'name': 'cancelable', 'type': 'bool'}], 'returns': None, 'desc': 'Shows a dialog box with two buttons, from which the user can choose. If cancelable is\ntrue there will be an additional CANCEL button. Pressing a button will raise\nthe AfterChoosing event. The "choice" parameter to\nAfterChoosing will be the text on the button that was pressed, or "Cancel" if\nthe CANCEL button was pressed. If canceled, the TextInputCanceled event will also\nrun.'}, {'name': 'ShowMessageDialog', 'args': [{'name': 'message', 'type': 'str'}, {'name': 'title', 'type': 'str'}, {'name': 'buttonText', 'type': 'str'}], 'returns': None, 'desc': 'Display an alert dialog with a single button that dismisses the alert.'}, {'name': 'ShowPasswordDialog', 'args': [{'name': 'message', 'type': 'str'}, {'name': 'title', 'type': 'str'}, {'name': 'cancelable', 'type': 'bool'}], 'returns': None, 'desc': 'Shows a dialog box where the user can enter password (input is masked), after which the\nAfterTextInput event will be raised. If cancelable is true\nthere will be an additional CANCEL button. The AfterTextInput and\nTextInputCanceled events behave the same way as described in\nShowTextDialog.'}, {'name': 'ShowProgressDialog', 'args': [{'name': 'message', 'type': 'str'}, {'name': 'title', 'type': 'str'}], 'returns': None, 'desc': 'Shows a dialog box with an optional title and message (use empty strings if they are not\nwanted). This dialog box contains a spinning artifact to indicate that the program is working.\nIt cannot be canceled by the user but must be dismissed by the App Inventor Program by using\nthe DismissProgressDialog method.'}, {'name': 'ShowTextDialog', 'args': [{'name': 'message', 'type': 'str'}, {'name': 'title', 'type': 'str'}, {'name': 'cancelable', 'type': 'bool'}], 'returns': None, 'desc': 'Shows a dialog box where the user can enter text, after which the\nAfterTextInput  event will be raised. If cancelable is true\nthere will be an additional CANCEL button. Entering text will raise the\nAfterTextInput event. The "response" parameter to\nAfterTextInput  will be the text that was entered, or "Cancel" if the CANCEL\nbutton was pressed. If canceled, the TextInputCanceled event will also run.'}]}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., NotifierLength: int=..., TextColor: enums.Color=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the background color for alerts (not dialogs)."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def TextColor(self) -> enums.Color:
        """Specifies the text color for alerts (not dialogs)."""
        raise NotImplementedError

    @TextColor.setter
    def TextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    def DismissProgressDialog(self, /) -> None:
        """Dismisses the alert created by the ShowProgressDialog block"""
        raise NotImplementedError

    def LogError(self, message: str, /) -> None:
        """Writes an error message to the Android system log. See the Google Android documentation for
how to access the log."""
        raise NotImplementedError

    def LogInfo(self, message: str, /) -> None:
        """Writes an information message to the Android log."""
        raise NotImplementedError

    def LogWarning(self, message: str, /) -> None:
        """Writes a warning message to the Android log. See the Google Android documentation for how to
access the log."""
        raise NotImplementedError

    def ShowAlert(self, notice: str, /) -> None:
        """Display a temporary notification."""
        raise NotImplementedError

    def ShowChooseDialog(self, message: str, title: str, button1Text: str, button2Text: str, cancelable: bool, /) -> None:
        """Shows a dialog box with two buttons, from which the user can choose. If cancelable is
true there will be an additional CANCEL button. Pressing a button will raise
the AfterChoosing event. The "choice" parameter to
AfterChoosing will be the text on the button that was pressed, or "Cancel" if
the CANCEL button was pressed. If canceled, the TextInputCanceled event will also
run."""
        raise NotImplementedError

    def ShowMessageDialog(self, message: str, title: str, buttonText: str, /) -> None:
        """Display an alert dialog with a single button that dismisses the alert."""
        raise NotImplementedError

    def ShowPasswordDialog(self, message: str, title: str, cancelable: bool, /) -> None:
        """Shows a dialog box where the user can enter password (input is masked), after which the
AfterTextInput event will be raised. If cancelable is true
there will be an additional CANCEL button. The AfterTextInput and
TextInputCanceled events behave the same way as described in
ShowTextDialog."""
        raise NotImplementedError

    def ShowProgressDialog(self, message: str, title: str, /) -> None:
        """Shows a dialog box with an optional title and message (use empty strings if they are not
wanted). This dialog box contains a spinning artifact to indicate that the program is working.
It cannot be canceled by the user but must be dismissed by the App Inventor Program by using
the DismissProgressDialog method."""
        raise NotImplementedError

    def ShowTextDialog(self, message: str, title: str, cancelable: bool, /) -> None:
        """Shows a dialog box where the user can enter text, after which the
AfterTextInput  event will be raised. If cancelable is true
there will be an additional CANCEL button. Entering text will raise the
AfterTextInput event. The "response" parameter to
AfterTextInput  will be the text that was entered, or "Cancel" if the CANCEL
button was pressed. If canceled, the TextInputCanceled event will also run."""
        raise NotImplementedError

    def on_AfterChoosing(self, callback: Callable[[str], None], /) -> None:
        """AfterChoosing(choice)

Event after the user has made a selection for
ShowChooseDialog."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterChoosing(callback: Callable[['Notifier', bool, str], None], /) -> None:
        """AfterChoosing(choice)

Event after the user has made a selection for
ShowChooseDialog."""
        raise NotImplementedError

    def on_AfterTextInput(self, callback: Callable[[str], None], /) -> None:
        """AfterTextInput(response)

Event raised after the user has responded to ShowTextDialog."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterTextInput(callback: Callable[['Notifier', bool, str], None], /) -> None:
        """AfterTextInput(response)

Event raised after the user has responded to ShowTextDialog."""
        raise NotImplementedError

    def on_ChoosingCanceled(self, callback: Callable[[], None], /) -> None:
        """ChoosingCanceled()

Event raised when the user cancels choosing an option.
ShowChooseDialog."""
        raise NotImplementedError

    @staticmethod
    def on_any_ChoosingCanceled(callback: Callable[['Notifier', bool], None], /) -> None:
        """ChoosingCanceled()

Event raised when the user cancels choosing an option.
ShowChooseDialog."""
        raise NotImplementedError

    def on_TextInputCanceled(self, callback: Callable[[], None], /) -> None:
        """TextInputCanceled()

Event raised when the user cancels
ShowPasswordDialog, or
ShowTextDialog."""
        raise NotImplementedError

    @staticmethod
    def on_any_TextInputCanceled(callback: Callable[['Notifier', bool], None], /) -> None:
        """TextInputCanceled()

Event raised when the user cancels
ShowPasswordDialog, or
ShowTextDialog."""
        raise NotImplementedError

class PasswordTextBox(Component):
    """Users enter passwords in a password text box component, which hides the text that has been typed in it."""
    __data__ = {'desc': 'Users enter passwords in a password text box component, which hides the text that has been typed in it.', 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "The background color of the PasswordTextBox`. You can choose a color by name in the Designer or in\nthe Blocks Editor. The default background color is 'default' (shaded 3-D look)."}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'If set, user can enter text into the PasswordTextBox.'}, {'name': 'FontBold', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies whether the text of the PasswordTextBox should be bold.\nSome fonts do not support bold.'}, {'name': 'FontItalic', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies whether the text of the PasswordTextBox should be italic.\nSome fonts do not support italic.'}, {'name': 'FontSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text font size of the PasswordTextBox, measured in sp(scale-independent pixels).'}, {'name': 'FontTypeface', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'The text font face of the PasswordTextBox. Valid values are 0 (default), 1 (serif), 2 (sans\nserif), or 3 (monospace).'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the PasswordTextBox's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the PasswordTextBox's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Hint', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'PasswordTextBox hint for the user.'}, {'name': 'NumbersOnly', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'If true, then this PasswordTextBox accepts only numbers as keyboard input. Numbers can include a\ndecimal point and an optional leading minus sign. This applies to keyboard input only. Even\nif NumbersOnly is true, you can set the text to anything at all using the\n[Text`](#PasswordTextBox.Text) property.'}, {'name': 'PasswordVisible', 'type': 'bool', 'ro': False, 'do': False, 'bo': True, 'desc': 'Specifies whether the password is hidden (default) or shown.'}, {'name': 'Text', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'The text in the PasswordTextBox, which can be set by the programmer in the Designer or Blocks Editor,\nor it can be entered by the user (unless the Enabled property is false).'}, {'name': 'TextAlignment', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the alignment of the PasswordTextBox's text. Valid values are:\n0 (normal; e.g., left-justified if text is written left to right),\n1 (center), or\n2 (opposite; e.g., right-justified if text is written left to right)."}, {'name': 'TextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text color of the PasswordTextBox as an alpha-red-green-blue\ninteger.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the PasswordTextBox should be visible on the screen.  Value is true\nif the PasswordTextBox is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the PasswordTextBox, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the PasswordTextBox as a percentage\nof the Screen's Width."}], 'events': [{'name': 'GotFocus', 'args': [], 'desc': 'Event raised when the PasswordTextBox is selected for input, such as by\nthe user touching it.'}, {'name': 'LostFocus', 'args': [], 'desc': 'Event raised when the PasswordTextBox is no longer selected for input, such\nas if the user touches a different text box.'}], 'methods': [{'name': 'RequestFocus', 'args': [], 'returns': None, 'desc': 'Request focus to current PasswordTextBox.'}]}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., Enabled: bool=..., FontBold: bool=..., FontItalic: bool=..., FontSize: int=..., FontTypeface: str=..., Height: int=..., Hint: str=..., NumbersOnly: bool=..., Text: str=..., TextAlignment: int=..., TextColor: enums.Color=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """The background color of the PasswordTextBox`. You can choose a color by name in the Designer or in
the Blocks Editor. The default background color is 'default' (shaded 3-D look)."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """If set, user can enter text into the PasswordTextBox."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontSize(self) -> int:
        """Specifies the text font size of the PasswordTextBox, measured in sp(scale-independent pixels)."""
        raise NotImplementedError

    @FontSize.setter
    def FontSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the PasswordTextBox's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the PasswordTextBox's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Hint(self) -> str:
        """PasswordTextBox hint for the user."""
        raise NotImplementedError

    @Hint.setter
    def Hint(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def NumbersOnly(self) -> bool:
        """If true, then this PasswordTextBox accepts only numbers as keyboard input. Numbers can include a
decimal point and an optional leading minus sign. This applies to keyboard input only. Even
if NumbersOnly is true, you can set the text to anything at all using the
[Text`](#PasswordTextBox.Text) property."""
        raise NotImplementedError

    @NumbersOnly.setter
    def NumbersOnly(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def PasswordVisible(self) -> bool:
        """Specifies whether the password is hidden (default) or shown."""
        raise NotImplementedError

    @PasswordVisible.setter
    def PasswordVisible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Text(self) -> str:
        """The text in the PasswordTextBox, which can be set by the programmer in the Designer or Blocks Editor,
or it can be entered by the user (unless the Enabled property is false)."""
        raise NotImplementedError

    @Text.setter
    def Text(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def TextColor(self) -> enums.Color:
        """Specifies the text color of the PasswordTextBox as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @TextColor.setter
    def TextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the PasswordTextBox should be visible on the screen.  Value is true
if the PasswordTextBox is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the PasswordTextBox, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the PasswordTextBox as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def RequestFocus(self, /) -> None:
        """Request focus to current PasswordTextBox."""
        raise NotImplementedError

    def on_GotFocus(self, callback: Callable[[], None], /) -> None:
        """GotFocus()

Event raised when the PasswordTextBox is selected for input, such as by
the user touching it."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotFocus(callback: Callable[['PasswordTextBox', bool], None], /) -> None:
        """GotFocus()

Event raised when the PasswordTextBox is selected for input, such as by
the user touching it."""
        raise NotImplementedError

    def on_LostFocus(self, callback: Callable[[], None], /) -> None:
        """LostFocus()

Event raised when the PasswordTextBox is no longer selected for input, such
as if the user touches a different text box."""
        raise NotImplementedError

    @staticmethod
    def on_any_LostFocus(callback: Callable[['PasswordTextBox', bool], None], /) -> None:
        """LostFocus()

Event raised when the PasswordTextBox is no longer selected for input, such
as if the user touches a different text box."""
        raise NotImplementedError

class Form(Component):
    """Top-level component containing all other components in the program."""
    __data__ = {'desc': 'Top-level component containing all other components in the program.', 'properties': [{'name': 'AboutScreen', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Information about the screen. It appears when "About this Application" is selected from the\nsystem menu. Use it to tell users about your app. In multiple screen apps, each screen has its\nown AboutScreen info.'}, {'name': 'AccentColor', 'type': 'enums.Color', 'ro': False, 'do': True, 'bo': False, 'desc': 'This is the accent color used for highlights and other user interface accents in newer\nversions of Android. Components affected by this property include dialogs created by the\nNotifier, the DatePicker, and others.'}, {'name': 'AlignHorizontal', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'A number that encodes how contents of the screen are aligned horizontally. The choices are:\n1 (left aligned), 3 (horizontally centered), 2 (right aligned).'}, {'name': 'AlignVertical', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'A number that encodes how the contents of the arrangement are aligned vertically. The choices\nare: 1 (aligned at the top), 2 (vertically centered), 3 (aligned at the bottom). Vertical\nalignment has no effect if the screen is scrollable.'}, {'name': 'AppName', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'This is the display name of the installed application in the phone. If the AppName is blank,\nit will be set to the name of the project when the project is built.'}, {'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the Screen's background color as an alpha-red-green-blue\ninteger.  If an BackgroundImage has been set, the color\nchange will not be visible until the BackgroundImage is removed."}, {'name': 'BackgroundImage', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the path of the Screen's background image. If there is both an BackgroundImage\nand a BackgroundColor specified, only the BackgroundImage will be visible."}, {'name': 'BigDefaultText', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'When checked, all default size text will be increased in size.'}, {'name': 'BlocksToolkit', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'A JSON string representing the subset for the screen. Authors of template apps can use this to control what components, designer properties, and blocks are available in the project.'}, {'name': 'CloseScreenAnimation', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Sets the animation type for the transition of this form closing and returning\nto a form behind it in the activity stack.'}, {'name': 'DefaultFileScope', 'type': 'enums.FileScope', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies the default scope used when components access files. Note that the File\ncomponent has its own property for controlling file scopes.'}, {'name': 'Height', 'type': 'int', 'ro': True, 'do': False, 'bo': False, 'desc': 'Returns the Screen height in pixels (y-size).'}, {'name': 'HighContrast', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'When checked, there will be high contrast mode turned on.'}, {'name': 'Icon', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': "The image used for your App's display icon should be a square png or jpeg image with dimensions\nup to 1024x1024 pixels. Larger images may cause compiling or installing the app to fail.\nThe build server will generate images of standard dimensions for Android devices."}, {'name': 'OpenScreenAnimation', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Sets the animation type for the transition of this form opening.'}, {'name': 'Platform', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Gets the name of the underlying platform running the app. Currently, this is the text\n"Android". Other platforms may be supported in the future.'}, {'name': 'PlatformVersion', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Gets the version number of the platform running the app. This is typically a dotted version\nnumber, such as 10.0. Any value can be returned, however, so you should take care to handle\nunexpected data. If the platform version is unavailable, the empty text will be returned.'}, {'name': 'PrimaryColor', 'type': 'enums.Color', 'ro': False, 'do': True, 'bo': False, 'desc': "This is the primary color used as part of the Android theme, including coloring the Screen's\ntitle bar."}, {'name': 'PrimaryColorDark', 'type': 'enums.Color', 'ro': False, 'do': True, 'bo': False, 'desc': "This is the primary color used when the Theme property is specified to be Dark. It applies to\na number of elements, including the Screen's title bar."}, {'name': 'ScreenOrientation', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Declares the requested screen orientation, specified as a text value. Commonly used values are\nlandscape, portrait, sensor, user and unspecified. See the Android developer\ndocumentation for the complete list of possible\noptions.'}, {'name': 'Scrollable', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'When checked, there will be a vertical scrollbar on the screen, and the height of the\napplication can exceed the physical height of the device. When unchecked, the application\nheight is constrained to the height of the device.'}, {'name': 'ShowListsAsJson', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'If true (the default), lists will be shown as strings in JSON/Python notation\nfor example [1, "a", true]. If false, lists will be shown in the LISP\nnotation, for example (1 a true).\n\n   Note: This property appears only in Screen1 and the value for Screen1 determines the\nbehavior for all screens in the app.\n'}, {'name': 'ShowStatusBar', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'The status bar is the topmost bar on the screen. This property reports whether the status bar\nis visible.'}, {'name': 'Sizing', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'If set to responsive (the default), screen layouts will use the actual resolution of the\ndevice. See the documentation on responsive design in App\nInventor for more information.\nIf set to fixed, screen layouts will be created for a single fixed-size screen and autoscaled.\n\n   Note: This property appears on Screen1 only and controls the sizing for all screens in\nthe app.\n'}, {'name': 'Theme', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'Selects the theme for the application. Theme can only be set at compile time and the Companion\nwill approximate changes during live development. Possible options are:\n\n   \nClassic, which is the same as older versions of App Inventor;\nDevice Default, which gives the same theme as the version of Android running on the\ndevice and uses PrimaryColor for the Action Bar and has light buttons;\nBlack Title Text, which is the Device Default theme but with black title text; and\nDark, which is a dark version of the Device Default theme using PrimaryColorDark and\nhaving dark grey components.\n\n'}, {'name': 'Title', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': "Title property setter method: sets a new caption for the form in the\nform's title bar."}, {'name': 'TitleVisible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'The title bar is the top gray bar on the screen. This property reports whether the title bar\nis visible.'}, {'name': 'TutorialURL', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'A URL which will be opened on the left side panel (which can be toggled once it is open). This\nis intended for projects that have an in-line tutorial as part of the project. For security\nreasons, only tutorials hosted on http://appinventor.mit.edu or linked to from our URL\nshortener (http://appinv.us) may be used here. Other URLs will be silently ignored.'}, {'name': 'VersionCode', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': 'An integer value which must be incremented each time a new Android Application Package File\n(APK) is created for the Google Play Store.'}, {'name': 'VersionName', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'A string which can be changed to allow Google Play Store users to distinguish between\ndifferent versions of the App.'}, {'name': 'Width', 'type': 'int', 'ro': True, 'do': False, 'bo': False, 'desc': 'Returns the Screen width in pixels (x-size).'}], 'events': [{'name': 'BackPressed', 'args': [], 'desc': 'Device back button pressed.'}, {'name': 'ErrorOccurred', 'args': [{'name': 'component', 'type': 'Component'}, {'name': 'functionName', 'type': 'str'}, {'name': 'errorNumber', 'type': 'int'}, {'name': 'message', 'type': 'str'}], 'desc': 'Event raised when an error occurs. Only some errors will raise this condition.  For those errors, the system will show a notification by default.  You can use this event handler to prescribe an error behavior different than the default.'}, {'name': 'Initialize', 'args': [], 'desc': 'The Initialize event is run when the Screen starts and is only run once per screen.'}, {'name': 'OtherScreenClosed', 'args': [{'name': 'otherScreenName', 'type': 'str'}, {'name': 'result', 'type': 'Any'}], 'desc': 'Event raised when another screen has closed and control has returned to this screen.'}, {'name': 'PermissionDenied', 'args': [{'name': 'component', 'type': 'Component'}, {'name': 'functionName', 'type': 'str'}, {'name': 'permissionName', 'type': 'str'}], 'desc': 'Event to handle when the app user has denied a needed permission.'}, {'name': 'PermissionGranted', 'args': [{'name': 'permissionName', 'type': 'str'}], 'desc': 'Event to handle when the app user has granted a needed permission. This event is only run when permission is\ngranted in response to the AskForPermission method.'}, {'name': 'ScreenOrientationChanged', 'args': [], 'desc': 'Screen orientation changed'}], 'methods': [{'name': 'AskForPermission', 'args': [{'name': 'permissionName', 'type': 'str'}], 'returns': None, 'desc': 'Ask the user to grant access to a sensitive permission, such as ACCESS_FINE_LOCATION. This\nblock is typically used as part of a PermissionDenied\nevent to ask for permission. If the user grants permission, the\nPermissionGranted event will be run. If the user denies permission, the\nPermissionDenied event will be run.\n\n   Note: It is a best practice to only ask for permissions at the time they are needed,\nwhich App Inventor components will do when necessary. You should not use AskForPermission\nin your Initialize event unless access to that permission is critical to the\nbehavior of your app and is needed up front, such as location services for a navigation app.\n'}, {'name': 'HideKeyboard', 'args': [], 'returns': None, 'desc': 'Hide the soft keyboard'}]}

    def __init__(self, /, *, parent: Component=..., AboutScreen: str=..., AccentColor: enums.Color=..., AlignHorizontal: int=..., AlignVertical: int=..., AppName: str=..., BackgroundColor: enums.Color=..., BackgroundImage: str=..., BigDefaultText: bool=..., BlocksToolkit: str=..., CloseScreenAnimation: str=..., DefaultFileScope: enums.FileScope=..., Height: int=..., HighContrast: bool=..., Icon: str=..., OpenScreenAnimation: str=..., PrimaryColor: enums.Color=..., PrimaryColorDark: enums.Color=..., ScreenOrientation: str=..., Scrollable: bool=..., ShowListsAsJson: bool=..., ShowStatusBar: bool=..., Sizing: str=..., Theme: str=..., Title: str=..., TitleVisible: bool=..., TutorialURL: str=..., VersionCode: int=..., VersionName: str=..., Width: int=...):
        raise NotImplementedError

    @property
    def AboutScreen(self) -> str:
        """Information about the screen. It appears when "About this Application" is selected from the
system menu. Use it to tell users about your app. In multiple screen apps, each screen has its
own AboutScreen info."""
        raise NotImplementedError

    @AboutScreen.setter
    def AboutScreen(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def AlignHorizontal(self) -> int:
        """A number that encodes how contents of the screen are aligned horizontally. The choices are:
1 (left aligned), 3 (horizontally centered), 2 (right aligned)."""
        raise NotImplementedError

    @AlignHorizontal.setter
    def AlignHorizontal(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def AlignVertical(self) -> int:
        """A number that encodes how the contents of the arrangement are aligned vertically. The choices
are: 1 (aligned at the top), 2 (vertically centered), 3 (aligned at the bottom). Vertical
alignment has no effect if the screen is scrollable."""
        raise NotImplementedError

    @AlignVertical.setter
    def AlignVertical(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the Screen's background color as an alpha-red-green-blue
integer.  If an BackgroundImage has been set, the color
change will not be visible until the BackgroundImage is removed."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def BackgroundImage(self) -> str:
        """Specifies the path of the Screen's background image. If there is both an BackgroundImage
and a BackgroundColor specified, only the BackgroundImage will be visible."""
        raise NotImplementedError

    @BackgroundImage.setter
    def BackgroundImage(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def BigDefaultText(self) -> bool:
        """When checked, all default size text will be increased in size."""
        raise NotImplementedError

    @BigDefaultText.setter
    def BigDefaultText(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def CloseScreenAnimation(self) -> str:
        """Sets the animation type for the transition of this form closing and returning
to a form behind it in the activity stack."""
        raise NotImplementedError

    @CloseScreenAnimation.setter
    def CloseScreenAnimation(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Returns the Screen height in pixels (y-size)."""
        raise NotImplementedError

    @property
    def HighContrast(self) -> bool:
        """When checked, there will be high contrast mode turned on."""
        raise NotImplementedError

    @HighContrast.setter
    def HighContrast(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def OpenScreenAnimation(self) -> str:
        """Sets the animation type for the transition of this form opening."""
        raise NotImplementedError

    @OpenScreenAnimation.setter
    def OpenScreenAnimation(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Platform(self) -> str:
        """Gets the name of the underlying platform running the app. Currently, this is the text
"Android". Other platforms may be supported in the future."""
        raise NotImplementedError

    @property
    def PlatformVersion(self) -> str:
        """Gets the version number of the platform running the app. This is typically a dotted version
number, such as 10.0. Any value can be returned, however, so you should take care to handle
unexpected data. If the platform version is unavailable, the empty text will be returned."""
        raise NotImplementedError

    @property
    def ScreenOrientation(self) -> str:
        """Declares the requested screen orientation, specified as a text value. Commonly used values are
landscape, portrait, sensor, user and unspecified. See the Android developer
documentation for the complete list of possible
options."""
        raise NotImplementedError

    @ScreenOrientation.setter
    def ScreenOrientation(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Scrollable(self) -> bool:
        """When checked, there will be a vertical scrollbar on the screen, and the height of the
application can exceed the physical height of the device. When unchecked, the application
height is constrained to the height of the device."""
        raise NotImplementedError

    @Scrollable.setter
    def Scrollable(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def ShowStatusBar(self) -> bool:
        """The status bar is the topmost bar on the screen. This property reports whether the status bar
is visible."""
        raise NotImplementedError

    @ShowStatusBar.setter
    def ShowStatusBar(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Title(self) -> str:
        """Title property setter method: sets a new caption for the form in the
form's title bar."""
        raise NotImplementedError

    @Title.setter
    def Title(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def TitleVisible(self) -> bool:
        """The title bar is the top gray bar on the screen. This property reports whether the title bar
is visible."""
        raise NotImplementedError

    @TitleVisible.setter
    def TitleVisible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Returns the Screen width in pixels (x-size)."""
        raise NotImplementedError

    def AskForPermission(self, permissionName: str, /) -> None:
        """Ask the user to grant access to a sensitive permission, such as ACCESS_FINE_LOCATION. This
block is typically used as part of a PermissionDenied
event to ask for permission. If the user grants permission, the
PermissionGranted event will be run. If the user denies permission, the
PermissionDenied event will be run.

   Note: It is a best practice to only ask for permissions at the time they are needed,
which App Inventor components will do when necessary. You should not use AskForPermission
in your Initialize event unless access to that permission is critical to the
behavior of your app and is needed up front, such as location services for a navigation app.
"""
        raise NotImplementedError

    def HideKeyboard(self, /) -> None:
        """Hide the soft keyboard"""
        raise NotImplementedError

    def on_BackPressed(self, callback: Callable[[], None], /) -> None:
        """BackPressed()

Device back button pressed."""
        raise NotImplementedError

    def on_ErrorOccurred(self, callback: Callable[[Component, str, int, str], None], /) -> None:
        """ErrorOccurred(component, functionName, errorNumber, message)

Event raised when an error occurs. Only some errors will raise this condition.  For those errors, the system will show a notification by default.  You can use this event handler to prescribe an error behavior different than the default."""
        raise NotImplementedError

    def on_Initialize(self, callback: Callable[[], None], /) -> None:
        """Initialize()

The Initialize event is run when the Screen starts and is only run once per screen."""
        raise NotImplementedError

    def on_OtherScreenClosed(self, callback: Callable[[str, Any], None], /) -> None:
        """OtherScreenClosed(otherScreenName, result)

Event raised when another screen has closed and control has returned to this screen."""
        raise NotImplementedError

    def on_PermissionDenied(self, callback: Callable[[Component, str, str], None], /) -> None:
        """PermissionDenied(component, functionName, permissionName)

Event to handle when the app user has denied a needed permission."""
        raise NotImplementedError

    def on_PermissionGranted(self, callback: Callable[[str], None], /) -> None:
        """PermissionGranted(permissionName)

Event to handle when the app user has granted a needed permission. This event is only run when permission is
granted in response to the AskForPermission method."""
        raise NotImplementedError

    def on_ScreenOrientationChanged(self, callback: Callable[[], None], /) -> None:
        """ScreenOrientationChanged()

Screen orientation changed"""
        raise NotImplementedError

class Slider(Component):
    """This class is used to display a Slider."""
    __data__ = {'desc': 'This class is used to display a Slider.', 'properties': [{'name': 'ColorLeft', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the color of the slider bar to the left of the thumb as an alpha-red-green-blue\ninteger, i.e., 0xAARRGGBB.  An alpha of 00\nindicates fully transparent and FF means opaque.'}, {'name': 'ColorRight', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the color of the slider bar to the right of the thumb as an alpha-red-green-blue\ninteger, i.e., 0xAARRGGBB.  An alpha of 00\nindicates fully transparent and FF means opaque.'}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the Slider's vertical height as a percentage\nof the Screen's Height."}, {'name': 'MaxValue', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Sets the maximum value of slider. If the new maximum is less than the\ncurrent minimum, then minimum and maximum will both be set to this value.\nSetting MaxValue resets the thumb position to halfway between MinValue\nand MaxValue and signals the PositionChanged` event.'}, {'name': 'MinValue', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Sets the minimum value of slider. If the new minimum is greater than the\ncurrent maximum, then minimum and maximum will both be set to this value.\nSetting MinValue resets the thumb position to halfway between MinValue\nand MaxValue and signals the PositionChanged`\nevent.'}, {'name': 'ThumbEnabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Whether or not the slider thumb is being be shown.'}, {'name': 'ThumbPosition', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Sets the position of the slider thumb. If this value is greater than MaxValue,\nthen it will be set to same value as MaxValue. If this value is less than\nMinValue, then it will be set to same value as MinValue.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the Slider should be visible on the screen.  Value is true\nif the Slider is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the Slider, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the Slider as a percentage\nof the Screen's Width."}], 'events': [{'name': 'PositionChanged', 'args': [{'name': 'thumbPosition', 'type': 'int'}], 'desc': 'Indicates that position of the slider thumb has changed.'}], 'methods': []}

    def __init__(self, /, *, parent: Component=..., ColorLeft: enums.Color=..., ColorRight: enums.Color=..., MaxValue: int=..., MinValue: int=..., ThumbEnabled: bool=..., ThumbPosition: int=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def ColorLeft(self) -> enums.Color:
        """Specifies the color of the slider bar to the left of the thumb as an alpha-red-green-blue
integer, i.e., 0xAARRGGBB.  An alpha of 00
indicates fully transparent and FF means opaque."""
        raise NotImplementedError

    @ColorLeft.setter
    def ColorLeft(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def ColorRight(self) -> enums.Color:
        """Specifies the color of the slider bar to the right of the thumb as an alpha-red-green-blue
integer, i.e., 0xAARRGGBB.  An alpha of 00
indicates fully transparent and FF means opaque."""
        raise NotImplementedError

    @ColorRight.setter
    def ColorRight(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the Slider's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def MaxValue(self) -> int:
        """Sets the maximum value of slider. If the new maximum is less than the
current minimum, then minimum and maximum will both be set to this value.
Setting MaxValue resets the thumb position to halfway between MinValue
and MaxValue and signals the PositionChanged` event."""
        raise NotImplementedError

    @MaxValue.setter
    def MaxValue(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def MinValue(self) -> int:
        """Sets the minimum value of slider. If the new minimum is greater than the
current maximum, then minimum and maximum will both be set to this value.
Setting MinValue resets the thumb position to halfway between MinValue
and MaxValue and signals the PositionChanged`
event."""
        raise NotImplementedError

    @MinValue.setter
    def MinValue(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def ThumbEnabled(self) -> bool:
        """Whether or not the slider thumb is being be shown."""
        raise NotImplementedError

    @ThumbEnabled.setter
    def ThumbEnabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def ThumbPosition(self) -> int:
        """Sets the position of the slider thumb. If this value is greater than MaxValue,
then it will be set to same value as MaxValue. If this value is less than
MinValue, then it will be set to same value as MinValue."""
        raise NotImplementedError

    @ThumbPosition.setter
    def ThumbPosition(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the Slider should be visible on the screen.  Value is true
if the Slider is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the Slider, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the Slider as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def on_PositionChanged(self, callback: Callable[[int], None], /) -> None:
        """PositionChanged(thumbPosition)

Indicates that position of the slider thumb has changed."""
        raise NotImplementedError

    @staticmethod
    def on_any_PositionChanged(callback: Callable[['Slider', bool, int], None], /) -> None:
        """PositionChanged(thumbPosition)

Indicates that position of the slider thumb has changed."""
        raise NotImplementedError

class Spinner(Component):
    """A Spinner component that displays a dialog with a list of elements. These elements can be set
in the Designer or Blocks Editor by setting the ElementsFromString property to
a comma-separated list of values (for example, choice 1, choice 2, choice 3) or by setting the
Elements property to a List in the Blocks editor. Spinners are created with
the first item already selected, so selecting it does not generate an
AfterSelecting event. Consequently it's useful to make the first Spinner item
be a non-choice like "Select from belowâ\x80¦"."""
    __data__ = {'desc': 'A Spinner component that displays a dialog with a list of elements. These elements can be set\nin the Designer or Blocks Editor by setting the ElementsFromString property to\na comma-separated list of values (for example, choice 1, choice 2, choice 3) or by setting the\nElements property to a List in the Blocks editor. Spinners are created with\nthe first item already selected, so selecting it does not generate an\nAfterSelecting event. Consequently it\'s useful to make the first Spinner item\nbe a non-choice like "Select from belowâ\x80¦".', 'properties': [{'name': 'Elements', 'type': 'list', 'ro': False, 'do': False, 'bo': True, 'desc': 'Specifies the list of choices to display.'}, {'name': 'ElementsFromString', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Set the list of choices from a string of comma-separated values.'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the Spinner's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the Spinner's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Prompt', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text used for the title of the Spinner window.'}, {'name': 'Selection', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the current selected item in the Spinner.'}, {'name': 'SelectionIndex', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': 'Set the Spinner selection to the element at the given index.\nIf an attempt is made to set this to a number less than 1 or greater than the number of\nitems in the Spinner, SelectionIndex will be set to 0, and Selection\nwill be set to the empty text.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the Spinner should be visible on the screen.  Value is true\nif the Spinner is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the Spinner, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the Spinner as a percentage\nof the Screen's Width."}], 'events': [{'name': 'AfterSelecting', 'args': [{'name': 'selection', 'type': 'str'}], 'desc': 'Event called after the user selects an item from the dropdown list.'}], 'methods': [{'name': 'DisplayDropdown', 'args': [], 'returns': None, 'desc': 'Displays the dropdown list for selection, same action as when the user clicks on the spinner.'}]}

    def __init__(self, /, *, parent: Component=..., ElementsFromString: str=..., Height: int=..., Prompt: str=..., Selection: str=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def Elements(self) -> list:
        """Specifies the list of choices to display."""
        raise NotImplementedError

    @Elements.setter
    def Elements(self, value: list, /) -> None:
        raise NotImplementedError

    @property
    def ElementsFromString(self) -> str:
        """Set the list of choices from a string of comma-separated values."""
        raise NotImplementedError

    @ElementsFromString.setter
    def ElementsFromString(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the Spinner's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the Spinner's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Prompt(self) -> str:
        """Specifies the text used for the title of the Spinner window."""
        raise NotImplementedError

    @Prompt.setter
    def Prompt(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Selection(self) -> str:
        """Specifies the current selected item in the Spinner."""
        raise NotImplementedError

    @Selection.setter
    def Selection(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def SelectionIndex(self) -> int:
        """Set the Spinner selection to the element at the given index.
If an attempt is made to set this to a number less than 1 or greater than the number of
items in the Spinner, SelectionIndex will be set to 0, and Selection
will be set to the empty text."""
        raise NotImplementedError

    @SelectionIndex.setter
    def SelectionIndex(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the Spinner should be visible on the screen.  Value is true
if the Spinner is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the Spinner, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the Spinner as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def DisplayDropdown(self, /) -> None:
        """Displays the dropdown list for selection, same action as when the user clicks on the spinner."""
        raise NotImplementedError

    def on_AfterSelecting(self, callback: Callable[[str], None], /) -> None:
        """AfterSelecting(selection)

Event called after the user selects an item from the dropdown list."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterSelecting(callback: Callable[['Spinner', bool, str], None], /) -> None:
        """AfterSelecting(selection)

Event called after the user selects an item from the dropdown list."""
        raise NotImplementedError

class Switch(Component):
    """Switch components can detect user taps and can change their boolean state in response. They
are identical to CheckBoxes except in appearance."""
    __data__ = {'desc': 'Switch components can detect user taps and can change their boolean state in response. They\nare identical to CheckBoxes except in appearance.', 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the background color of the Switch as an alpha-red-green-blue\ninteger.'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the Switch should be active and clickable.'}, {'name': 'FontBold', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies whether the text of the Switch should be bold.\nSome fonts do not support bold.'}, {'name': 'FontItalic', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies whether the text of the Switch should be italic.\nSome fonts do not support italic.'}, {'name': 'FontSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text font size of the Switch, measured in sp(scale-independent pixels).'}, {'name': 'FontTypeface', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies the text font face of the Switch as default, serif, sans\nserif, or monospace.'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the Switch's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the Switch's vertical height as a percentage\nof the Screen's Height."}, {'name': 'On', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'True if the switch is in the On state, false otherwise.'}, {'name': 'Text', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text displayed by the Switch.'}, {'name': 'TextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text color of the Switch as an alpha-red-green-blue\ninteger.'}, {'name': 'ThumbColorActive', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the Switch's thumb color when switch is in the On state."}, {'name': 'ThumbColorInactive', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the Switch's thumb color when switch is in the Off state."}, {'name': 'TrackColorActive', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the Switch's track color when in the On state."}, {'name': 'TrackColorInactive', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the Switch's track color when in the Off state."}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the Switch should be visible on the screen.  Value is true\nif the Switch is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the Switch, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the Switch as a percentage\nof the Screen's Width."}], 'events': [{'name': 'Changed', 'args': [], 'desc': 'User change the state of the Switch from On to Off or back.'}, {'name': 'GotFocus', 'args': [], 'desc': 'Switch became the focused component.'}, {'name': 'LostFocus', 'args': [], 'desc': 'Switch stopped being the focused component.'}], 'methods': []}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., Enabled: bool=..., FontBold: bool=..., FontItalic: bool=..., FontSize: int=..., FontTypeface: str=..., Height: int=..., On: bool=..., Text: str=..., TextColor: enums.Color=..., ThumbColorActive: enums.Color=..., ThumbColorInactive: enums.Color=..., TrackColorActive: enums.Color=..., TrackColorInactive: enums.Color=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the background color of the Switch as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Specifies whether the Switch should be active and clickable."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontSize(self) -> int:
        """Specifies the text font size of the Switch, measured in sp(scale-independent pixels)."""
        raise NotImplementedError

    @FontSize.setter
    def FontSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the Switch's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the Switch's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def On(self) -> bool:
        """True if the switch is in the On state, false otherwise."""
        raise NotImplementedError

    @On.setter
    def On(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Text(self) -> str:
        """Specifies the text displayed by the Switch."""
        raise NotImplementedError

    @Text.setter
    def Text(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def TextColor(self) -> enums.Color:
        """Specifies the text color of the Switch as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @TextColor.setter
    def TextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def ThumbColorActive(self) -> enums.Color:
        """Specifies the Switch's thumb color when switch is in the On state."""
        raise NotImplementedError

    @ThumbColorActive.setter
    def ThumbColorActive(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def ThumbColorInactive(self) -> enums.Color:
        """Specifies the Switch's thumb color when switch is in the Off state."""
        raise NotImplementedError

    @ThumbColorInactive.setter
    def ThumbColorInactive(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def TrackColorActive(self) -> enums.Color:
        """Specifies the Switch's track color when in the On state."""
        raise NotImplementedError

    @TrackColorActive.setter
    def TrackColorActive(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def TrackColorInactive(self) -> enums.Color:
        """Specifies the Switch's track color when in the Off state."""
        raise NotImplementedError

    @TrackColorInactive.setter
    def TrackColorInactive(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the Switch should be visible on the screen.  Value is true
if the Switch is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the Switch, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the Switch as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def on_Changed(self, callback: Callable[[], None], /) -> None:
        """Changed()

User change the state of the Switch from On to Off or back."""
        raise NotImplementedError

    @staticmethod
    def on_any_Changed(callback: Callable[['Switch', bool], None], /) -> None:
        """Changed()

User change the state of the Switch from On to Off or back."""
        raise NotImplementedError

    def on_GotFocus(self, callback: Callable[[], None], /) -> None:
        """GotFocus()

Switch became the focused component."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotFocus(callback: Callable[['Switch', bool], None], /) -> None:
        """GotFocus()

Switch became the focused component."""
        raise NotImplementedError

    def on_LostFocus(self, callback: Callable[[], None], /) -> None:
        """LostFocus()

Switch stopped being the focused component."""
        raise NotImplementedError

    @staticmethod
    def on_any_LostFocus(callback: Callable[['Switch', bool], None], /) -> None:
        """LostFocus()

Switch stopped being the focused component."""
        raise NotImplementedError

class TextBox(Component):
    """Users enter text in a text box component."""
    __data__ = {'desc': 'Users enter text in a text box component.', 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "The background color of the TextBox`. You can choose a color by name in the Designer or in\nthe Blocks Editor. The default background color is 'default' (shaded 3-D look)."}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'If set, user can enter text into the TextBox.'}, {'name': 'FontBold', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies whether the text of the TextBox should be bold.\nSome fonts do not support bold.'}, {'name': 'FontItalic', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies whether the text of the TextBox should be italic.\nSome fonts do not support italic.'}, {'name': 'FontSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text font size of the TextBox, measured in sp(scale-independent pixels).'}, {'name': 'FontTypeface', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'The text font face of the TextBox. Valid values are 0 (default), 1 (serif), 2 (sans\nserif), or 3 (monospace).'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the TextBox's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the TextBox's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Hint', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'TextBox hint for the user.'}, {'name': 'MultiLine', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'If true, then this TextBox accepts multiple lines of input, which are entered using the\nreturn key. For single line text boxes there is a Done key instead of a return key, and\npressing Done hides the keyboard. The app should call the HideKeyboard method to hide the\nkeyboard for a mutiline text box.'}, {'name': 'NumbersOnly', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'If true, then this TextBox accepts only numbers as keyboard input. Numbers can include a\ndecimal point and an optional leading minus sign. This applies to keyboard input only. Even\nif NumbersOnly is true, you can set the text to anything at all using the\n[Text`](#TextBox.Text) property.'}, {'name': 'ReadOnly', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Whether the TextBox is read-only. By default, this is true.'}, {'name': 'Text', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'The text in the TextBox, which can be set by the programmer in the Designer or Blocks Editor,\nor it can be entered by the user (unless the Enabled property is false).'}, {'name': 'TextAlignment', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the alignment of the TextBox's text. Valid values are:\n0 (normal; e.g., left-justified if text is written left to right),\n1 (center), or\n2 (opposite; e.g., right-justified if text is written left to right)."}, {'name': 'TextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text color of the TextBox as an alpha-red-green-blue\ninteger.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the TextBox should be visible on the screen.  Value is true\nif the TextBox is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the TextBox, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the TextBox as a percentage\nof the Screen's Width."}], 'events': [{'name': 'GotFocus', 'args': [], 'desc': 'Event raised when the TextBox is selected for input, such as by\nthe user touching it.'}, {'name': 'LostFocus', 'args': [], 'desc': 'Event raised when the TextBox is no longer selected for input, such\nas if the user touches a different text box.'}], 'methods': [{'name': 'HideKeyboard', 'args': [], 'returns': None, 'desc': 'Hide the keyboard. Only multiline text boxes need this. Single line text boxes close the\nkeyboard when the users presses the Done key.'}, {'name': 'RequestFocus', 'args': [], 'returns': None, 'desc': 'Request focus to current TextBox.'}]}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., Enabled: bool=..., FontBold: bool=..., FontItalic: bool=..., FontSize: int=..., FontTypeface: str=..., Height: int=..., Hint: str=..., MultiLine: bool=..., NumbersOnly: bool=..., ReadOnly: bool=..., Text: str=..., TextAlignment: int=..., TextColor: enums.Color=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """The background color of the TextBox`. You can choose a color by name in the Designer or in
the Blocks Editor. The default background color is 'default' (shaded 3-D look)."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """If set, user can enter text into the TextBox."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontSize(self) -> int:
        """Specifies the text font size of the TextBox, measured in sp(scale-independent pixels)."""
        raise NotImplementedError

    @FontSize.setter
    def FontSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the TextBox's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the TextBox's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Hint(self) -> str:
        """TextBox hint for the user."""
        raise NotImplementedError

    @Hint.setter
    def Hint(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def MultiLine(self) -> bool:
        """If true, then this TextBox accepts multiple lines of input, which are entered using the
return key. For single line text boxes there is a Done key instead of a return key, and
pressing Done hides the keyboard. The app should call the HideKeyboard method to hide the
keyboard for a mutiline text box."""
        raise NotImplementedError

    @MultiLine.setter
    def MultiLine(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def NumbersOnly(self) -> bool:
        """If true, then this TextBox accepts only numbers as keyboard input. Numbers can include a
decimal point and an optional leading minus sign. This applies to keyboard input only. Even
if NumbersOnly is true, you can set the text to anything at all using the
[Text`](#TextBox.Text) property."""
        raise NotImplementedError

    @NumbersOnly.setter
    def NumbersOnly(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def ReadOnly(self) -> bool:
        """Whether the TextBox is read-only. By default, this is true."""
        raise NotImplementedError

    @ReadOnly.setter
    def ReadOnly(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Text(self) -> str:
        """The text in the TextBox, which can be set by the programmer in the Designer or Blocks Editor,
or it can be entered by the user (unless the Enabled property is false)."""
        raise NotImplementedError

    @Text.setter
    def Text(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def TextColor(self) -> enums.Color:
        """Specifies the text color of the TextBox as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @TextColor.setter
    def TextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the TextBox should be visible on the screen.  Value is true
if the TextBox is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the TextBox, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the TextBox as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def HideKeyboard(self, /) -> None:
        """Hide the keyboard. Only multiline text boxes need this. Single line text boxes close the
keyboard when the users presses the Done key."""
        raise NotImplementedError

    def RequestFocus(self, /) -> None:
        """Request focus to current TextBox."""
        raise NotImplementedError

    def on_GotFocus(self, callback: Callable[[], None], /) -> None:
        """GotFocus()

Event raised when the TextBox is selected for input, such as by
the user touching it."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotFocus(callback: Callable[['TextBox', bool], None], /) -> None:
        """GotFocus()

Event raised when the TextBox is selected for input, such as by
the user touching it."""
        raise NotImplementedError

    def on_LostFocus(self, callback: Callable[[], None], /) -> None:
        """LostFocus()

Event raised when the TextBox is no longer selected for input, such
as if the user touches a different text box."""
        raise NotImplementedError

    @staticmethod
    def on_any_LostFocus(callback: Callable[['TextBox', bool], None], /) -> None:
        """LostFocus()

Event raised when the TextBox is no longer selected for input, such
as if the user touches a different text box."""
        raise NotImplementedError

class TimePicker(Component):
    """A button that, when clicked on, opens a dialog to allow the user to select a time."""
    __data__ = {'desc': 'A button that, when clicked on, opens a dialog to allow the user to select a time.', 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the TimePicker's background color as an alpha-red-green-blue\ninteger.  If an Image has been set, the color\nchange will not be visible until the Image is removed."}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the TimePicker should be active and clickable.'}, {'name': 'FontBold', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the text of the TimePicker should be bold.\nSome fonts do not support bold.'}, {'name': 'FontItalic', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the text of the TimePicker should be italic.\nSome fonts do not support italic.'}, {'name': 'FontSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text font size of the TimePicker, measured in sp(scale-independent pixels).'}, {'name': 'FontTypeface', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the text font face of the TimePicker as default, serif, sans\nserif, monospace, or custom font typeface. To add a custom typeface,\nupload a .ttf file to the project's media."}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the TimePicker's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the TimePicker's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Hour', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the hour of the time that was last picked using the TimePicker`.\nThe time returned is always in the 24hour format.'}, {'name': 'Image', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the path of the TimePicker's image. If there is both an Image and a\nBackgroundColor specified, only the Image will be visible."}, {'name': 'Instant', 'type': 'enums.Instant', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the instant in time that was last picked using the TimePicker.'}, {'name': 'Minute', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the hour of the time that was last picked using the TimePicker.\nThe time returned is always in the 24hour format.'}, {'name': 'Shape', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies the shape of the TimePicker. The valid values for this property are 0 (default),\n1 (rounded), 2 (rectangle), and 3 (oval). The Shape will not be visible if an\nImage is used.'}, {'name': 'ShowFeedback', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies if a visual feedback should be shown when a TimePicker with an assigned\nImage is pressed.'}, {'name': 'Text', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text displayed by the TimePicker.'}, {'name': 'TextAlignment', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the alignment of the TimePicker's text. Valid values are:\n0 (normal; e.g., left-justified if text is written left to right),\n1 (center), or\n2 (opposite; e.g., right-justified if text is written left to right)."}, {'name': 'TextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text color of the TimePicker as an alpha-red-green-blue\ninteger.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the TimePicker should be visible on the screen.  Value is true\nif the TimePicker is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the TimePicker, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the TimePicker as a percentage\nof the Screen's Width."}], 'events': [{'name': 'AfterTimeSet', 'args': [], 'desc': 'This event is run when a user has set the time in the popup dialog.'}, {'name': 'GotFocus', 'args': [], 'desc': 'Indicates the cursor moved over the TimePicker so it is now possible\nto click it.'}, {'name': 'LostFocus', 'args': [], 'desc': 'Indicates the cursor moved away from the TimePicker so it is now no\nlonger possible to click it.'}, {'name': 'TouchDown', 'args': [], 'desc': 'Indicates that the TimePicker was pressed down.'}, {'name': 'TouchUp', 'args': [], 'desc': 'Indicates that the TimePicker has been released.'}], 'methods': [{'name': 'LaunchPicker', 'args': [], 'returns': None, 'desc': 'Launches the TimePicker dialog.'}, {'name': 'SetTimeToDisplay', 'args': [{'name': 'hour', 'type': 'int'}, {'name': 'minute', 'type': 'int'}], 'returns': None, 'desc': 'Allows the user to set the time to be displayed when the TimePicker opens. Valid values for\nthe hour field are 0-23 and 0-59 for the second field.'}, {'name': 'SetTimeToDisplayFromInstant', 'args': [{'name': 'instant', 'type': 'enums.Instant'}], 'returns': None, 'desc': 'Allows the instant to set the hour and minute to be displayed when the TimePicker opens.\nInstants are used in Clock, DatePicker, and TimePicker\ncomponents.'}]}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., Enabled: bool=..., FontBold: bool=..., FontItalic: bool=..., FontSize: int=..., FontTypeface: str=..., Height: int=..., Image: str=..., Shape: int=..., ShowFeedback: bool=..., Text: str=..., TextAlignment: int=..., TextColor: enums.Color=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the TimePicker's background color as an alpha-red-green-blue
integer.  If an Image has been set, the color
change will not be visible until the Image is removed."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Specifies whether the TimePicker should be active and clickable."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontBold(self) -> bool:
        """Specifies whether the text of the TimePicker should be bold.
Some fonts do not support bold."""
        raise NotImplementedError

    @FontBold.setter
    def FontBold(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontItalic(self) -> bool:
        """Specifies whether the text of the TimePicker should be italic.
Some fonts do not support italic."""
        raise NotImplementedError

    @FontItalic.setter
    def FontItalic(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontSize(self) -> int:
        """Specifies the text font size of the TimePicker, measured in sp(scale-independent pixels)."""
        raise NotImplementedError

    @FontSize.setter
    def FontSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the TimePicker's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the TimePicker's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Hour(self) -> int:
        """Returns the hour of the time that was last picked using the TimePicker`.
The time returned is always in the 24hour format."""
        raise NotImplementedError

    @property
    def Image(self) -> str:
        """Specifies the path of the TimePicker's image. If there is both an Image and a
BackgroundColor specified, only the Image will be visible."""
        raise NotImplementedError

    @Image.setter
    def Image(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Instant(self) -> enums.Instant:
        """Returns the instant in time that was last picked using the TimePicker."""
        raise NotImplementedError

    @property
    def Minute(self) -> int:
        """Returns the hour of the time that was last picked using the TimePicker.
The time returned is always in the 24hour format."""
        raise NotImplementedError

    @property
    def ShowFeedback(self) -> bool:
        """Specifies if a visual feedback should be shown when a TimePicker with an assigned
Image is pressed."""
        raise NotImplementedError

    @ShowFeedback.setter
    def ShowFeedback(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Text(self) -> str:
        """Specifies the text displayed by the TimePicker."""
        raise NotImplementedError

    @Text.setter
    def Text(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def TextColor(self) -> enums.Color:
        """Specifies the text color of the TimePicker as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @TextColor.setter
    def TextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the TimePicker should be visible on the screen.  Value is true
if the TimePicker is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the TimePicker, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the TimePicker as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def LaunchPicker(self, /) -> None:
        """Launches the TimePicker dialog."""
        raise NotImplementedError

    def SetTimeToDisplay(self, hour: int, minute: int, /) -> None:
        """Allows the user to set the time to be displayed when the TimePicker opens. Valid values for
the hour field are 0-23 and 0-59 for the second field."""
        raise NotImplementedError

    def SetTimeToDisplayFromInstant(self, instant: enums.Instant, /) -> None:
        """Allows the instant to set the hour and minute to be displayed when the TimePicker opens.
Instants are used in Clock, DatePicker, and TimePicker
components."""
        raise NotImplementedError

    def on_AfterTimeSet(self, callback: Callable[[], None], /) -> None:
        """AfterTimeSet()

This event is run when a user has set the time in the popup dialog."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterTimeSet(callback: Callable[['TimePicker', bool], None], /) -> None:
        """AfterTimeSet()

This event is run when a user has set the time in the popup dialog."""
        raise NotImplementedError

    def on_GotFocus(self, callback: Callable[[], None], /) -> None:
        """GotFocus()

Indicates the cursor moved over the TimePicker so it is now possible
to click it."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotFocus(callback: Callable[['TimePicker', bool], None], /) -> None:
        """GotFocus()

Indicates the cursor moved over the TimePicker so it is now possible
to click it."""
        raise NotImplementedError

    def on_LostFocus(self, callback: Callable[[], None], /) -> None:
        """LostFocus()

Indicates the cursor moved away from the TimePicker so it is now no
longer possible to click it."""
        raise NotImplementedError

    @staticmethod
    def on_any_LostFocus(callback: Callable[['TimePicker', bool], None], /) -> None:
        """LostFocus()

Indicates the cursor moved away from the TimePicker so it is now no
longer possible to click it."""
        raise NotImplementedError

    def on_TouchDown(self, callback: Callable[[], None], /) -> None:
        """TouchDown()

Indicates that the TimePicker was pressed down."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchDown(callback: Callable[['TimePicker', bool], None], /) -> None:
        """TouchDown()

Indicates that the TimePicker was pressed down."""
        raise NotImplementedError

    def on_TouchUp(self, callback: Callable[[], None], /) -> None:
        """TouchUp()

Indicates that the TimePicker has been released."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchUp(callback: Callable[['TimePicker', bool], None], /) -> None:
        """TouchUp()

Indicates that the TimePicker has been released."""
        raise NotImplementedError

class WebViewer(Component):
    """Component for viewing Web pages."""
    __data__ = {'desc': 'Component for viewing Web pages.', 'properties': [{'name': 'CurrentPageTitle', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the title of the page currently being viewed'}, {'name': 'CurrentUrl', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the URL currently being viewed. This could be different from the HomeUrl\nif new pages were visited by following links.'}, {'name': 'FollowLinks', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Determines whether to follow links when they are tapped in the WebViewer. If you follow\nlinks, you can use GoBack and GoForward to navigate the browser history.'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the WebViewer's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the WebViewer's vertical height as a percentage\nof the Screen's Height."}, {'name': 'HomeUrl', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the URL of the page the WebViewer should initially open to. Setting this will\nload the page.'}, {'name': 'IgnoreSslErrors', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Determine whether or not to ignore SSL errors. Set to true to ignore errors.\nUse this to accept self signed certificates from websites.'}, {'name': 'PromptforPermission', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Determine if the user should be prompted for permission to use the geolocation API while in\nthe WebViewer. If true, prompt the user of the WebViewer to give\npermission to access the geolocation API. If false, assume permission is\ngranted.'}, {'name': 'UsesLocation', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies whether or not this WebViewer can access the JavaScript\ngeolocation API.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the WebViewer should be visible on the screen.  Value is true\nif the WebViewer is showing and false if hidden.'}, {'name': 'WebViewString', 'type': 'str', 'ro': False, 'do': False, 'bo': True, 'desc': "Gets the WebView's String, which is viewable through Javascript in the WebView as the\nwindow.AppInventor object."}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the WebViewer, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the WebViewer as a percentage\nof the Screen's Width."}], 'events': [{'name': 'BeforePageLoad', 'args': [{'name': 'url', 'type': 'str'}], 'desc': 'When a page is about to load this event is run.'}, {'name': 'ErrorOccurred', 'args': [{'name': 'errorCode', 'type': 'int'}, {'name': 'description', 'type': 'str'}, {'name': 'failingUrl', 'type': 'str'}], 'desc': 'When an error occurs this event is run.'}, {'name': 'PageLoaded', 'args': [{'name': 'url', 'type': 'str'}], 'desc': 'When a page is finished loading this event is run.'}, {'name': 'WebViewStringChange', 'args': [{'name': 'value', 'type': 'str'}], 'desc': 'Event that runs when the AppInventor.setWebViewString method is called from JavaScript.\nThe new WebViewString is given by the value parameter.'}], 'methods': [{'name': 'CanGoBack', 'args': [], 'returns': 'bool', 'desc': 'Returns true if the WebViewer can go back in the history list.'}, {'name': 'CanGoForward', 'args': [], 'returns': 'bool', 'desc': 'Returns true if the WebViewer can go forward in the history list.'}, {'name': 'ClearCaches', 'args': [], 'returns': None, 'desc': 'Clear the internal webview cache, both ram and disk. This is useful\nwhen using the WebViewer to poll a page that may not be sending\nappropriate cache control headers.'}, {'name': 'ClearCookies', 'args': [], 'returns': None, 'desc': "Clear the webview's cookies. This is useful if you want to\nsign the user out of a website that uses them to store logins."}, {'name': 'ClearLocations', 'args': [], 'returns': None, 'desc': 'Clear Stored Location permissions. When the geolocation API is used in\nthe WebViewer, the end user is prompted on a per URL basis for whether\nor not permission should be granted to access their location. This\nfunction clears this information for all locations.\n\n   As the permissions interface is not available on phones older then\nEclair, this function is a no-op on older phones.\n'}, {'name': 'GoBack', 'args': [], 'returns': None, 'desc': 'Go back to the previous page in the history list. Does nothing if there is no previous page.'}, {'name': 'GoForward', 'args': [], 'returns': None, 'desc': 'Go forward to the next page in the history list. Does nothing if there is no next page.'}, {'name': 'GoHome', 'args': [], 'returns': None, 'desc': 'Loads the  page from the home URL.  This happens automatically when\nhome URL is changed.'}, {'name': 'GoToUrl', 'args': [{'name': 'url', 'type': 'str'}], 'returns': None, 'desc': 'Load the page at the given URL.'}, {'name': 'Reload', 'args': [], 'returns': None, 'desc': 'Reload the current page.'}, {'name': 'RunJavaScript', 'args': [{'name': 'js', 'type': 'str'}], 'returns': None, 'desc': 'Run JavaScript in the current page.'}, {'name': 'StopLoading', 'args': [], 'returns': None, 'desc': 'Stop loading a page.'}]}

    def __init__(self, /, *, parent: Component=..., FollowLinks: bool=..., Height: int=..., HomeUrl: str=..., IgnoreSslErrors: bool=..., PromptforPermission: bool=..., UsesLocation: bool=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def CurrentPageTitle(self) -> str:
        """Returns the title of the page currently being viewed"""
        raise NotImplementedError

    @property
    def CurrentUrl(self) -> str:
        """Returns the URL currently being viewed. This could be different from the HomeUrl
if new pages were visited by following links."""
        raise NotImplementedError

    @property
    def FollowLinks(self) -> bool:
        """Determines whether to follow links when they are tapped in the WebViewer. If you follow
links, you can use GoBack and GoForward to navigate the browser history."""
        raise NotImplementedError

    @FollowLinks.setter
    def FollowLinks(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the WebViewer's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the WebViewer's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HomeUrl(self) -> str:
        """Specifies the URL of the page the WebViewer should initially open to. Setting this will
load the page."""
        raise NotImplementedError

    @HomeUrl.setter
    def HomeUrl(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def IgnoreSslErrors(self) -> bool:
        """Determine whether or not to ignore SSL errors. Set to true to ignore errors.
Use this to accept self signed certificates from websites."""
        raise NotImplementedError

    @IgnoreSslErrors.setter
    def IgnoreSslErrors(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def PromptforPermission(self) -> bool:
        """Determine if the user should be prompted for permission to use the geolocation API while in
the WebViewer. If true, prompt the user of the WebViewer to give
permission to access the geolocation API. If false, assume permission is
granted."""
        raise NotImplementedError

    @PromptforPermission.setter
    def PromptforPermission(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the WebViewer should be visible on the screen.  Value is true
if the WebViewer is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def WebViewString(self) -> str:
        """Gets the WebView's String, which is viewable through Javascript in the WebView as the
window.AppInventor object."""
        raise NotImplementedError

    @WebViewString.setter
    def WebViewString(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the WebViewer, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the WebViewer as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def CanGoBack(self, /) -> bool:
        """Returns true if the WebViewer can go back in the history list."""
        raise NotImplementedError

    def CanGoForward(self, /) -> bool:
        """Returns true if the WebViewer can go forward in the history list."""
        raise NotImplementedError

    def ClearCaches(self, /) -> None:
        """Clear the internal webview cache, both ram and disk. This is useful
when using the WebViewer to poll a page that may not be sending
appropriate cache control headers."""
        raise NotImplementedError

    def ClearCookies(self, /) -> None:
        """Clear the webview's cookies. This is useful if you want to
sign the user out of a website that uses them to store logins."""
        raise NotImplementedError

    def ClearLocations(self, /) -> None:
        """Clear Stored Location permissions. When the geolocation API is used in
the WebViewer, the end user is prompted on a per URL basis for whether
or not permission should be granted to access their location. This
function clears this information for all locations.

   As the permissions interface is not available on phones older then
Eclair, this function is a no-op on older phones.
"""
        raise NotImplementedError

    def GoBack(self, /) -> None:
        """Go back to the previous page in the history list. Does nothing if there is no previous page."""
        raise NotImplementedError

    def GoForward(self, /) -> None:
        """Go forward to the next page in the history list. Does nothing if there is no next page."""
        raise NotImplementedError

    def GoHome(self, /) -> None:
        """Loads the  page from the home URL.  This happens automatically when
home URL is changed."""
        raise NotImplementedError

    def GoToUrl(self, url: str, /) -> None:
        """Load the page at the given URL."""
        raise NotImplementedError

    def Reload(self, /) -> None:
        """Reload the current page."""
        raise NotImplementedError

    def RunJavaScript(self, js: str, /) -> None:
        """Run JavaScript in the current page."""
        raise NotImplementedError

    def StopLoading(self, /) -> None:
        """Stop loading a page."""
        raise NotImplementedError

    def on_BeforePageLoad(self, callback: Callable[[str], None], /) -> None:
        """BeforePageLoad(url)

When a page is about to load this event is run."""
        raise NotImplementedError

    @staticmethod
    def on_any_BeforePageLoad(callback: Callable[['WebViewer', bool, str], None], /) -> None:
        """BeforePageLoad(url)

When a page is about to load this event is run."""
        raise NotImplementedError

    def on_ErrorOccurred(self, callback: Callable[[int, str, str], None], /) -> None:
        """ErrorOccurred(errorCode, description, failingUrl)

When an error occurs this event is run."""
        raise NotImplementedError

    @staticmethod
    def on_any_ErrorOccurred(callback: Callable[['WebViewer', bool, int, str, str], None], /) -> None:
        """ErrorOccurred(errorCode, description, failingUrl)

When an error occurs this event is run."""
        raise NotImplementedError

    def on_PageLoaded(self, callback: Callable[[str], None], /) -> None:
        """PageLoaded(url)

When a page is finished loading this event is run."""
        raise NotImplementedError

    @staticmethod
    def on_any_PageLoaded(callback: Callable[['WebViewer', bool, str], None], /) -> None:
        """PageLoaded(url)

When a page is finished loading this event is run."""
        raise NotImplementedError

    def on_WebViewStringChange(self, callback: Callable[[str], None], /) -> None:
        """WebViewStringChange(value)

Event that runs when the AppInventor.setWebViewString method is called from JavaScript.
The new WebViewString is given by the value parameter."""
        raise NotImplementedError

    @staticmethod
    def on_any_WebViewStringChange(callback: Callable[['WebViewer', bool, str], None], /) -> None:
        """WebViewStringChange(value)

Event that runs when the AppInventor.setWebViewString method is called from JavaScript.
The new WebViewString is given by the value parameter."""
        raise NotImplementedError

class HorizontalArrangement(Component):
    """Use a horizontal arrangement component to display a group of components laid out from left to
right."""
    __data__ = {'desc': 'Use a horizontal arrangement component to display a group of components laid out from left to\nright.', 'properties': [{'name': 'AlignHorizontal', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "A number that encodes how contents of the HorizontalArrangement are aligned horizontally. The choices\nare: 1 = left aligned, 2 = right aligned, 3 = horizontally centered. Alignment has no\neffect if the HorizontalArrangement's Width is Automatic."}, {'name': 'AlignVertical', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "A number that encodes how the contents of the HorizontalArrangement are aligned vertically. The choices\nare: 1 = aligned at the top, 2 = vertically centered, 3 = aligned at the bottom.\nAlignment has no effect if the HorizontalArrangement's Height is Automatic."}, {'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the background color of the HorizontalArrangement as an alpha-red-green-blue\ninteger.  If an Image has been set, the color change will not be visible\nuntil the Image is removed.'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the HorizontalArrangement's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the HorizontalArrangement's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Image', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the path of the background image of the HorizontalArrangement.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the HorizontalArrangement should be visible on the screen.  Value is true\nif the HorizontalArrangement is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the HorizontalArrangement, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the HorizontalArrangement as a percentage\nof the Screen's Width."}], 'events': [], 'methods': []}

    def __init__(self, /, *, parent: Component=..., AlignHorizontal: int=..., AlignVertical: int=..., BackgroundColor: enums.Color=..., Height: int=..., Image: str=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def AlignHorizontal(self) -> int:
        """A number that encodes how contents of the HorizontalArrangement are aligned horizontally. The choices
are: 1 = left aligned, 2 = right aligned, 3 = horizontally centered. Alignment has no
effect if the HorizontalArrangement's Width is Automatic."""
        raise NotImplementedError

    @AlignHorizontal.setter
    def AlignHorizontal(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def AlignVertical(self) -> int:
        """A number that encodes how the contents of the HorizontalArrangement are aligned vertically. The choices
are: 1 = aligned at the top, 2 = vertically centered, 3 = aligned at the bottom.
Alignment has no effect if the HorizontalArrangement's Height is Automatic."""
        raise NotImplementedError

    @AlignVertical.setter
    def AlignVertical(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the background color of the HorizontalArrangement as an alpha-red-green-blue
integer.  If an Image has been set, the color change will not be visible
until the Image is removed."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the HorizontalArrangement's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the HorizontalArrangement's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Image(self) -> str:
        """Specifies the path of the background image of the HorizontalArrangement."""
        raise NotImplementedError

    @Image.setter
    def Image(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the HorizontalArrangement should be visible on the screen.  Value is true
if the HorizontalArrangement is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the HorizontalArrangement, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the HorizontalArrangement as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

class HorizontalScrollArrangement(Component):
    """A formatting element in which to place components that should be displayed from left to right.
If you wish to have components displayed one over another, use VerticalScrollArrangement
instead."""
    __data__ = {'desc': 'A formatting element in which to place components that should be displayed from left to right.\nIf you wish to have components displayed one over another, use VerticalScrollArrangement\ninstead.', 'properties': [{'name': 'AlignHorizontal', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "A number that encodes how contents of the HorizontalScrollArrangement are aligned horizontally. The choices\nare: 1 = left aligned, 2 = right aligned, 3 = horizontally centered. Alignment has no\neffect if the HorizontalScrollArrangement's Width is Automatic."}, {'name': 'AlignVertical', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "A number that encodes how the contents of the HorizontalScrollArrangement are aligned vertically. The choices\nare: 1 = aligned at the top, 2 = vertically centered, 3 = aligned at the bottom.\nAlignment has no effect if the HorizontalScrollArrangement's Height is Automatic."}, {'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the background color of the HorizontalScrollArrangement as an alpha-red-green-blue\ninteger.  If an Image has been set, the color change will not be visible\nuntil the Image is removed.'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the HorizontalScrollArrangement's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the HorizontalScrollArrangement's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Image', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the path of the background image of the HorizontalScrollArrangement.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the HorizontalScrollArrangement should be visible on the screen.  Value is true\nif the HorizontalScrollArrangement is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the HorizontalScrollArrangement, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the HorizontalScrollArrangement as a percentage\nof the Screen's Width."}], 'events': [], 'methods': []}

    def __init__(self, /, *, parent: Component=..., AlignHorizontal: int=..., AlignVertical: int=..., BackgroundColor: enums.Color=..., Height: int=..., Image: str=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def AlignHorizontal(self) -> int:
        """A number that encodes how contents of the HorizontalScrollArrangement are aligned horizontally. The choices
are: 1 = left aligned, 2 = right aligned, 3 = horizontally centered. Alignment has no
effect if the HorizontalScrollArrangement's Width is Automatic."""
        raise NotImplementedError

    @AlignHorizontal.setter
    def AlignHorizontal(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def AlignVertical(self) -> int:
        """A number that encodes how the contents of the HorizontalScrollArrangement are aligned vertically. The choices
are: 1 = aligned at the top, 2 = vertically centered, 3 = aligned at the bottom.
Alignment has no effect if the HorizontalScrollArrangement's Height is Automatic."""
        raise NotImplementedError

    @AlignVertical.setter
    def AlignVertical(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the background color of the HorizontalScrollArrangement as an alpha-red-green-blue
integer.  If an Image has been set, the color change will not be visible
until the Image is removed."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the HorizontalScrollArrangement's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the HorizontalScrollArrangement's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Image(self) -> str:
        """Specifies the path of the background image of the HorizontalScrollArrangement."""
        raise NotImplementedError

    @Image.setter
    def Image(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the HorizontalScrollArrangement should be visible on the screen.  Value is true
if the HorizontalScrollArrangement is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the HorizontalScrollArrangement, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the HorizontalScrollArrangement as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

class TableArrangement(Component):
    """Use a table arrangement component to display a group of components in a tabular fashion."""
    __data__ = {'desc': 'Use a table arrangement component to display a group of components in a tabular fashion.', 'properties': [{'name': 'Columns', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': 'Determines the number of columns in the table.'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the TableArrangement's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the TableArrangement's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Rows', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': 'Determines the number of rows in the table.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the TableArrangement should be visible on the screen.  Value is true\nif the TableArrangement is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the TableArrangement, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the TableArrangement as a percentage\nof the Screen's Width."}], 'events': [], 'methods': []}

    def __init__(self, /, *, parent: Component=..., Columns: int=..., Height: int=..., Rows: int=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the TableArrangement's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the TableArrangement's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the TableArrangement should be visible on the screen.  Value is true
if the TableArrangement is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the TableArrangement, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the TableArrangement as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

class VerticalArrangement(Component):
    """Use a VerticalArrangement component to display a group of components laid out from top to
bottom, left-aligned."""
    __data__ = {'desc': 'Use a VerticalArrangement component to display a group of components laid out from top to\nbottom, left-aligned.', 'properties': [{'name': 'AlignHorizontal', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "A number that encodes how contents of the VerticalArrangement are aligned horizontally. The choices\nare: 1 = left aligned, 2 = right aligned, 3 = horizontally centered. Alignment has no\neffect if the VerticalArrangement's Width is Automatic."}, {'name': 'AlignVertical', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "A number that encodes how the contents of the VerticalArrangement are aligned vertically. The choices\nare: 1 = aligned at the top, 2 = vertically centered, 3 = aligned at the bottom.\nAlignment has no effect if the VerticalArrangement's Height is Automatic."}, {'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the background color of the VerticalArrangement as an alpha-red-green-blue\ninteger.  If an Image has been set, the color change will not be visible\nuntil the Image is removed.'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the VerticalArrangement's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the VerticalArrangement's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Image', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the path of the background image of the VerticalArrangement.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the VerticalArrangement should be visible on the screen.  Value is true\nif the VerticalArrangement is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the VerticalArrangement, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the VerticalArrangement as a percentage\nof the Screen's Width."}], 'events': [], 'methods': []}

    def __init__(self, /, *, parent: Component=..., AlignHorizontal: int=..., AlignVertical: int=..., BackgroundColor: enums.Color=..., Height: int=..., Image: str=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def AlignHorizontal(self) -> int:
        """A number that encodes how contents of the VerticalArrangement are aligned horizontally. The choices
are: 1 = left aligned, 2 = right aligned, 3 = horizontally centered. Alignment has no
effect if the VerticalArrangement's Width is Automatic."""
        raise NotImplementedError

    @AlignHorizontal.setter
    def AlignHorizontal(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def AlignVertical(self) -> int:
        """A number that encodes how the contents of the VerticalArrangement are aligned vertically. The choices
are: 1 = aligned at the top, 2 = vertically centered, 3 = aligned at the bottom.
Alignment has no effect if the VerticalArrangement's Height is Automatic."""
        raise NotImplementedError

    @AlignVertical.setter
    def AlignVertical(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the background color of the VerticalArrangement as an alpha-red-green-blue
integer.  If an Image has been set, the color change will not be visible
until the Image is removed."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the VerticalArrangement's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the VerticalArrangement's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Image(self) -> str:
        """Specifies the path of the background image of the VerticalArrangement."""
        raise NotImplementedError

    @Image.setter
    def Image(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the VerticalArrangement should be visible on the screen.  Value is true
if the VerticalArrangement is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the VerticalArrangement, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the VerticalArrangement as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

class VerticalScrollArrangement(Component):
    """A formatting element in which to place components that should be displayed one below another.
(The first child component is stored on top, the second beneath it, etc.) If you wish to have
components displayed next to one another, use HorizontalScrollArrangement instead."""
    __data__ = {'desc': 'A formatting element in which to place components that should be displayed one below another.\n(The first child component is stored on top, the second beneath it, etc.) If you wish to have\ncomponents displayed next to one another, use HorizontalScrollArrangement instead.', 'properties': [{'name': 'AlignHorizontal', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "A number that encodes how contents of the VerticalScrollArrangement are aligned horizontally. The choices\nare: 1 = left aligned, 2 = right aligned, 3 = horizontally centered. Alignment has no\neffect if the VerticalScrollArrangement's Width is Automatic."}, {'name': 'AlignVertical', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "A number that encodes how the contents of the VerticalScrollArrangement are aligned vertically. The choices\nare: 1 = aligned at the top, 2 = vertically centered, 3 = aligned at the bottom.\nAlignment has no effect if the VerticalScrollArrangement's Height is Automatic."}, {'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the background color of the VerticalScrollArrangement as an alpha-red-green-blue\ninteger.  If an Image has been set, the color change will not be visible\nuntil the Image is removed.'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the VerticalScrollArrangement's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the VerticalScrollArrangement's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Image', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the path of the background image of the VerticalScrollArrangement.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the VerticalScrollArrangement should be visible on the screen.  Value is true\nif the VerticalScrollArrangement is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the VerticalScrollArrangement, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the VerticalScrollArrangement as a percentage\nof the Screen's Width."}], 'events': [], 'methods': []}

    def __init__(self, /, *, parent: Component=..., AlignHorizontal: int=..., AlignVertical: int=..., BackgroundColor: enums.Color=..., Height: int=..., Image: str=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def AlignHorizontal(self) -> int:
        """A number that encodes how contents of the VerticalScrollArrangement are aligned horizontally. The choices
are: 1 = left aligned, 2 = right aligned, 3 = horizontally centered. Alignment has no
effect if the VerticalScrollArrangement's Width is Automatic."""
        raise NotImplementedError

    @AlignHorizontal.setter
    def AlignHorizontal(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def AlignVertical(self) -> int:
        """A number that encodes how the contents of the VerticalScrollArrangement are aligned vertically. The choices
are: 1 = aligned at the top, 2 = vertically centered, 3 = aligned at the bottom.
Alignment has no effect if the VerticalScrollArrangement's Height is Automatic."""
        raise NotImplementedError

    @AlignVertical.setter
    def AlignVertical(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the background color of the VerticalScrollArrangement as an alpha-red-green-blue
integer.  If an Image has been set, the color change will not be visible
until the Image is removed."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the VerticalScrollArrangement's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the VerticalScrollArrangement's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Image(self) -> str:
        """Specifies the path of the background image of the VerticalScrollArrangement."""
        raise NotImplementedError

    @Image.setter
    def Image(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the VerticalScrollArrangement should be visible on the screen.  Value is true
if the VerticalScrollArrangement is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the VerticalScrollArrangement, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the VerticalScrollArrangement as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

class Camcorder(Component):
    """A component to record a video using the device's camcorder. After the video is recorded, the
name of the file on the phone containing the clip is available as an argument to the
AfterRecording event. The file name can be used, for example, to set the source
property of a VideoPlayer component."""
    __data__ = {'desc': "A component to record a video using the device's camcorder. After the video is recorded, the\nname of the file on the phone containing the clip is available as an argument to the\nAfterRecording event. The file name can be used, for example, to set the source\nproperty of a VideoPlayer component.", 'properties': [], 'events': [{'name': 'AfterRecording', 'args': [{'name': 'clip', 'type': 'str'}], 'desc': 'Indicates that a video was recorded with the camera and provides the path to\nthe stored video.'}], 'methods': [{'name': 'RecordVideo', 'args': [], 'returns': None, 'desc': 'Records a video, then raises the AfterRecording event.'}]}

    def __init__(self, /, *, parent: Component=...):
        raise NotImplementedError

    def RecordVideo(self, /) -> None:
        """Records a video, then raises the AfterRecording event."""
        raise NotImplementedError

    def on_AfterRecording(self, callback: Callable[[str], None], /) -> None:
        """AfterRecording(clip)

Indicates that a video was recorded with the camera and provides the path to
the stored video."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterRecording(callback: Callable[['Camcorder', bool, str], None], /) -> None:
        """AfterRecording(clip)

Indicates that a video was recorded with the camera and provides the path to
the stored video."""
        raise NotImplementedError

class Camera(Component):
    """Use a camera component to take a picture on the phone."""
    __data__ = {'desc': 'Use a camera component to take a picture on the phone.', 'properties': [], 'events': [{'name': 'AfterPicture', 'args': [{'name': 'image', 'type': 'str'}], 'desc': 'Called after the picture is taken. The text argument image is the path that can be used to\nlocate the image on the phone.'}], 'methods': [{'name': 'TakePicture', 'args': [], 'returns': None, 'desc': 'Takes a picture, then raises the AfterPicture event.'}]}

    def __init__(self, /, *, parent: Component=...):
        raise NotImplementedError

    def TakePicture(self, /) -> None:
        """Takes a picture, then raises the AfterPicture event."""
        raise NotImplementedError

    def on_AfterPicture(self, callback: Callable[[str], None], /) -> None:
        """AfterPicture(image)

Called after the picture is taken. The text argument image is the path that can be used to
locate the image on the phone."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterPicture(callback: Callable[['Camera', bool, str], None], /) -> None:
        """AfterPicture(image)

Called after the picture is taken. The text argument image is the path that can be used to
locate the image on the phone."""
        raise NotImplementedError

class ImagePicker(Component):
    """A special-purpose button. When the user taps an ImagePicker, the device's image gallery
appears, and the user can choose an image. After an image is picked, it is saved, and the
Selection property will be the name of the file where the image is stored. In order
to not fill up storage, a maximum of 10 images will be stored. Picking more images will delete
previous images, in order from oldest to newest."""
    __data__ = {'desc': "A special-purpose button. When the user taps an ImagePicker, the device's image gallery\nappears, and the user can choose an image. After an image is picked, it is saved, and the\nSelection property will be the name of the file where the image is stored. In order\nto not fill up storage, a maximum of 10 images will be stored. Picking more images will delete\nprevious images, in order from oldest to newest.", 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the ImagePicker's background color as an alpha-red-green-blue\ninteger.  If an Image has been set, the color\nchange will not be visible until the Image is removed."}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the ImagePicker should be active and clickable.'}, {'name': 'FontBold', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the text of the ImagePicker should be bold.\nSome fonts do not support bold.'}, {'name': 'FontItalic', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the text of the ImagePicker should be italic.\nSome fonts do not support italic.'}, {'name': 'FontSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text font size of the ImagePicker, measured in sp(scale-independent pixels).'}, {'name': 'FontTypeface', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the text font face of the ImagePicker as default, serif, sans\nserif, monospace, or custom font typeface. To add a custom typeface,\nupload a .ttf file to the project's media."}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the ImagePicker's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the ImagePicker's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Image', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the path of the ImagePicker's image. If there is both an Image and a\nBackgroundColor specified, only the Image will be visible."}, {'name': 'Selection', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Path to the file containing the image that was selected.'}, {'name': 'Shape', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies the shape of the ImagePicker. The valid values for this property are 0 (default),\n1 (rounded), 2 (rectangle), and 3 (oval). The Shape will not be visible if an\nImage is used.'}, {'name': 'ShowFeedback', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies if a visual feedback should be shown when a ImagePicker with an assigned\nImage is pressed.'}, {'name': 'Text', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text displayed by the ImagePicker.'}, {'name': 'TextAlignment', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the alignment of the ImagePicker's text. Valid values are:\n0 (normal; e.g., left-justified if text is written left to right),\n1 (center), or\n2 (opposite; e.g., right-justified if text is written left to right)."}, {'name': 'TextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text color of the ImagePicker as an alpha-red-green-blue\ninteger.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the ImagePicker should be visible on the screen.  Value is true\nif the ImagePicker is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the ImagePicker, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the ImagePicker as a percentage\nof the Screen's Width."}], 'events': [{'name': 'AfterPicking', 'args': [], 'desc': 'Event to be raised after the ImagePicker activity returns its\nresult and the properties have been filled in.'}, {'name': 'BeforePicking', 'args': [], 'desc': 'Event to raise when the ImagePicker is clicked or the picker is shown\nusing the Open method.  This event occurs before the picker is displayed, and\ncan be used to prepare the picker before it is shown.'}, {'name': 'GotFocus', 'args': [], 'desc': 'Indicates the cursor moved over the ImagePicker so it is now possible\nto click it.'}, {'name': 'LostFocus', 'args': [], 'desc': 'Indicates the cursor moved away from the ImagePicker so it is now no\nlonger possible to click it.'}, {'name': 'TouchDown', 'args': [], 'desc': 'Indicates that the ImagePicker was pressed down.'}, {'name': 'TouchUp', 'args': [], 'desc': 'Indicates that the ImagePicker has been released.'}], 'methods': [{'name': 'Open', 'args': [], 'returns': None, 'desc': 'Opens the ImagePicker, as though the user clicked on it.'}]}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., Enabled: bool=..., FontBold: bool=..., FontItalic: bool=..., FontSize: int=..., FontTypeface: str=..., Height: int=..., Image: str=..., Shape: int=..., ShowFeedback: bool=..., Text: str=..., TextAlignment: int=..., TextColor: enums.Color=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the ImagePicker's background color as an alpha-red-green-blue
integer.  If an Image has been set, the color
change will not be visible until the Image is removed."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Specifies whether the ImagePicker should be active and clickable."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontBold(self) -> bool:
        """Specifies whether the text of the ImagePicker should be bold.
Some fonts do not support bold."""
        raise NotImplementedError

    @FontBold.setter
    def FontBold(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontItalic(self) -> bool:
        """Specifies whether the text of the ImagePicker should be italic.
Some fonts do not support italic."""
        raise NotImplementedError

    @FontItalic.setter
    def FontItalic(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontSize(self) -> int:
        """Specifies the text font size of the ImagePicker, measured in sp(scale-independent pixels)."""
        raise NotImplementedError

    @FontSize.setter
    def FontSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the ImagePicker's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the ImagePicker's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Image(self) -> str:
        """Specifies the path of the ImagePicker's image. If there is both an Image and a
BackgroundColor specified, only the Image will be visible."""
        raise NotImplementedError

    @Image.setter
    def Image(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Selection(self) -> str:
        """Path to the file containing the image that was selected."""
        raise NotImplementedError

    @property
    def ShowFeedback(self) -> bool:
        """Specifies if a visual feedback should be shown when a ImagePicker with an assigned
Image is pressed."""
        raise NotImplementedError

    @ShowFeedback.setter
    def ShowFeedback(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Text(self) -> str:
        """Specifies the text displayed by the ImagePicker."""
        raise NotImplementedError

    @Text.setter
    def Text(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def TextColor(self) -> enums.Color:
        """Specifies the text color of the ImagePicker as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @TextColor.setter
    def TextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the ImagePicker should be visible on the screen.  Value is true
if the ImagePicker is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the ImagePicker, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the ImagePicker as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def Open(self, /) -> None:
        """Opens the ImagePicker, as though the user clicked on it."""
        raise NotImplementedError

    def on_AfterPicking(self, callback: Callable[[], None], /) -> None:
        """AfterPicking()

Event to be raised after the ImagePicker activity returns its
result and the properties have been filled in."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterPicking(callback: Callable[['ImagePicker', bool], None], /) -> None:
        """AfterPicking()

Event to be raised after the ImagePicker activity returns its
result and the properties have been filled in."""
        raise NotImplementedError

    def on_BeforePicking(self, callback: Callable[[], None], /) -> None:
        """BeforePicking()

Event to raise when the ImagePicker is clicked or the picker is shown
using the Open method.  This event occurs before the picker is displayed, and
can be used to prepare the picker before it is shown."""
        raise NotImplementedError

    @staticmethod
    def on_any_BeforePicking(callback: Callable[['ImagePicker', bool], None], /) -> None:
        """BeforePicking()

Event to raise when the ImagePicker is clicked or the picker is shown
using the Open method.  This event occurs before the picker is displayed, and
can be used to prepare the picker before it is shown."""
        raise NotImplementedError

    def on_GotFocus(self, callback: Callable[[], None], /) -> None:
        """GotFocus()

Indicates the cursor moved over the ImagePicker so it is now possible
to click it."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotFocus(callback: Callable[['ImagePicker', bool], None], /) -> None:
        """GotFocus()

Indicates the cursor moved over the ImagePicker so it is now possible
to click it."""
        raise NotImplementedError

    def on_LostFocus(self, callback: Callable[[], None], /) -> None:
        """LostFocus()

Indicates the cursor moved away from the ImagePicker so it is now no
longer possible to click it."""
        raise NotImplementedError

    @staticmethod
    def on_any_LostFocus(callback: Callable[['ImagePicker', bool], None], /) -> None:
        """LostFocus()

Indicates the cursor moved away from the ImagePicker so it is now no
longer possible to click it."""
        raise NotImplementedError

    def on_TouchDown(self, callback: Callable[[], None], /) -> None:
        """TouchDown()

Indicates that the ImagePicker was pressed down."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchDown(callback: Callable[['ImagePicker', bool], None], /) -> None:
        """TouchDown()

Indicates that the ImagePicker was pressed down."""
        raise NotImplementedError

    def on_TouchUp(self, callback: Callable[[], None], /) -> None:
        """TouchUp()

Indicates that the ImagePicker has been released."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchUp(callback: Callable[['ImagePicker', bool], None], /) -> None:
        """TouchUp()

Indicates that the ImagePicker has been released."""
        raise NotImplementedError

class Player(Component):
    """Multimedia component that plays audio and controls phone vibration. The name of a multimedia
file is specified in the Source property, which can be set in the Designer or
in the Blocks Editor. The length of time for a vibration is specified in the Blocks Editor in
milliseconds (thousandths of a second)."""
    __data__ = {'desc': 'Multimedia component that plays audio and controls phone vibration. The name of a multimedia\nfile is specified in the Source property, which can be set in the Designer or\nin the Blocks Editor. The length of time for a vibration is specified in the Blocks Editor in\nmilliseconds (thousandths of a second).', 'properties': [{'name': 'IsPlaying', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Reports whether the media is playing.'}, {'name': 'Loop', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'If true, the Player will loop when it plays. Setting Loop while the player is playing will\naffect the current playing.'}, {'name': 'PlayOnlyInForeground', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'If true, the Player will pause playing when leaving the current screen; if false\n(default option), the Player continues playing whenever the current screen is displaying or\nnot.'}, {'name': 'Source', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Sets the audio source.'}, {'name': 'Volume', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Sets the volume property to a number between 0 and 100.'}], 'events': [{'name': 'Completed', 'args': [], 'desc': 'Indicates that the media has reached the end'}, {'name': 'OtherPlayerStarted', 'args': [], 'desc': 'This event is signaled when another player has started (and the current player is playing or\npaused, but not stopped).'}], 'methods': [{'name': 'Pause', 'args': [], 'returns': None, 'desc': 'Suspends playing the media if it is playing.'}, {'name': 'Start', 'args': [], 'returns': None, 'desc': 'Plays the media.  If it was previously paused, the playing is resumed.\nIf it was previously stopped, it starts from the beginning.'}, {'name': 'Stop', 'args': [], 'returns': None, 'desc': 'Stops playing the media and seeks to the beginning of the song.'}, {'name': 'Vibrate', 'args': [{'name': 'milliseconds', 'type': 'int'}], 'returns': None, 'desc': 'Vibrates for specified number of milliseconds.'}]}

    def __init__(self, /, *, parent: Component=..., Loop: bool=..., PlayOnlyInForeground: bool=..., Source: str=..., Volume: int=...):
        raise NotImplementedError

    @property
    def IsPlaying(self) -> bool:
        """Reports whether the media is playing."""
        raise NotImplementedError

    @property
    def Loop(self) -> bool:
        """If true, the Player will loop when it plays. Setting Loop while the player is playing will
affect the current playing."""
        raise NotImplementedError

    @Loop.setter
    def Loop(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def PlayOnlyInForeground(self) -> bool:
        """If true, the Player will pause playing when leaving the current screen; if false
(default option), the Player continues playing whenever the current screen is displaying or
not."""
        raise NotImplementedError

    @PlayOnlyInForeground.setter
    def PlayOnlyInForeground(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Source(self) -> str:
        """Sets the audio source."""
        raise NotImplementedError

    @Source.setter
    def Source(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Volume(self) -> int:
        """Sets the volume property to a number between 0 and 100."""
        raise NotImplementedError

    @Volume.setter
    def Volume(self, value: int, /) -> None:
        raise NotImplementedError

    def Pause(self, /) -> None:
        """Suspends playing the media if it is playing."""
        raise NotImplementedError

    def Start(self, /) -> None:
        """Plays the media.  If it was previously paused, the playing is resumed.
If it was previously stopped, it starts from the beginning."""
        raise NotImplementedError

    def Stop(self, /) -> None:
        """Stops playing the media and seeks to the beginning of the song."""
        raise NotImplementedError

    def Vibrate(self, milliseconds: int, /) -> None:
        """Vibrates for specified number of milliseconds."""
        raise NotImplementedError

    def on_Completed(self, callback: Callable[[], None], /) -> None:
        """Completed()

Indicates that the media has reached the end"""
        raise NotImplementedError

    @staticmethod
    def on_any_Completed(callback: Callable[['Player', bool], None], /) -> None:
        """Completed()

Indicates that the media has reached the end"""
        raise NotImplementedError

    def on_OtherPlayerStarted(self, callback: Callable[[], None], /) -> None:
        """OtherPlayerStarted()

This event is signaled when another player has started (and the current player is playing or
paused, but not stopped)."""
        raise NotImplementedError

    @staticmethod
    def on_any_OtherPlayerStarted(callback: Callable[['Player', bool], None], /) -> None:
        """OtherPlayerStarted()

This event is signaled when another player has started (and the current player is playing or
paused, but not stopped)."""
        raise NotImplementedError

class Sound(Component):
    """A multimedia component that plays sound files and optionally vibrates for the number of
milliseconds (thousandths of a second) specified in the Blocks Editor. The name of the sound
file to play can be specified either in the Designer or in the Blocks Editor."""
    __data__ = {'desc': 'A multimedia component that plays sound files and optionally vibrates for the number of\nmilliseconds (thousandths of a second) specified in the Blocks Editor. The name of the sound\nfile to play can be specified either in the Designer or in the Blocks Editor.', 'properties': [{'name': 'MinimumInterval', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the minimum interval required between calls to Play, in\nmilliseconds.\nOnce the sound starts playing, all further Play calls will be ignored\nuntil the interval has elapsed.'}, {'name': 'Source', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'The name of the sound file. Only certain formats are supported.\nSee http://developer.android.com/guide/appendix/media-formats.html.'}], 'events': [], 'methods': [{'name': 'Pause', 'args': [], 'returns': None, 'desc': 'Pauses playing the sound if it is being played.'}, {'name': 'Play', 'args': [], 'returns': None, 'desc': 'Plays the sound.'}, {'name': 'Resume', 'args': [], 'returns': None, 'desc': 'Resumes playing the sound after a pause.'}, {'name': 'Stop', 'args': [], 'returns': None, 'desc': 'Stops playing the sound if it is being played.'}, {'name': 'Vibrate', 'args': [{'name': 'millisecs', 'type': 'int'}], 'returns': None, 'desc': 'Vibrates for the specified number of milliseconds.'}]}

    def __init__(self, /, *, parent: Component=..., MinimumInterval: int=..., Source: str=...):
        raise NotImplementedError

    @property
    def MinimumInterval(self) -> int:
        """Specifies the minimum interval required between calls to Play, in
milliseconds.
Once the sound starts playing, all further Play calls will be ignored
until the interval has elapsed."""
        raise NotImplementedError

    @MinimumInterval.setter
    def MinimumInterval(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Source(self) -> str:
        """The name of the sound file. Only certain formats are supported.
See http://developer.android.com/guide/appendix/media-formats.html."""
        raise NotImplementedError

    @Source.setter
    def Source(self, value: str, /) -> None:
        raise NotImplementedError

    def Pause(self, /) -> None:
        """Pauses playing the sound if it is being played."""
        raise NotImplementedError

    def Play(self, /) -> None:
        """Plays the sound."""
        raise NotImplementedError

    def Resume(self, /) -> None:
        """Resumes playing the sound after a pause."""
        raise NotImplementedError

    def Stop(self, /) -> None:
        """Stops playing the sound if it is being played."""
        raise NotImplementedError

    def Vibrate(self, millisecs: int, /) -> None:
        """Vibrates for the specified number of milliseconds."""
        raise NotImplementedError

class SoundRecorder(Component):
    """Multimedia component that records audio."""
    __data__ = {'desc': 'Multimedia component that records audio.', 'properties': [{'name': 'SavedRecording', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the path to the file where the recording should be stored. If this property is the\nempty string, then starting a recording will create a file in an appropriate location. If the\nproperty is not the empty string, it should specify a complete path to a file in an existing\ndirectory, including a file name with the extension .3gp.'}], 'events': [{'name': 'AfterSoundRecorded', 'args': [{'name': 'sound', 'type': 'str'}], 'desc': 'Provides the location of the newly created sound.'}, {'name': 'StartedRecording', 'args': [], 'desc': 'Indicates that the recorder has started, and can be stopped.'}, {'name': 'StoppedRecording', 'args': [], 'desc': 'Indicates that the recorder has stopped, and can be started again.'}], 'methods': [{'name': 'Start', 'args': [], 'returns': None, 'desc': 'Starts recording.'}, {'name': 'Stop', 'args': [], 'returns': None, 'desc': 'Stops recording.'}]}

    def __init__(self, /, *, parent: Component=..., SavedRecording: str=...):
        raise NotImplementedError

    @property
    def SavedRecording(self) -> str:
        """Specifies the path to the file where the recording should be stored. If this property is the
empty string, then starting a recording will create a file in an appropriate location. If the
property is not the empty string, it should specify a complete path to a file in an existing
directory, including a file name with the extension .3gp."""
        raise NotImplementedError

    @SavedRecording.setter
    def SavedRecording(self, value: str, /) -> None:
        raise NotImplementedError

    def Start(self, /) -> None:
        """Starts recording."""
        raise NotImplementedError

    def Stop(self, /) -> None:
        """Stops recording."""
        raise NotImplementedError

    def on_AfterSoundRecorded(self, callback: Callable[[str], None], /) -> None:
        """AfterSoundRecorded(sound)

Provides the location of the newly created sound."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterSoundRecorded(callback: Callable[['SoundRecorder', bool, str], None], /) -> None:
        """AfterSoundRecorded(sound)

Provides the location of the newly created sound."""
        raise NotImplementedError

    def on_StartedRecording(self, callback: Callable[[], None], /) -> None:
        """StartedRecording()

Indicates that the recorder has started, and can be stopped."""
        raise NotImplementedError

    @staticmethod
    def on_any_StartedRecording(callback: Callable[['SoundRecorder', bool], None], /) -> None:
        """StartedRecording()

Indicates that the recorder has started, and can be stopped."""
        raise NotImplementedError

    def on_StoppedRecording(self, callback: Callable[[], None], /) -> None:
        """StoppedRecording()

Indicates that the recorder has stopped, and can be started again."""
        raise NotImplementedError

    @staticmethod
    def on_any_StoppedRecording(callback: Callable[['SoundRecorder', bool], None], /) -> None:
        """StoppedRecording()

Indicates that the recorder has stopped, and can be started again."""
        raise NotImplementedError

class SpeechRecognizer(Component):
    """Use a SpeechRecognizer component to listen to the user speaking and convert the spoken sound
into text using the device's speech recognition feature."""
    __data__ = {'desc': "Use a SpeechRecognizer component to listen to the user speaking and convert the spoken sound\ninto text using the device's speech recognition feature.", 'properties': [{'name': 'Language', 'type': 'str', 'ro': False, 'do': False, 'bo': True, 'desc': "Suggests the language to use for recognizing speech. An empty string (the default) will\nuse the system's default language.\n\n   Language is specified using a language tag\n  with an optional region suffix, such as en or es-MX. The set of supported languages will\n  vary by device.\n"}, {'name': 'Result', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the last text produced by the recognizer.'}, {'name': 'UseLegacy', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'If true, a separate dialog is used to recognize speech (the default). If false, speech is\nrecognized in the background and updates are received as it recognizes words.\nAfterGettingText may get several calls with partial set to true.\nOnce sufficient time has elapsed since the last utterance, or StopListening is called,\nthe last string will be returned with partial set to false to indicate that it is the\nfinal recognized string and no more data will be provided until recognition is again started. See\nAfterGettingText for more details on partial speech recognition.'}], 'events': [{'name': 'AfterGettingText', 'args': [{'name': 'result', 'type': 'str'}, {'name': 'partial', 'type': 'bool'}], 'desc': 'Simple event to raise after the SpeechRecognizer has recognized speech. If\nUseLegacy is true, then this event will only happen once\nat the very end of the recognition. If UseLegacy is false,\nthen this event will run multiple times as the SpeechRecognizer incrementally recognizes\nspeech. In this case, partial will be true until the recognized speech\nhas been finalized (e.g., the user has stopped speaking), in which case partial will be\nfalse.'}, {'name': 'BeforeGettingText', 'args': [], 'desc': 'Simple event to raise when the SpeechRecognizer is invoked but before its\nactivity is started.'}], 'methods': [{'name': 'GetText', 'args': [], 'returns': None, 'desc': 'Asks the user to speak, and converts the speech to text. Signals the\nAfterGettingText event when the result is available.'}, {'name': 'Stop', 'args': [], 'returns': None, 'desc': 'Function used to forcefully stop listening speech in cases where\nSpeechRecognizer cannot stop automatically.\nThis function works only when the UseLegacy property is\nset to false.'}]}

    def __init__(self, /, *, parent: Component=..., UseLegacy: bool=...):
        raise NotImplementedError

    @property
    def Language(self) -> str:
        """Suggests the language to use for recognizing speech. An empty string (the default) will
use the system's default language.

   Language is specified using a language tag
  with an optional region suffix, such as en or es-MX. The set of supported languages will
  vary by device.
"""
        raise NotImplementedError

    @Language.setter
    def Language(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Result(self) -> str:
        """Returns the last text produced by the recognizer."""
        raise NotImplementedError

    @property
    def UseLegacy(self) -> bool:
        """If true, a separate dialog is used to recognize speech (the default). If false, speech is
recognized in the background and updates are received as it recognizes words.
AfterGettingText may get several calls with partial set to true.
Once sufficient time has elapsed since the last utterance, or StopListening is called,
the last string will be returned with partial set to false to indicate that it is the
final recognized string and no more data will be provided until recognition is again started. See
AfterGettingText for more details on partial speech recognition."""
        raise NotImplementedError

    @UseLegacy.setter
    def UseLegacy(self, value: bool, /) -> None:
        raise NotImplementedError

    def GetText(self, /) -> None:
        """Asks the user to speak, and converts the speech to text. Signals the
AfterGettingText event when the result is available."""
        raise NotImplementedError

    def Stop(self, /) -> None:
        """Function used to forcefully stop listening speech in cases where
SpeechRecognizer cannot stop automatically.
This function works only when the UseLegacy property is
set to false."""
        raise NotImplementedError

    def on_AfterGettingText(self, callback: Callable[[str, bool], None], /) -> None:
        """AfterGettingText(result, partial)

Simple event to raise after the SpeechRecognizer has recognized speech. If
UseLegacy is true, then this event will only happen once
at the very end of the recognition. If UseLegacy is false,
then this event will run multiple times as the SpeechRecognizer incrementally recognizes
speech. In this case, partial will be true until the recognized speech
has been finalized (e.g., the user has stopped speaking), in which case partial will be
false."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterGettingText(callback: Callable[['SpeechRecognizer', bool, str, bool], None], /) -> None:
        """AfterGettingText(result, partial)

Simple event to raise after the SpeechRecognizer has recognized speech. If
UseLegacy is true, then this event will only happen once
at the very end of the recognition. If UseLegacy is false,
then this event will run multiple times as the SpeechRecognizer incrementally recognizes
speech. In this case, partial will be true until the recognized speech
has been finalized (e.g., the user has stopped speaking), in which case partial will be
false."""
        raise NotImplementedError

    def on_BeforeGettingText(self, callback: Callable[[], None], /) -> None:
        """BeforeGettingText()

Simple event to raise when the SpeechRecognizer is invoked but before its
activity is started."""
        raise NotImplementedError

    @staticmethod
    def on_any_BeforeGettingText(callback: Callable[['SpeechRecognizer', bool], None], /) -> None:
        """BeforeGettingText()

Simple event to raise when the SpeechRecognizer is invoked but before its
activity is started."""
        raise NotImplementedError

class TextToSpeech(Component):
    """The TextToSpeech component speaks a given text aloud. You can set the pitch
and the rate of speech."""
    __data__ = {'desc': 'The TextToSpeech component speaks a given text aloud. You can set the pitch\nand the rate of speech.', 'properties': [{'name': 'AvailableCountries', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': 'List of the country codes available on this device for use with TextToSpeech.  Check the Android developer documentation under supported languages to find the meanings of these abbreviations.'}, {'name': 'AvailableLanguages', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': 'List of the languages available on this device for use with TextToSpeech.  Check the Android developer documentation under supported languages to find the meanings of these abbreviations.'}, {'name': 'Country', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Country code to use for speech generation. This can affect the pronunciation. For example,\nBritish English (GBR) will sound different from US English (USA). Not every country code will\naffect every language.'}, {'name': 'Language', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Sets the language for TextToSpeech. This changes the way that words are pronounced, not the\nactual language that is spoken. For example, setting the language to French and speaking\nEnglish text will sound like someone speaking English with a French accent.'}, {'name': 'Pitch', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Sets the speech pitch for the TextToSpeech.\n\n   The values should be between 0 and 2 where lower values lower the tone of synthesized voice\nand greater values raise it.\nThe default value is 1.0 for normal pitch.\n'}, {'name': 'Result', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns true if the text was successfully converted to\nspeech, otherwise false.'}, {'name': 'SpeechRate', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Sets the SpeechRate for TextToSpeech.\n\n   The values should be between 0 and 2 where lower values slow down the pitch and greater\nvalues accelerate it.\nThe default value is 1.0 for normal speech rate.\n'}], 'events': [{'name': 'AfterSpeaking', 'args': [{'name': 'result', 'type': 'bool'}], 'desc': 'Event to raise after the message is spoken. The result will be\ntrue if the message is spoken successfully, otherwise it will be\nfalse.'}, {'name': 'BeforeSpeaking', 'args': [], 'desc': 'Event to raise when Speak is invoked, before the message is spoken.'}], 'methods': [{'name': 'Speak', 'args': [{'name': 'message', 'type': 'str'}], 'returns': None, 'desc': 'Speaks the given message.'}]}

    def __init__(self, /, *, parent: Component=..., Country: str=..., Language: str=..., Pitch: int=..., SpeechRate: int=...):
        raise NotImplementedError

    @property
    def AvailableCountries(self) -> list:
        """List of the country codes available on this device for use with TextToSpeech.  Check the Android developer documentation under supported languages to find the meanings of these abbreviations."""
        raise NotImplementedError

    @property
    def AvailableLanguages(self) -> list:
        """List of the languages available on this device for use with TextToSpeech.  Check the Android developer documentation under supported languages to find the meanings of these abbreviations."""
        raise NotImplementedError

    @property
    def Country(self) -> str:
        """Country code to use for speech generation. This can affect the pronunciation. For example,
British English (GBR) will sound different from US English (USA). Not every country code will
affect every language."""
        raise NotImplementedError

    @Country.setter
    def Country(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Language(self) -> str:
        """Sets the language for TextToSpeech. This changes the way that words are pronounced, not the
actual language that is spoken. For example, setting the language to French and speaking
English text will sound like someone speaking English with a French accent."""
        raise NotImplementedError

    @Language.setter
    def Language(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Pitch(self) -> int:
        """Sets the speech pitch for the TextToSpeech.

   The values should be between 0 and 2 where lower values lower the tone of synthesized voice
and greater values raise it.
The default value is 1.0 for normal pitch.
"""
        raise NotImplementedError

    @Pitch.setter
    def Pitch(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Result(self) -> bool:
        """Returns true if the text was successfully converted to
speech, otherwise false."""
        raise NotImplementedError

    @property
    def SpeechRate(self) -> int:
        """Sets the SpeechRate for TextToSpeech.

   The values should be between 0 and 2 where lower values slow down the pitch and greater
values accelerate it.
The default value is 1.0 for normal speech rate.
"""
        raise NotImplementedError

    @SpeechRate.setter
    def SpeechRate(self, value: int, /) -> None:
        raise NotImplementedError

    def Speak(self, message: str, /) -> None:
        """Speaks the given message."""
        raise NotImplementedError

    def on_AfterSpeaking(self, callback: Callable[[bool], None], /) -> None:
        """AfterSpeaking(result)

Event to raise after the message is spoken. The result will be
true if the message is spoken successfully, otherwise it will be
false."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterSpeaking(callback: Callable[['TextToSpeech', bool, bool], None], /) -> None:
        """AfterSpeaking(result)

Event to raise after the message is spoken. The result will be
true if the message is spoken successfully, otherwise it will be
false."""
        raise NotImplementedError

    def on_BeforeSpeaking(self, callback: Callable[[], None], /) -> None:
        """BeforeSpeaking()

Event to raise when Speak is invoked, before the message is spoken."""
        raise NotImplementedError

    @staticmethod
    def on_any_BeforeSpeaking(callback: Callable[['TextToSpeech', bool], None], /) -> None:
        """BeforeSpeaking()

Event to raise when Speak is invoked, before the message is spoken."""
        raise NotImplementedError

class Translator(Component):
    """Use this component to translate words and sentences between
different languages. This component needs Internet access, as it
will request translations from a server at MIT (which in turn will
request translations from a commercial translation service).
Specify the source and target language in the form source-target
using two letter language codes.  So "en-es" will translate from
English to Spanish while "es-ru" will translate from Spanish to
Russian. If you leave out the source language, the service will
attempt to detect the source language. So providing just "es" will
attempt to detect the source language and translate it to Spanish."""
    __data__ = {'desc': 'Use this component to translate words and sentences between\ndifferent languages. This component needs Internet access, as it\nwill request translations from a server at MIT (which in turn will\nrequest translations from a commercial translation service).\nSpecify the source and target language in the form source-target\nusing two letter language codes.  So "en-es" will translate from\nEnglish to Spanish while "es-ru" will translate from Spanish to\nRussian. If you leave out the source language, the service will\nattempt to detect the source language. So providing just "es" will\nattempt to detect the source language and translate it to Spanish.', 'properties': [{'name': 'ApiKey', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'The API Key to use. MIT App Inventor will automatically fill this\nvalue in. You should not need to change it.'}], 'events': [{'name': 'GotTranslation', 'args': [{'name': 'responseCode', 'type': 'str'}, {'name': 'translation', 'type': 'str'}], 'desc': 'Event indicating that a request has finished and has returned data (translation).'}], 'methods': [{'name': 'RequestTranslation', 'args': [{'name': 'languageToTranslateTo', 'type': 'str'}, {'name': 'textToTranslate', 'type': 'str'}], 'returns': None, 'desc': "By providing a target language to translate to (for instance, 'es' for Spanish, 'en' for\nEnglish, or 'ru' for Russian), and a word or sentence to translate, this method will request\na translation. Once the text is translated by the external\nservice, the event GotTranslation will be executed.\n\n   Note: Translator will attempt to detect the source language. You can also specify\nprepending it to the language translation, e.g., es-ru will specify Spanish to Russian\ntranslation.\n"}]}

    def __init__(self, /, *, parent: Component=..., ApiKey: str=...):
        raise NotImplementedError

    @property
    def ApiKey(self) -> str:
        """The API Key to use. MIT App Inventor will automatically fill this
value in. You should not need to change it."""
        raise NotImplementedError

    @ApiKey.setter
    def ApiKey(self, value: str, /) -> None:
        raise NotImplementedError

    def RequestTranslation(self, languageToTranslateTo: str, textToTranslate: str, /) -> None:
        """By providing a target language to translate to (for instance, 'es' for Spanish, 'en' for
English, or 'ru' for Russian), and a word or sentence to translate, this method will request
a translation. Once the text is translated by the external
service, the event GotTranslation will be executed.

   Note: Translator will attempt to detect the source language. You can also specify
prepending it to the language translation, e.g., es-ru will specify Spanish to Russian
translation.
"""
        raise NotImplementedError

    def on_GotTranslation(self, callback: Callable[[str, str], None], /) -> None:
        """GotTranslation(responseCode, translation)

Event indicating that a request has finished and has returned data (translation)."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotTranslation(callback: Callable[['Translator', bool, str, str], None], /) -> None:
        """GotTranslation(responseCode, translation)

Event indicating that a request has finished and has returned data (translation)."""
        raise NotImplementedError

class VideoPlayer(Component):
    """A multimedia component capable of playing videos. When the application is run, the VideoPlayer
will be displayed as a rectangle on-screen. If the user touches the rectangle, controls will
appear to play/pause, skip ahead, and skip backward within the video. The application can also
control behavior by calling the Start, Pause, and SeekTo
methods."""
    __data__ = {'desc': 'A multimedia component capable of playing videos. When the application is run, the VideoPlayer\nwill be displayed as a rectangle on-screen. If the user touches the rectangle, controls will\nappear to play/pause, skip ahead, and skip backward within the video. The application can also\ncontrol behavior by calling the Start, Pause, and SeekTo\nmethods.', 'properties': [{'name': 'FullScreen', 'type': 'bool', 'ro': False, 'do': False, 'bo': True, 'desc': 'Sets whether the video should be shown in fullscreen or not.'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the component's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the VideoPlayer's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Source', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Sets the "path" to the video. Usually, this will be the name of the video file, which should be\nadded in the Designer.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the VideoPlayer should be visible on the screen.  Value is true\nif the VideoPlayer is showing and false if hidden.'}, {'name': 'Volume', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Sets the volume property to a number between 0 and 100. Values less than 0\nwill be treated as 0, and values greater than 100 will be treated as 100.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the component's horizontal width, measured in pixels."}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the VideoPlayer as a percentage\nof the Screen's Width."}], 'events': [{'name': 'Completed', 'args': [], 'desc': 'Indicates that the video has reached the end'}], 'methods': [{'name': 'GetDuration', 'args': [], 'returns': 'int', 'desc': 'Returns duration of the video in milliseconds.'}, {'name': 'Pause', 'args': [], 'returns': None, 'desc': 'Pauses playback of the video.  Playback can be resumed at the same location by calling the\nStart method.'}, {'name': 'SeekTo', 'args': [{'name': 'ms', 'type': 'int'}], 'returns': None, 'desc': 'Seeks to the requested time (specified in milliseconds) in the video. If the video is paused, the frame shown will not be updated by the seek. The player can jump only to key frames in the video, so seeking to times that differ by short intervals may not actually move to different frames.'}, {'name': 'Start', 'args': [], 'returns': None, 'desc': 'Plays the media specified by the Source.'}, {'name': 'Stop', 'args': [], 'returns': None, 'desc': 'Resets to start of video and pauses it if video was playing.'}]}

    def __init__(self, /, *, parent: Component=..., Height: int=..., Source: str=..., Visible: bool=..., Volume: int=..., Width: int=...):
        raise NotImplementedError

    @property
    def FullScreen(self) -> bool:
        """Sets whether the video should be shown in fullscreen or not."""
        raise NotImplementedError

    @FullScreen.setter
    def FullScreen(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the component's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the VideoPlayer's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Source(self) -> str:
        """Sets the "path" to the video. Usually, this will be the name of the video file, which should be
added in the Designer."""
        raise NotImplementedError

    @Source.setter
    def Source(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the VideoPlayer should be visible on the screen.  Value is true
if the VideoPlayer is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Volume(self) -> int:
        """Sets the volume property to a number between 0 and 100. Values less than 0
will be treated as 0, and values greater than 100 will be treated as 100."""
        raise NotImplementedError

    @Volume.setter
    def Volume(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the component's horizontal width, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the VideoPlayer as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def GetDuration(self, /) -> int:
        """Returns duration of the video in milliseconds."""
        raise NotImplementedError

    def Pause(self, /) -> None:
        """Pauses playback of the video.  Playback can be resumed at the same location by calling the
Start method."""
        raise NotImplementedError

    def SeekTo(self, ms: int, /) -> None:
        """Seeks to the requested time (specified in milliseconds) in the video. If the video is paused, the frame shown will not be updated by the seek. The player can jump only to key frames in the video, so seeking to times that differ by short intervals may not actually move to different frames."""
        raise NotImplementedError

    def Start(self, /) -> None:
        """Plays the media specified by the Source."""
        raise NotImplementedError

    def Stop(self, /) -> None:
        """Resets to start of video and pauses it if video was playing."""
        raise NotImplementedError

    def on_Completed(self, callback: Callable[[], None], /) -> None:
        """Completed()

Indicates that the video has reached the end"""
        raise NotImplementedError

    @staticmethod
    def on_any_Completed(callback: Callable[['VideoPlayer', bool], None], /) -> None:
        """Completed()

Indicates that the video has reached the end"""
        raise NotImplementedError

class Ball(Component):
    """A round 'sprite' that can be placed on a Canvas, where it can react to touches and drags,
interact with other sprites (ImageSprites and other Balls) and the edge of the
Canvas, and move according to its property values."""
    __data__ = {'desc': "A round 'sprite' that can be placed on a Canvas, where it can react to touches and drags,\ninteract with other sprites (ImageSprites and other Balls) and the edge of the\nCanvas, and move according to its property values.", 'properties': [{'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Controls whether the Ball moves when its speed is non-zero.'}, {'name': 'Heading', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "The Ball's heading in degrees above the positive x-axis. Zero degrees is toward the right\nof the screen; 90 degrees is toward the top of the screen."}, {'name': 'Interval', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "The interval in milliseconds at which the Ball's position is updated. For example, if the\nInterval is 50 and the Speed is 10, then the Ball will move 10 pixels\nevery 50 milliseconds."}, {'name': 'OriginAtCenter', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'Whether the x- and y-coordinates should represent the center of the Ball\n(true) or its left and top edges (false).'}, {'name': 'PaintColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'The color of the Ball.'}, {'name': 'Radius', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'The distance from the center of the Ball to its edge.'}, {'name': 'Speed', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'The speed at which the Ball moves. The Ball moves this many pixels every\nInterval milliseconds if Enabled is true.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Sets whether sprite should be visible.'}, {'name': 'X', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'The horizontal coordinate of the Ball, increasing as the Ball moves right. If the property\nOriginAtCenter is true, the coordinate is for the center of the Ball;\notherwise, it is for the leftmost point of the Ball.'}, {'name': 'Y', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'The vertical coordinate of the Ball, increasing as the Ball moves down. If the property\nOriginAtCenter is true, the coordinate is for the center of the Ball\notherwise, it is for the uppermost point of the Ball.'}, {'name': 'Z', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'How the Ball should be layered relative to other Balls and ImageSprites, with higher-numbered layers in front of lower-numbered layers.'}], 'events': [{'name': 'CollidedWith', 'args': [{'name': 'other', 'type': 'Component'}], 'desc': 'Event handler called when two enabled sprites (Balls or ImageSprites)\ncollide. Note that checking for collisions with a rotated ImageSprite currently\nchecks against its unrotated position. Therefore, collision\nchecking will be inaccurate for tall narrow or short wide sprites that are\nrotated.'}, {'name': 'Dragged', 'args': [{'name': 'startX', 'type': 'int'}, {'name': 'startY', 'type': 'int'}, {'name': 'prevX', 'type': 'int'}, {'name': 'prevY', 'type': 'int'}, {'name': 'currentX', 'type': 'int'}, {'name': 'currentY', 'type': 'int'}], 'desc': 'Event handler for Dragged events.  On all calls, the starting coordinates\nare where the screen was first touched, and the "current" coordinates\ndescribe the endpoint of the current line segment.  On the first call\nwithin a given drag, the "previous" coordinates are the same as the\nstarting coordinates; subsequently, they are the "current" coordinates\nfrom the prior call. Note that the Ball won\'t actually move\nanywhere in response to the Dragged event unless\nMoveTo is specifically called.'}, {'name': 'EdgeReached', 'args': [{'name': 'edge', 'type': 'int'}], 'desc': 'Event handler called when the Ball reaches an edge of the screen.\nIf Bounce is then called with that edge, the sprite will appear to bounce off\nof the edge it reached. Edge here is represented as an integer that indicates one of eight\ndirections north(1), northeast(2), east(3), southeast(4), south (-1), southwest(-2), west(-3),\nand northwest(-4).'}, {'name': 'Flung', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}, {'name': 'speed', 'type': 'int'}, {'name': 'heading', 'type': 'int'}, {'name': 'xvel', 'type': 'int'}, {'name': 'yvel', 'type': 'int'}], 'desc': "When a fling gesture (quick swipe) is made on the sprite: provides\nthe (x,y) position of the start of the fling, relative to the upper\nleft of the canvas. Also provides the speed (pixels per millisecond) and heading\n(-180 to 180 degrees) of the fling, as well as the x velocity and y velocity\ncomponents of the fling's vector."}, {'name': 'NoLongerCollidingWith', 'args': [{'name': 'other', 'type': 'Component'}], 'desc': 'Event indicating that a pair of sprites are no longer colliding.'}, {'name': 'TouchDown', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'desc': 'When the user begins touching the sprite (places finger on sprite and\nleaves it there): provides the (x,y) position of the touch, relative\nto the upper left of the canvas'}, {'name': 'TouchUp', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'desc': 'When the user stops touching the sprite (lifts finger after a\nTouchDown event): provides the (x,y) position of the touch, relative\nto the upper left of the canvas.'}, {'name': 'Touched', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'desc': 'When the user touches the sprite and then immediately lifts finger: provides\nthe (x,y) position of the touch, relative to the upper left of the canvas.'}], 'methods': [{'name': 'Bounce', 'args': [{'name': 'edge', 'type': 'int'}], 'returns': None, 'desc': 'Makes this Ball bounce, as if off a wall. For normal bouncing, the edge argument should\nbe the one returned by EdgeReached.'}, {'name': 'CollidingWith', 'args': [{'name': 'other', 'type': 'Component'}], 'returns': 'bool', 'desc': 'Indicates whether a collision has been registered between this Ball\nand the passed other sprite.'}, {'name': 'MoveIntoBounds', 'args': [], 'returns': None, 'desc': 'Moves the sprite back in bounds if part of it extends out of bounds,\nhaving no effect otherwise. If the sprite is too wide to fit on the\ncanvas, this aligns the left side of the sprite with the left side of the\ncanvas. If the sprite is too tall to fit on the canvas, this aligns the\ntop side of the sprite with the top side of the canvas.'}, {'name': 'MoveTo', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'returns': None, 'desc': 'Sets the x and y coordinates of the Ball. If OriginAtCenter is true,\nthe center of the Ball will be placed here. Otherwise, the top left edge of the Ball will\nbe placed at the specified coordinates.'}, {'name': 'MoveToPoint', 'args': [{'name': 'coordinates', 'type': 'list'}], 'returns': None, 'desc': 'Moves the Ball so that its origin is at the specified x and y coordinates.'}, {'name': 'PointInDirection', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'returns': None, 'desc': 'Turns this Ball to point toward the point with the coordinates (x, y).'}, {'name': 'PointTowards', 'args': [{'name': 'target', 'type': 'Component'}], 'returns': None, 'desc': 'Turns this Ball to point towards a given target sprite. The new heading will be parallel\nto the line joining the centerpoints of the two sprites.'}]}

    def __init__(self, /, *, parent: Component=..., Enabled: bool=..., Heading: int=..., Interval: int=..., OriginAtCenter: bool=..., PaintColor: enums.Color=..., Radius: int=..., Speed: int=..., Visible: bool=..., X: int=..., Y: int=..., Z: int=...):
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Controls whether the Ball moves when its speed is non-zero."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Heading(self) -> int:
        """The Ball's heading in degrees above the positive x-axis. Zero degrees is toward the right
of the screen; 90 degrees is toward the top of the screen."""
        raise NotImplementedError

    @Heading.setter
    def Heading(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Interval(self) -> int:
        """The interval in milliseconds at which the Ball's position is updated. For example, if the
Interval is 50 and the Speed is 10, then the Ball will move 10 pixels
every 50 milliseconds."""
        raise NotImplementedError

    @Interval.setter
    def Interval(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def PaintColor(self) -> enums.Color:
        """The color of the Ball."""
        raise NotImplementedError

    @PaintColor.setter
    def PaintColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Radius(self) -> int:
        """The distance from the center of the Ball to its edge."""
        raise NotImplementedError

    @Radius.setter
    def Radius(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Speed(self) -> int:
        """The speed at which the Ball moves. The Ball moves this many pixels every
Interval milliseconds if Enabled is true."""
        raise NotImplementedError

    @Speed.setter
    def Speed(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Sets whether sprite should be visible."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def X(self) -> int:
        """The horizontal coordinate of the Ball, increasing as the Ball moves right. If the property
OriginAtCenter is true, the coordinate is for the center of the Ball;
otherwise, it is for the leftmost point of the Ball."""
        raise NotImplementedError

    @X.setter
    def X(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Y(self) -> int:
        """The vertical coordinate of the Ball, increasing as the Ball moves down. If the property
OriginAtCenter is true, the coordinate is for the center of the Ball
otherwise, it is for the uppermost point of the Ball."""
        raise NotImplementedError

    @Y.setter
    def Y(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Z(self) -> int:
        """How the Ball should be layered relative to other Balls and ImageSprites, with higher-numbered layers in front of lower-numbered layers."""
        raise NotImplementedError

    @Z.setter
    def Z(self, value: int, /) -> None:
        raise NotImplementedError

    def Bounce(self, edge: int, /) -> None:
        """Makes this Ball bounce, as if off a wall. For normal bouncing, the edge argument should
be the one returned by EdgeReached."""
        raise NotImplementedError

    def CollidingWith(self, other: Component, /) -> bool:
        """Indicates whether a collision has been registered between this Ball
and the passed other sprite."""
        raise NotImplementedError

    def MoveIntoBounds(self, /) -> None:
        """Moves the sprite back in bounds if part of it extends out of bounds,
having no effect otherwise. If the sprite is too wide to fit on the
canvas, this aligns the left side of the sprite with the left side of the
canvas. If the sprite is too tall to fit on the canvas, this aligns the
top side of the sprite with the top side of the canvas."""
        raise NotImplementedError

    def MoveTo(self, x: int, y: int, /) -> None:
        """Sets the x and y coordinates of the Ball. If OriginAtCenter is true,
the center of the Ball will be placed here. Otherwise, the top left edge of the Ball will
be placed at the specified coordinates."""
        raise NotImplementedError

    def MoveToPoint(self, coordinates: list, /) -> None:
        """Moves the Ball so that its origin is at the specified x and y coordinates."""
        raise NotImplementedError

    def PointInDirection(self, x: int, y: int, /) -> None:
        """Turns this Ball to point toward the point with the coordinates (x, y)."""
        raise NotImplementedError

    def PointTowards(self, target: Component, /) -> None:
        """Turns this Ball to point towards a given target sprite. The new heading will be parallel
to the line joining the centerpoints of the two sprites."""
        raise NotImplementedError

    def on_CollidedWith(self, callback: Callable[[Component], None], /) -> None:
        """CollidedWith(other)

Event handler called when two enabled sprites (Balls or ImageSprites)
collide. Note that checking for collisions with a rotated ImageSprite currently
checks against its unrotated position. Therefore, collision
checking will be inaccurate for tall narrow or short wide sprites that are
rotated."""
        raise NotImplementedError

    @staticmethod
    def on_any_CollidedWith(callback: Callable[['Ball', bool, Component], None], /) -> None:
        """CollidedWith(other)

Event handler called when two enabled sprites (Balls or ImageSprites)
collide. Note that checking for collisions with a rotated ImageSprite currently
checks against its unrotated position. Therefore, collision
checking will be inaccurate for tall narrow or short wide sprites that are
rotated."""
        raise NotImplementedError

    def on_Dragged(self, callback: Callable[[int, int, int, int, int, int], None], /) -> None:
        """Dragged(startX, startY, prevX, prevY, currentX, currentY)

Event handler for Dragged events.  On all calls, the starting coordinates
are where the screen was first touched, and the "current" coordinates
describe the endpoint of the current line segment.  On the first call
within a given drag, the "previous" coordinates are the same as the
starting coordinates; subsequently, they are the "current" coordinates
from the prior call. Note that the Ball won't actually move
anywhere in response to the Dragged event unless
MoveTo is specifically called."""
        raise NotImplementedError

    @staticmethod
    def on_any_Dragged(callback: Callable[['Ball', bool, int, int, int, int, int, int], None], /) -> None:
        """Dragged(startX, startY, prevX, prevY, currentX, currentY)

Event handler for Dragged events.  On all calls, the starting coordinates
are where the screen was first touched, and the "current" coordinates
describe the endpoint of the current line segment.  On the first call
within a given drag, the "previous" coordinates are the same as the
starting coordinates; subsequently, they are the "current" coordinates
from the prior call. Note that the Ball won't actually move
anywhere in response to the Dragged event unless
MoveTo is specifically called."""
        raise NotImplementedError

    def on_EdgeReached(self, callback: Callable[[int], None], /) -> None:
        """EdgeReached(edge)

Event handler called when the Ball reaches an edge of the screen.
If Bounce is then called with that edge, the sprite will appear to bounce off
of the edge it reached. Edge here is represented as an integer that indicates one of eight
directions north(1), northeast(2), east(3), southeast(4), south (-1), southwest(-2), west(-3),
and northwest(-4)."""
        raise NotImplementedError

    @staticmethod
    def on_any_EdgeReached(callback: Callable[['Ball', bool, int], None], /) -> None:
        """EdgeReached(edge)

Event handler called when the Ball reaches an edge of the screen.
If Bounce is then called with that edge, the sprite will appear to bounce off
of the edge it reached. Edge here is represented as an integer that indicates one of eight
directions north(1), northeast(2), east(3), southeast(4), south (-1), southwest(-2), west(-3),
and northwest(-4)."""
        raise NotImplementedError

    def on_Flung(self, callback: Callable[[int, int, int, int, int, int], None], /) -> None:
        """Flung(x, y, speed, heading, xvel, yvel)

When a fling gesture (quick swipe) is made on the sprite: provides
the (x,y) position of the start of the fling, relative to the upper
left of the canvas. Also provides the speed (pixels per millisecond) and heading
(-180 to 180 degrees) of the fling, as well as the x velocity and y velocity
components of the fling's vector."""
        raise NotImplementedError

    @staticmethod
    def on_any_Flung(callback: Callable[['Ball', bool, int, int, int, int, int, int], None], /) -> None:
        """Flung(x, y, speed, heading, xvel, yvel)

When a fling gesture (quick swipe) is made on the sprite: provides
the (x,y) position of the start of the fling, relative to the upper
left of the canvas. Also provides the speed (pixels per millisecond) and heading
(-180 to 180 degrees) of the fling, as well as the x velocity and y velocity
components of the fling's vector."""
        raise NotImplementedError

    def on_NoLongerCollidingWith(self, callback: Callable[[Component], None], /) -> None:
        """NoLongerCollidingWith(other)

Event indicating that a pair of sprites are no longer colliding."""
        raise NotImplementedError

    @staticmethod
    def on_any_NoLongerCollidingWith(callback: Callable[['Ball', bool, Component], None], /) -> None:
        """NoLongerCollidingWith(other)

Event indicating that a pair of sprites are no longer colliding."""
        raise NotImplementedError

    def on_TouchDown(self, callback: Callable[[int, int], None], /) -> None:
        """TouchDown(x, y)

When the user begins touching the sprite (places finger on sprite and
leaves it there): provides the (x,y) position of the touch, relative
to the upper left of the canvas"""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchDown(callback: Callable[['Ball', bool, int, int], None], /) -> None:
        """TouchDown(x, y)

When the user begins touching the sprite (places finger on sprite and
leaves it there): provides the (x,y) position of the touch, relative
to the upper left of the canvas"""
        raise NotImplementedError

    def on_TouchUp(self, callback: Callable[[int, int], None], /) -> None:
        """TouchUp(x, y)

When the user stops touching the sprite (lifts finger after a
TouchDown event): provides the (x,y) position of the touch, relative
to the upper left of the canvas."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchUp(callback: Callable[['Ball', bool, int, int], None], /) -> None:
        """TouchUp(x, y)

When the user stops touching the sprite (lifts finger after a
TouchDown event): provides the (x,y) position of the touch, relative
to the upper left of the canvas."""
        raise NotImplementedError

    def on_Touched(self, callback: Callable[[int, int], None], /) -> None:
        """Touched(x, y)

When the user touches the sprite and then immediately lifts finger: provides
the (x,y) position of the touch, relative to the upper left of the canvas."""
        raise NotImplementedError

    @staticmethod
    def on_any_Touched(callback: Callable[['Ball', bool, int, int], None], /) -> None:
        """Touched(x, y)

When the user touches the sprite and then immediately lifts finger: provides
the (x,y) position of the touch, relative to the upper left of the canvas."""
        raise NotImplementedError

class Canvas(Component):
    """A two-dimensional touch-sensitive rectangular panel on which drawing can
be done and sprites can be moved."""
    __data__ = {'desc': 'A two-dimensional touch-sensitive rectangular panel on which drawing can\nbe done and sprites can be moved.', 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the Canvas's background color as an alpha-red-green-blue\ninteger, i.e., 0xAARRGGBB.  An alpha of 00\nindicates fully transparent and FF means opaque.\nThe background color only shows if there is no background image."}, {'name': 'BackgroundImage', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the name of a file containing the background image for the Canvas.'}, {'name': 'BackgroundImageinBase64', 'type': 'str', 'ro': False, 'do': False, 'bo': True, 'desc': 'Set the background image in Base64 format. This requires API level >= 8. For devices with API level less than 8, setting this will end up with an empty background.'}, {'name': 'ExtendMovesOutsideCanvas', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Determines whether moves can extend beyond the canvas borders.   Default is false. This should normally be false, and the property is provided for backwards compatibility.'}, {'name': 'FontSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the font size of text drawn on the Canvas.'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the Canvas's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the Canvas's vertical height as a percentage\nof the Screen's Height."}, {'name': 'LineWidth', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the width of lines drawn on the Canvas.'}, {'name': 'PaintColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the paint color as an alpha-red-green-blue integer,\ni.e., 0xAARRGGBB.  An alpha of 00 indicates fully\ntransparent and FF means opaque.'}, {'name': 'TapThreshold', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the movement threshold to differentiate a drag from a tap.'}, {'name': 'TextAlignment', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the alignment of the canvas's text: center, normal\n(starting at the specified point in DrawText or\nDrawTextAtAngle),\nor opposite (ending at the specified point in\nDrawText or\nDrawTextAtAngle)."}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the Canvas should be visible on the screen.  Value is true\nif the Canvas is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the Canvas, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the Canvas as a percentage\nof the Screen's Width."}], 'events': [{'name': 'Dragged', 'args': [{'name': 'startX', 'type': 'int'}, {'name': 'startY', 'type': 'int'}, {'name': 'prevX', 'type': 'int'}, {'name': 'prevY', 'type': 'int'}, {'name': 'currentX', 'type': 'int'}, {'name': 'currentY', 'type': 'int'}, {'name': 'draggedAnySprite', 'type': 'bool'}], 'desc': 'When the user does a drag from one point (prevX, prevY) to\nanother (x, y).  The pair (startX, startY) indicates where the\nuser first touched the screen, and "draggedAnySprite" indicates whether a\nsprite is being dragged.'}, {'name': 'Flung', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}, {'name': 'speed', 'type': 'int'}, {'name': 'heading', 'type': 'int'}, {'name': 'xvel', 'type': 'int'}, {'name': 'yvel', 'type': 'int'}, {'name': 'flungSprite', 'type': 'bool'}], 'desc': 'When a fling gesture (quick swipe) is made on the canvas: provides\nthe (x,y) position of the start of the fling, relative to the upper\nleft of the canvas. Also provides the speed (pixels per millisecond) and heading\n(-180 to 180 degrees) of the fling, as well as the x velocity and y velocity\ncomponents of the fling\'s vector. The value "flungSprite" is true if a sprite\nwas located near the the starting point of the fling gesture.'}, {'name': 'TouchDown', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'desc': 'When the user begins touching the canvas (places finger on canvas and\nleaves it there): provides the (x,y) position of the touch, relative\nto the upper left of the canvas'}, {'name': 'TouchUp', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'desc': 'When the user stops touching the canvas (lifts finger after a\nTouchDown event): provides the (x,y) position of the touch, relative\nto the upper left of the canvas'}, {'name': 'Touched', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}, {'name': 'touchedAnySprite', 'type': 'bool'}], 'desc': 'When the user touches the canvas and then immediately lifts finger: provides\nthe (x,y) position of the touch, relative to the upper left of the canvas.  TouchedAnySprite\nis true if the same touch also touched a sprite, and false otherwise.'}], 'methods': [{'name': 'Clear', 'args': [], 'returns': None, 'desc': 'Clears the canvas, without removing the background image, if one\nwas provided.'}, {'name': 'DrawArc', 'args': [{'name': 'left', 'type': 'int'}, {'name': 'top', 'type': 'int'}, {'name': 'right', 'type': 'int'}, {'name': 'bottom', 'type': 'int'}, {'name': 'startAngle', 'type': 'int'}, {'name': 'sweepAngle', 'type': 'int'}, {'name': 'useCenter', 'type': 'bool'}, {'name': 'fill', 'type': 'bool'}], 'returns': None, 'desc': 'Draw an arc on Canvas, by drawing an arc from a specified oval (specified by left, top, right & bottom).\nStart angle is 0 when heading to the right, and increase when rotate clockwise.\nWhen useCenter is true, a sector will be drawed instead of an arc.\nWhen fill is true, a filled arc (or sector) will be drawed instead of just an outline.'}, {'name': 'DrawCircle', 'args': [{'name': 'centerX', 'type': 'int'}, {'name': 'centerY', 'type': 'int'}, {'name': 'radius', 'type': 'int'}, {'name': 'fill', 'type': 'bool'}], 'returns': None, 'desc': 'Draws a circle (filled in) with the given radius centered at the given coordinates on the\nCanvas.'}, {'name': 'DrawLine', 'args': [{'name': 'x1', 'type': 'int'}, {'name': 'y1', 'type': 'int'}, {'name': 'x2', 'type': 'int'}, {'name': 'y2', 'type': 'int'}], 'returns': None, 'desc': 'Draws a line between the given coordinates on the canvas.'}, {'name': 'DrawPoint', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'returns': None, 'desc': 'Draws a point at the given coordinates on the canvas.'}, {'name': 'DrawShape', 'args': [{'name': 'pointList', 'type': 'list'}, {'name': 'fill', 'type': 'bool'}], 'returns': None, 'desc': 'Draws a shape on the canvas.\npointList should be a list contains sub-lists with two number which represents a coordinate.\nThe first point and last point does not need to be the same. e.g. ((x1 y1) (x2 y2) (x3 y3))\nWhen fill is true, the shape will be filled.'}, {'name': 'DrawText', 'args': [{'name': 'text', 'type': 'str'}, {'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'returns': None, 'desc': 'Draws the specified text relative to the specified coordinates\nusing the values of the FontSize and\nTextAlignment properties.'}, {'name': 'DrawTextAtAngle', 'args': [{'name': 'text', 'type': 'str'}, {'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}, {'name': 'angle', 'type': 'int'}], 'returns': None, 'desc': 'Draws the specified text starting at the specified coordinates\nat the specified angle using the values of the FontSize and\nTextAlignment properties.'}, {'name': 'GetBackgroundPixelColor', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'returns': 'enums.Color', 'desc': 'Gets the color of the given pixel, ignoring sprites.'}, {'name': 'GetPixelColor', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'returns': 'enums.Color', 'desc': 'Gets the color of the given pixel, including sprites.'}, {'name': 'Save', 'args': [], 'returns': 'str', 'desc': "Saves a picture of this Canvas to the device's external storage.\nIf an error occurs, the Screen's ErrorOccurred event will be called."}, {'name': 'SaveAs', 'args': [{'name': 'fileName', 'type': 'str'}], 'returns': 'str', 'desc': 'Saves a picture of this Canvas to the device\'s external storage in the file\nnamed fileName. fileName must end with one of ".jpg", ".jpeg", or ".png"\n(which determines the file type: JPEG, or PNG).'}, {'name': 'SetBackgroundPixelColor', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}, {'name': 'color', 'type': 'enums.Color'}], 'returns': None, 'desc': 'Sets the color of the given pixel.  This has no effect if the\ncoordinates are out of bounds.'}]}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., BackgroundImage: str=..., ExtendMovesOutsideCanvas: bool=..., FontSize: int=..., Height: int=..., LineWidth: int=..., PaintColor: enums.Color=..., TapThreshold: int=..., TextAlignment: int=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the Canvas's background color as an alpha-red-green-blue
integer, i.e., 0xAARRGGBB.  An alpha of 00
indicates fully transparent and FF means opaque.
The background color only shows if there is no background image."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def BackgroundImage(self) -> str:
        """Specifies the name of a file containing the background image for the Canvas."""
        raise NotImplementedError

    @BackgroundImage.setter
    def BackgroundImage(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def BackgroundImageinBase64(self) -> str:
        """Set the background image in Base64 format. This requires API level >= 8. For devices with API level less than 8, setting this will end up with an empty background."""
        raise NotImplementedError

    @BackgroundImageinBase64.setter
    def BackgroundImageinBase64(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def ExtendMovesOutsideCanvas(self) -> bool:
        """Determines whether moves can extend beyond the canvas borders.   Default is false. This should normally be false, and the property is provided for backwards compatibility."""
        raise NotImplementedError

    @ExtendMovesOutsideCanvas.setter
    def ExtendMovesOutsideCanvas(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontSize(self) -> int:
        """Specifies the font size of text drawn on the Canvas."""
        raise NotImplementedError

    @FontSize.setter
    def FontSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the Canvas's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the Canvas's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def LineWidth(self) -> int:
        """Specifies the width of lines drawn on the Canvas."""
        raise NotImplementedError

    @LineWidth.setter
    def LineWidth(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def PaintColor(self) -> enums.Color:
        """Specifies the paint color as an alpha-red-green-blue integer,
i.e., 0xAARRGGBB.  An alpha of 00 indicates fully
transparent and FF means opaque."""
        raise NotImplementedError

    @PaintColor.setter
    def PaintColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def TapThreshold(self) -> int:
        """Specifies the movement threshold to differentiate a drag from a tap."""
        raise NotImplementedError

    @TapThreshold.setter
    def TapThreshold(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def TextAlignment(self) -> int:
        """Specifies the alignment of the canvas's text: center, normal
(starting at the specified point in DrawText or
DrawTextAtAngle),
or opposite (ending at the specified point in
DrawText or
DrawTextAtAngle)."""
        raise NotImplementedError

    @TextAlignment.setter
    def TextAlignment(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the Canvas should be visible on the screen.  Value is true
if the Canvas is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the Canvas, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the Canvas as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def Clear(self, /) -> None:
        """Clears the canvas, without removing the background image, if one
was provided."""
        raise NotImplementedError

    def DrawArc(self, left: int, top: int, right: int, bottom: int, startAngle: int, sweepAngle: int, useCenter: bool, fill: bool, /) -> None:
        """Draw an arc on Canvas, by drawing an arc from a specified oval (specified by left, top, right & bottom).
Start angle is 0 when heading to the right, and increase when rotate clockwise.
When useCenter is true, a sector will be drawed instead of an arc.
When fill is true, a filled arc (or sector) will be drawed instead of just an outline."""
        raise NotImplementedError

    def DrawCircle(self, centerX: int, centerY: int, radius: int, fill: bool, /) -> None:
        """Draws a circle (filled in) with the given radius centered at the given coordinates on the
Canvas."""
        raise NotImplementedError

    def DrawLine(self, x1: int, y1: int, x2: int, y2: int, /) -> None:
        """Draws a line between the given coordinates on the canvas."""
        raise NotImplementedError

    def DrawPoint(self, x: int, y: int, /) -> None:
        """Draws a point at the given coordinates on the canvas."""
        raise NotImplementedError

    def DrawShape(self, pointList: list, fill: bool, /) -> None:
        """Draws a shape on the canvas.
pointList should be a list contains sub-lists with two number which represents a coordinate.
The first point and last point does not need to be the same. e.g. ((x1 y1) (x2 y2) (x3 y3))
When fill is true, the shape will be filled."""
        raise NotImplementedError

    def DrawText(self, text: str, x: int, y: int, /) -> None:
        """Draws the specified text relative to the specified coordinates
using the values of the FontSize and
TextAlignment properties."""
        raise NotImplementedError

    def DrawTextAtAngle(self, text: str, x: int, y: int, angle: int, /) -> None:
        """Draws the specified text starting at the specified coordinates
at the specified angle using the values of the FontSize and
TextAlignment properties."""
        raise NotImplementedError

    def GetBackgroundPixelColor(self, x: int, y: int, /) -> enums.Color:
        """Gets the color of the given pixel, ignoring sprites."""
        raise NotImplementedError

    def GetPixelColor(self, x: int, y: int, /) -> enums.Color:
        """Gets the color of the given pixel, including sprites."""
        raise NotImplementedError

    def Save(self, /) -> str:
        """Saves a picture of this Canvas to the device's external storage.
If an error occurs, the Screen's ErrorOccurred event will be called."""
        raise NotImplementedError

    def SaveAs(self, fileName: str, /) -> str:
        """Saves a picture of this Canvas to the device's external storage in the file
named fileName. fileName must end with one of ".jpg", ".jpeg", or ".png"
(which determines the file type: JPEG, or PNG)."""
        raise NotImplementedError

    def SetBackgroundPixelColor(self, x: int, y: int, color: enums.Color, /) -> None:
        """Sets the color of the given pixel.  This has no effect if the
coordinates are out of bounds."""
        raise NotImplementedError

    def on_Dragged(self, callback: Callable[[int, int, int, int, int, int, bool], None], /) -> None:
        """Dragged(startX, startY, prevX, prevY, currentX, currentY, draggedAnySprite)

When the user does a drag from one point (prevX, prevY) to
another (x, y).  The pair (startX, startY) indicates where the
user first touched the screen, and "draggedAnySprite" indicates whether a
sprite is being dragged."""
        raise NotImplementedError

    @staticmethod
    def on_any_Dragged(callback: Callable[['Canvas', bool, int, int, int, int, int, int, bool], None], /) -> None:
        """Dragged(startX, startY, prevX, prevY, currentX, currentY, draggedAnySprite)

When the user does a drag from one point (prevX, prevY) to
another (x, y).  The pair (startX, startY) indicates where the
user first touched the screen, and "draggedAnySprite" indicates whether a
sprite is being dragged."""
        raise NotImplementedError

    def on_Flung(self, callback: Callable[[int, int, int, int, int, int, bool], None], /) -> None:
        """Flung(x, y, speed, heading, xvel, yvel, flungSprite)

When a fling gesture (quick swipe) is made on the canvas: provides
the (x,y) position of the start of the fling, relative to the upper
left of the canvas. Also provides the speed (pixels per millisecond) and heading
(-180 to 180 degrees) of the fling, as well as the x velocity and y velocity
components of the fling's vector. The value "flungSprite" is true if a sprite
was located near the the starting point of the fling gesture."""
        raise NotImplementedError

    @staticmethod
    def on_any_Flung(callback: Callable[['Canvas', bool, int, int, int, int, int, int, bool], None], /) -> None:
        """Flung(x, y, speed, heading, xvel, yvel, flungSprite)

When a fling gesture (quick swipe) is made on the canvas: provides
the (x,y) position of the start of the fling, relative to the upper
left of the canvas. Also provides the speed (pixels per millisecond) and heading
(-180 to 180 degrees) of the fling, as well as the x velocity and y velocity
components of the fling's vector. The value "flungSprite" is true if a sprite
was located near the the starting point of the fling gesture."""
        raise NotImplementedError

    def on_TouchDown(self, callback: Callable[[int, int], None], /) -> None:
        """TouchDown(x, y)

When the user begins touching the canvas (places finger on canvas and
leaves it there): provides the (x,y) position of the touch, relative
to the upper left of the canvas"""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchDown(callback: Callable[['Canvas', bool, int, int], None], /) -> None:
        """TouchDown(x, y)

When the user begins touching the canvas (places finger on canvas and
leaves it there): provides the (x,y) position of the touch, relative
to the upper left of the canvas"""
        raise NotImplementedError

    def on_TouchUp(self, callback: Callable[[int, int], None], /) -> None:
        """TouchUp(x, y)

When the user stops touching the canvas (lifts finger after a
TouchDown event): provides the (x,y) position of the touch, relative
to the upper left of the canvas"""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchUp(callback: Callable[['Canvas', bool, int, int], None], /) -> None:
        """TouchUp(x, y)

When the user stops touching the canvas (lifts finger after a
TouchDown event): provides the (x,y) position of the touch, relative
to the upper left of the canvas"""
        raise NotImplementedError

    def on_Touched(self, callback: Callable[[int, int, bool], None], /) -> None:
        """Touched(x, y, touchedAnySprite)

When the user touches the canvas and then immediately lifts finger: provides
the (x,y) position of the touch, relative to the upper left of the canvas.  TouchedAnySprite
is true if the same touch also touched a sprite, and false otherwise."""
        raise NotImplementedError

    @staticmethod
    def on_any_Touched(callback: Callable[['Canvas', bool, int, int, bool], None], /) -> None:
        """Touched(x, y, touchedAnySprite)

When the user touches the canvas and then immediately lifts finger: provides
the (x,y) position of the touch, relative to the upper left of the canvas.  TouchedAnySprite
is true if the same touch also touched a sprite, and false otherwise."""
        raise NotImplementedError

class ImageSprite(Component):
    """A 'sprite' that can be placed on a Canvas, where it can react to touches and drags,
interact with other sprites (Balls and other ImageSprites) and the edge of the
Canvas, and move according to its property values. Its appearance is that of the image
specified in its Picture property (unless its Visible property is
false."""
    __data__ = {'desc': "A 'sprite' that can be placed on a Canvas, where it can react to touches and drags,\ninteract with other sprites (Balls and other ImageSprites) and the edge of the\nCanvas, and move according to its property values. Its appearance is that of the image\nspecified in its Picture property (unless its Visible property is\nfalse.", 'properties': [{'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Controls whether the ImageSprite moves when its speed is non-zero.'}, {'name': 'Heading', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "The ImageSprite's heading in degrees above the positive x-axis. Zero degrees is toward the right\nof the screen; 90 degrees is toward the top of the screen."}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'The height of the ImageSprite in pixels.'}, {'name': 'Interval', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "The interval in milliseconds at which the ImageSprite's position is updated. For example, if the\nInterval is 50 and the Speed is 10, then the ImageSprite will move 10 pixels\nevery 50 milliseconds."}, {'name': 'Picture', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the path of the sprite's picture."}, {'name': 'Rotates', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': "If true, the sprite image rotates to match the sprite's heading. If false, the sprite image\ndoes not rotate when the sprite changes heading. The sprite rotates around its centerpoint."}, {'name': 'Speed', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'The speed at which the ImageSprite moves. The ImageSprite moves this many pixels every\nInterval milliseconds if Enabled is true.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Sets whether sprite should be visible.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'The width of the ImageSprite in pixels.'}, {'name': 'X', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'The horizontal coordinate of the left edge of the ImageSprite, increasing as the ImageSprite moves right.'}, {'name': 'Y', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'The vertical coordinate of the top edge of the ImageSprite, increasing as the ImageSprite moves down.'}, {'name': 'Z', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'How the ImageSprite should be layered relative to other Balls and ImageSprites, with higher-numbered layers in front of lower-numbered layers.'}], 'events': [{'name': 'CollidedWith', 'args': [{'name': 'other', 'type': 'Component'}], 'desc': 'Event handler called when two enabled sprites (Balls or ImageSprites)\ncollide. Note that checking for collisions with a rotated ImageSprite currently\nchecks against its unrotated position. Therefore, collision\nchecking will be inaccurate for tall narrow or short wide sprites that are\nrotated.'}, {'name': 'Dragged', 'args': [{'name': 'startX', 'type': 'int'}, {'name': 'startY', 'type': 'int'}, {'name': 'prevX', 'type': 'int'}, {'name': 'prevY', 'type': 'int'}, {'name': 'currentX', 'type': 'int'}, {'name': 'currentY', 'type': 'int'}], 'desc': 'Event handler for Dragged events.  On all calls, the starting coordinates\nare where the screen was first touched, and the "current" coordinates\ndescribe the endpoint of the current line segment.  On the first call\nwithin a given drag, the "previous" coordinates are the same as the\nstarting coordinates; subsequently, they are the "current" coordinates\nfrom the prior call. Note that the ImageSprite won\'t actually move\nanywhere in response to the Dragged event unless\nMoveTo is specifically called.'}, {'name': 'EdgeReached', 'args': [{'name': 'edge', 'type': 'int'}], 'desc': 'Event handler called when the ImageSprite reaches an edge of the screen.\nIf Bounce is then called with that edge, the sprite will appear to bounce off\nof the edge it reached. Edge here is represented as an integer that indicates one of eight\ndirections north(1), northeast(2), east(3), southeast(4), south (-1), southwest(-2), west(-3),\nand northwest(-4).'}, {'name': 'Flung', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}, {'name': 'speed', 'type': 'int'}, {'name': 'heading', 'type': 'int'}, {'name': 'xvel', 'type': 'int'}, {'name': 'yvel', 'type': 'int'}], 'desc': "When a fling gesture (quick swipe) is made on the sprite: provides\nthe (x,y) position of the start of the fling, relative to the upper\nleft of the canvas. Also provides the speed (pixels per millisecond) and heading\n(-180 to 180 degrees) of the fling, as well as the x velocity and y velocity\ncomponents of the fling's vector."}, {'name': 'NoLongerCollidingWith', 'args': [{'name': 'other', 'type': 'Component'}], 'desc': 'Event indicating that a pair of sprites are no longer colliding.'}, {'name': 'TouchDown', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'desc': 'When the user begins touching the sprite (places finger on sprite and\nleaves it there): provides the (x,y) position of the touch, relative\nto the upper left of the canvas'}, {'name': 'TouchUp', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'desc': 'When the user stops touching the sprite (lifts finger after a\nTouchDown event): provides the (x,y) position of the touch, relative\nto the upper left of the canvas.'}, {'name': 'Touched', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'desc': 'When the user touches the sprite and then immediately lifts finger: provides\nthe (x,y) position of the touch, relative to the upper left of the canvas.'}], 'methods': [{'name': 'Bounce', 'args': [{'name': 'edge', 'type': 'int'}], 'returns': None, 'desc': 'Makes this ImageSprite bounce, as if off a wall. For normal bouncing, the edge argument should\nbe the one returned by EdgeReached.'}, {'name': 'CollidingWith', 'args': [{'name': 'other', 'type': 'Component'}], 'returns': 'bool', 'desc': 'Indicates whether a collision has been registered between this ImageSprite\nand the passed other sprite.'}, {'name': 'MoveIntoBounds', 'args': [], 'returns': None, 'desc': 'Moves the sprite back in bounds if part of it extends out of bounds,\nhaving no effect otherwise. If the sprite is too wide to fit on the\ncanvas, this aligns the left side of the sprite with the left side of the\ncanvas. If the sprite is too tall to fit on the canvas, this aligns the\ntop side of the sprite with the top side of the canvas.'}, {'name': 'MoveTo', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'returns': None, 'desc': 'Moves the ImageSprite so that its left top corner is at the specified x and y coordinates.'}, {'name': 'MoveToPoint', 'args': [{'name': 'coordinates', 'type': 'list'}], 'returns': None, 'desc': 'Moves the ImageSprite so that its origin is at the specified x and y coordinates.'}, {'name': 'PointInDirection', 'args': [{'name': 'x', 'type': 'int'}, {'name': 'y', 'type': 'int'}], 'returns': None, 'desc': 'Turns this ImageSprite to point toward the point with the coordinates (x, y).'}, {'name': 'PointTowards', 'args': [{'name': 'target', 'type': 'Component'}], 'returns': None, 'desc': 'Turns this ImageSprite to point towards a given target sprite. The new heading will be parallel\nto the line joining the centerpoints of the two sprites.'}]}

    def __init__(self, /, *, parent: Component=..., Enabled: bool=..., Heading: int=..., Height: int=..., Interval: int=..., Picture: str=..., Rotates: bool=..., Speed: int=..., Visible: bool=..., Width: int=..., X: int=..., Y: int=..., Z: int=...):
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Controls whether the ImageSprite moves when its speed is non-zero."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Heading(self) -> int:
        """The ImageSprite's heading in degrees above the positive x-axis. Zero degrees is toward the right
of the screen; 90 degrees is toward the top of the screen."""
        raise NotImplementedError

    @Heading.setter
    def Heading(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """The height of the ImageSprite in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Interval(self) -> int:
        """The interval in milliseconds at which the ImageSprite's position is updated. For example, if the
Interval is 50 and the Speed is 10, then the ImageSprite will move 10 pixels
every 50 milliseconds."""
        raise NotImplementedError

    @Interval.setter
    def Interval(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Picture(self) -> str:
        """Specifies the path of the sprite's picture."""
        raise NotImplementedError

    @Picture.setter
    def Picture(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Rotates(self) -> bool:
        """If true, the sprite image rotates to match the sprite's heading. If false, the sprite image
does not rotate when the sprite changes heading. The sprite rotates around its centerpoint."""
        raise NotImplementedError

    @Rotates.setter
    def Rotates(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Speed(self) -> int:
        """The speed at which the ImageSprite moves. The ImageSprite moves this many pixels every
Interval milliseconds if Enabled is true."""
        raise NotImplementedError

    @Speed.setter
    def Speed(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Sets whether sprite should be visible."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """The width of the ImageSprite in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def X(self) -> int:
        """The horizontal coordinate of the left edge of the ImageSprite, increasing as the ImageSprite moves right."""
        raise NotImplementedError

    @X.setter
    def X(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Y(self) -> int:
        """The vertical coordinate of the top edge of the ImageSprite, increasing as the ImageSprite moves down."""
        raise NotImplementedError

    @Y.setter
    def Y(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Z(self) -> int:
        """How the ImageSprite should be layered relative to other Balls and ImageSprites, with higher-numbered layers in front of lower-numbered layers."""
        raise NotImplementedError

    @Z.setter
    def Z(self, value: int, /) -> None:
        raise NotImplementedError

    def Bounce(self, edge: int, /) -> None:
        """Makes this ImageSprite bounce, as if off a wall. For normal bouncing, the edge argument should
be the one returned by EdgeReached."""
        raise NotImplementedError

    def CollidingWith(self, other: Component, /) -> bool:
        """Indicates whether a collision has been registered between this ImageSprite
and the passed other sprite."""
        raise NotImplementedError

    def MoveIntoBounds(self, /) -> None:
        """Moves the sprite back in bounds if part of it extends out of bounds,
having no effect otherwise. If the sprite is too wide to fit on the
canvas, this aligns the left side of the sprite with the left side of the
canvas. If the sprite is too tall to fit on the canvas, this aligns the
top side of the sprite with the top side of the canvas."""
        raise NotImplementedError

    def MoveTo(self, x: int, y: int, /) -> None:
        """Moves the ImageSprite so that its left top corner is at the specified x and y coordinates."""
        raise NotImplementedError

    def MoveToPoint(self, coordinates: list, /) -> None:
        """Moves the ImageSprite so that its origin is at the specified x and y coordinates."""
        raise NotImplementedError

    def PointInDirection(self, x: int, y: int, /) -> None:
        """Turns this ImageSprite to point toward the point with the coordinates (x, y)."""
        raise NotImplementedError

    def PointTowards(self, target: Component, /) -> None:
        """Turns this ImageSprite to point towards a given target sprite. The new heading will be parallel
to the line joining the centerpoints of the two sprites."""
        raise NotImplementedError

    def on_CollidedWith(self, callback: Callable[[Component], None], /) -> None:
        """CollidedWith(other)

Event handler called when two enabled sprites (Balls or ImageSprites)
collide. Note that checking for collisions with a rotated ImageSprite currently
checks against its unrotated position. Therefore, collision
checking will be inaccurate for tall narrow or short wide sprites that are
rotated."""
        raise NotImplementedError

    @staticmethod
    def on_any_CollidedWith(callback: Callable[['ImageSprite', bool, Component], None], /) -> None:
        """CollidedWith(other)

Event handler called when two enabled sprites (Balls or ImageSprites)
collide. Note that checking for collisions with a rotated ImageSprite currently
checks against its unrotated position. Therefore, collision
checking will be inaccurate for tall narrow or short wide sprites that are
rotated."""
        raise NotImplementedError

    def on_Dragged(self, callback: Callable[[int, int, int, int, int, int], None], /) -> None:
        """Dragged(startX, startY, prevX, prevY, currentX, currentY)

Event handler for Dragged events.  On all calls, the starting coordinates
are where the screen was first touched, and the "current" coordinates
describe the endpoint of the current line segment.  On the first call
within a given drag, the "previous" coordinates are the same as the
starting coordinates; subsequently, they are the "current" coordinates
from the prior call. Note that the ImageSprite won't actually move
anywhere in response to the Dragged event unless
MoveTo is specifically called."""
        raise NotImplementedError

    @staticmethod
    def on_any_Dragged(callback: Callable[['ImageSprite', bool, int, int, int, int, int, int], None], /) -> None:
        """Dragged(startX, startY, prevX, prevY, currentX, currentY)

Event handler for Dragged events.  On all calls, the starting coordinates
are where the screen was first touched, and the "current" coordinates
describe the endpoint of the current line segment.  On the first call
within a given drag, the "previous" coordinates are the same as the
starting coordinates; subsequently, they are the "current" coordinates
from the prior call. Note that the ImageSprite won't actually move
anywhere in response to the Dragged event unless
MoveTo is specifically called."""
        raise NotImplementedError

    def on_EdgeReached(self, callback: Callable[[int], None], /) -> None:
        """EdgeReached(edge)

Event handler called when the ImageSprite reaches an edge of the screen.
If Bounce is then called with that edge, the sprite will appear to bounce off
of the edge it reached. Edge here is represented as an integer that indicates one of eight
directions north(1), northeast(2), east(3), southeast(4), south (-1), southwest(-2), west(-3),
and northwest(-4)."""
        raise NotImplementedError

    @staticmethod
    def on_any_EdgeReached(callback: Callable[['ImageSprite', bool, int], None], /) -> None:
        """EdgeReached(edge)

Event handler called when the ImageSprite reaches an edge of the screen.
If Bounce is then called with that edge, the sprite will appear to bounce off
of the edge it reached. Edge here is represented as an integer that indicates one of eight
directions north(1), northeast(2), east(3), southeast(4), south (-1), southwest(-2), west(-3),
and northwest(-4)."""
        raise NotImplementedError

    def on_Flung(self, callback: Callable[[int, int, int, int, int, int], None], /) -> None:
        """Flung(x, y, speed, heading, xvel, yvel)

When a fling gesture (quick swipe) is made on the sprite: provides
the (x,y) position of the start of the fling, relative to the upper
left of the canvas. Also provides the speed (pixels per millisecond) and heading
(-180 to 180 degrees) of the fling, as well as the x velocity and y velocity
components of the fling's vector."""
        raise NotImplementedError

    @staticmethod
    def on_any_Flung(callback: Callable[['ImageSprite', bool, int, int, int, int, int, int], None], /) -> None:
        """Flung(x, y, speed, heading, xvel, yvel)

When a fling gesture (quick swipe) is made on the sprite: provides
the (x,y) position of the start of the fling, relative to the upper
left of the canvas. Also provides the speed (pixels per millisecond) and heading
(-180 to 180 degrees) of the fling, as well as the x velocity and y velocity
components of the fling's vector."""
        raise NotImplementedError

    def on_NoLongerCollidingWith(self, callback: Callable[[Component], None], /) -> None:
        """NoLongerCollidingWith(other)

Event indicating that a pair of sprites are no longer colliding."""
        raise NotImplementedError

    @staticmethod
    def on_any_NoLongerCollidingWith(callback: Callable[['ImageSprite', bool, Component], None], /) -> None:
        """NoLongerCollidingWith(other)

Event indicating that a pair of sprites are no longer colliding."""
        raise NotImplementedError

    def on_TouchDown(self, callback: Callable[[int, int], None], /) -> None:
        """TouchDown(x, y)

When the user begins touching the sprite (places finger on sprite and
leaves it there): provides the (x,y) position of the touch, relative
to the upper left of the canvas"""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchDown(callback: Callable[['ImageSprite', bool, int, int], None], /) -> None:
        """TouchDown(x, y)

When the user begins touching the sprite (places finger on sprite and
leaves it there): provides the (x,y) position of the touch, relative
to the upper left of the canvas"""
        raise NotImplementedError

    def on_TouchUp(self, callback: Callable[[int, int], None], /) -> None:
        """TouchUp(x, y)

When the user stops touching the sprite (lifts finger after a
TouchDown event): provides the (x,y) position of the touch, relative
to the upper left of the canvas."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchUp(callback: Callable[['ImageSprite', bool, int, int], None], /) -> None:
        """TouchUp(x, y)

When the user stops touching the sprite (lifts finger after a
TouchDown event): provides the (x,y) position of the touch, relative
to the upper left of the canvas."""
        raise NotImplementedError

    def on_Touched(self, callback: Callable[[int, int], None], /) -> None:
        """Touched(x, y)

When the user touches the sprite and then immediately lifts finger: provides
the (x,y) position of the touch, relative to the upper left of the canvas."""
        raise NotImplementedError

    @staticmethod
    def on_any_Touched(callback: Callable[['ImageSprite', bool, int, int], None], /) -> None:
        """Touched(x, y)

When the user touches the sprite and then immediately lifts finger: provides
the (x,y) position of the touch, relative to the upper left of the canvas."""
        raise NotImplementedError

class AccelerometerSensor(Component):
    """Non-visible component that can detect shaking and measure acceleration approximately in three
dimensions using SI units (m/s2). The components are:"""
    __data__ = {'desc': 'Non-visible component that can detect shaking and measure acceleration approximately in three\ndimensions using SI units (m/s2). The components are:', 'properties': [{'name': 'Available', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns whether the AccelerometerSensor hardware is available on the device.'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the sensor should generate events.  If true,\nthe sensor will generate events.  Otherwise, no events are\ngenerated even if the device is accelerated or shaken.'}, {'name': 'LegacyMode', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'Prior to the release that added this property the AccelerometerSensor component passed through sensor values directly as received from the Android system. However these values do not compensate for tablets that default to Landscape mode, requiring the MIT App Inventor programmer to compensate. However compensating would result in incorrect results in Portrait mode devices such as phones. We now detect Landscape mode tablets and perform the compensation. However if your project is already compensating for the change, you will now get incorrect results. Although our preferred solution is for you to update your project, you can also just set this property to "true" and our compensation code will be deactivated. Note: We recommend that you update your project as we may remove this property in a future release.'}, {'name': 'MinimumInterval', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the minimum interval required between back-to-back Shaking events,\nin milliseconds.\nOnce the phone starts being shaken, all further Shaking events will be ignored\nuntil the interval has elapsed.'}, {'name': 'Sensitivity', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the sensitivity of the accelerometer. Valid values are: 1 (weak), 2 (moderate),\nand 3 (strong).'}, {'name': 'XAccel', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the acceleration in the X-dimension in SI units (m/sÂ²).\nThe sensor must be enabled to return meaningful values.'}, {'name': 'YAccel', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the acceleration in the Y-dimension in SI units (m/sÂ²).\nThe sensor must be enabled to return meaningful values.'}, {'name': 'ZAccel', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the acceleration in the Z-dimension in SI units (m/sÂ²).\nThe sensor must be enabled to return meaningful values.'}], 'events': [{'name': 'AccelerationChanged', 'args': [{'name': 'xAccel', 'type': 'int'}, {'name': 'yAccel', 'type': 'int'}, {'name': 'zAccel', 'type': 'int'}], 'desc': 'Indicates the acceleration changed in the X, Y, and/or Z dimensions.'}, {'name': 'Shaking', 'args': [], 'desc': 'Indicates the device started being shaken or continues to be shaken.'}], 'methods': []}

    def __init__(self, /, *, parent: Component=..., Enabled: bool=..., LegacyMode: bool=..., MinimumInterval: int=..., Sensitivity: int=...):
        raise NotImplementedError

    @property
    def Available(self) -> bool:
        """Returns whether the AccelerometerSensor hardware is available on the device."""
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Specifies whether the sensor should generate events.  If true,
the sensor will generate events.  Otherwise, no events are
generated even if the device is accelerated or shaken."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def MinimumInterval(self) -> int:
        """Specifies the minimum interval required between back-to-back Shaking events,
in milliseconds.
Once the phone starts being shaken, all further Shaking events will be ignored
until the interval has elapsed."""
        raise NotImplementedError

    @MinimumInterval.setter
    def MinimumInterval(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Sensitivity(self) -> int:
        """Specifies the sensitivity of the accelerometer. Valid values are: 1 (weak), 2 (moderate),
and 3 (strong)."""
        raise NotImplementedError

    @Sensitivity.setter
    def Sensitivity(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def XAccel(self) -> int:
        """Returns the acceleration in the X-dimension in SI units (m/sÂ²).
The sensor must be enabled to return meaningful values."""
        raise NotImplementedError

    @property
    def YAccel(self) -> int:
        """Returns the acceleration in the Y-dimension in SI units (m/sÂ²).
The sensor must be enabled to return meaningful values."""
        raise NotImplementedError

    @property
    def ZAccel(self) -> int:
        """Returns the acceleration in the Z-dimension in SI units (m/sÂ²).
The sensor must be enabled to return meaningful values."""
        raise NotImplementedError

    def on_AccelerationChanged(self, callback: Callable[[int, int, int], None], /) -> None:
        """AccelerationChanged(xAccel, yAccel, zAccel)

Indicates the acceleration changed in the X, Y, and/or Z dimensions."""
        raise NotImplementedError

    @staticmethod
    def on_any_AccelerationChanged(callback: Callable[['AccelerometerSensor', bool, int, int, int], None], /) -> None:
        """AccelerationChanged(xAccel, yAccel, zAccel)

Indicates the acceleration changed in the X, Y, and/or Z dimensions."""
        raise NotImplementedError

    def on_Shaking(self, callback: Callable[[], None], /) -> None:
        """Shaking()

Indicates the device started being shaken or continues to be shaken."""
        raise NotImplementedError

    @staticmethod
    def on_any_Shaking(callback: Callable[['AccelerometerSensor', bool], None], /) -> None:
        """Shaking()

Indicates the device started being shaken or continues to be shaken."""
        raise NotImplementedError

class BarcodeScanner(Component):
    """Component for scanning a QR code and getting back the resulting string."""
    __data__ = {'desc': 'Component for scanning a QR code and getting back the resulting string.', 'properties': [{'name': 'Result', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Gets the text result of the previous scan.'}, {'name': 'UseExternalScanner', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Set whether or not you wish to use an External Scanning program such as\nBar Code Scanner. If false a version of ZXing integrated into App Inventor\nwill be used.'}], 'events': [{'name': 'AfterScan', 'args': [{'name': 'result', 'type': 'str'}], 'desc': 'Indicates that the scanner has read a (text) result and provides the result'}], 'methods': [{'name': 'DoScan', 'args': [], 'returns': None, 'desc': 'Begins a barcode scan, using the camera. When the scan is complete, the\nAfterScan event will be raised.'}]}

    def __init__(self, /, *, parent: Component=..., UseExternalScanner: bool=...):
        raise NotImplementedError

    @property
    def Result(self) -> str:
        """Gets the text result of the previous scan."""
        raise NotImplementedError

    @property
    def UseExternalScanner(self) -> bool:
        """Set whether or not you wish to use an External Scanning program such as
Bar Code Scanner. If false a version of ZXing integrated into App Inventor
will be used."""
        raise NotImplementedError

    @UseExternalScanner.setter
    def UseExternalScanner(self, value: bool, /) -> None:
        raise NotImplementedError

    def DoScan(self, /) -> None:
        """Begins a barcode scan, using the camera. When the scan is complete, the
AfterScan event will be raised."""
        raise NotImplementedError

    def on_AfterScan(self, callback: Callable[[str], None], /) -> None:
        """AfterScan(result)

Indicates that the scanner has read a (text) result and provides the result"""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterScan(callback: Callable[['BarcodeScanner', bool, str], None], /) -> None:
        """AfterScan(result)

Indicates that the scanner has read a (text) result and provides the result"""
        raise NotImplementedError

class Barometer(Component):
    """Physical world component that can measure the ambient air pressure if
supported by the hardware."""
    __data__ = {'desc': 'Physical world component that can measure the ambient air pressure if\nsupported by the hardware.', 'properties': [{'name': 'AirPressure', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'The atmospheric pressure in hPa (millibar), if the sensor is available \nand enabled.'}, {'name': 'Available', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Specifies whether or not the device has the hardware to support the Barometer component.'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the sensor should generate events.  If true,\nthe sensor will generate events.  Otherwise, no events are\ngenerated.'}, {'name': 'RefreshTime', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'The requested minimum time in milliseconds between changes in readings being reported. Android is not guaranteed to honor the request. Setting this property has no effect on pre-Gingerbread devices.'}], 'events': [{'name': 'AirPressureChanged', 'args': [{'name': 'pressure', 'type': 'int'}], 'desc': 'Called when a change is detected in the air pressure (provided in hPa).'}], 'methods': []}

    def __init__(self, /, *, parent: Component=..., Enabled: bool=..., RefreshTime: int=...):
        raise NotImplementedError

    @property
    def AirPressure(self) -> int:
        """The atmospheric pressure in hPa (millibar), if the sensor is available 
and enabled."""
        raise NotImplementedError

    @property
    def Available(self) -> bool:
        """Specifies whether or not the device has the hardware to support the Barometer component."""
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Specifies whether the sensor should generate events.  If true,
the sensor will generate events.  Otherwise, no events are
generated."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def RefreshTime(self) -> int:
        """The requested minimum time in milliseconds between changes in readings being reported. Android is not guaranteed to honor the request. Setting this property has no effect on pre-Gingerbread devices."""
        raise NotImplementedError

    @RefreshTime.setter
    def RefreshTime(self, value: int, /) -> None:
        raise NotImplementedError

    def on_AirPressureChanged(self, callback: Callable[[int], None], /) -> None:
        """AirPressureChanged(pressure)

Called when a change is detected in the air pressure (provided in hPa)."""
        raise NotImplementedError

    @staticmethod
    def on_any_AirPressureChanged(callback: Callable[['Barometer', bool, int], None], /) -> None:
        """AirPressureChanged(pressure)

Called when a change is detected in the air pressure (provided in hPa)."""
        raise NotImplementedError

class Clock(Component):
    """Non-visible component that provides the instant in time using the internal clock on the phone.
It can fire a timer at regularly set intervals and perform time calculations, manipulations,
and conversions."""
    __data__ = {'desc': 'Non-visible component that provides the instant in time using the internal clock on the phone.\nIt can fire a timer at regularly set intervals and perform time calculations, manipulations,\nand conversions.', 'properties': [{'name': 'TimerAlwaysFires', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Will fire even when application is not showing on the screen if true'}, {'name': 'TimerEnabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the Timer event should run.'}, {'name': 'TimerInterval', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the interval between subsequent Timer events.\n\n   Note: Drift may occur over time and that the system may not honor the\ntiming specified here if the app or another process on the phone is busy.\n'}], 'events': [{'name': 'Timer', 'args': [], 'desc': 'The Timer event runs when the timer has gone off.'}], 'methods': [{'name': 'AddDays', 'args': [{'name': 'instant', 'type': 'enums.Instant'}, {'name': 'quantity', 'type': 'int'}], 'returns': 'enums.Instant', 'desc': 'Returns an instant in time some days after the given instant.'}, {'name': 'AddDuration', 'args': [{'name': 'instant', 'type': 'enums.Instant'}, {'name': 'quantity', 'type': 'int'}], 'returns': 'enums.Instant', 'desc': 'Returns an instant in time some duration after the argument'}, {'name': 'AddHours', 'args': [{'name': 'instant', 'type': 'enums.Instant'}, {'name': 'quantity', 'type': 'int'}], 'returns': 'enums.Instant', 'desc': 'Returns an instant in time some hours after the given instant.'}, {'name': 'AddMinutes', 'args': [{'name': 'instant', 'type': 'enums.Instant'}, {'name': 'quantity', 'type': 'int'}], 'returns': 'enums.Instant', 'desc': 'Returns an instant in time some minutes after the given instant.'}, {'name': 'AddMonths', 'args': [{'name': 'instant', 'type': 'enums.Instant'}, {'name': 'quantity', 'type': 'int'}], 'returns': 'enums.Instant', 'desc': 'Returns an instant in time some months after the given instant.'}, {'name': 'AddSeconds', 'args': [{'name': 'instant', 'type': 'enums.Instant'}, {'name': 'quantity', 'type': 'int'}], 'returns': 'enums.Instant', 'desc': 'Returns an instant in time some seconds after the given instant.'}, {'name': 'AddWeeks', 'args': [{'name': 'instant', 'type': 'enums.Instant'}, {'name': 'quantity', 'type': 'int'}], 'returns': 'enums.Instant', 'desc': 'Returns An instant in time some weeks after the given instant.'}, {'name': 'AddYears', 'args': [{'name': 'instant', 'type': 'enums.Instant'}, {'name': 'quantity', 'type': 'int'}], 'returns': 'enums.Instant', 'desc': 'Returns an instant in time some years after the given instant.'}, {'name': 'DayOfMonth', 'args': [{'name': 'instant', 'type': 'enums.Instant'}], 'returns': 'int', 'desc': 'Returns the day of the month.'}, {'name': 'Duration', 'args': [{'name': 'start', 'type': 'enums.Instant'}, {'name': 'end', 'type': 'enums.Instant'}], 'returns': 'int', 'desc': 'Returns the milliseconds by which end follows start (+ or -)'}, {'name': 'DurationToDays', 'args': [{'name': 'duration', 'type': 'int'}], 'returns': 'int', 'desc': 'Returns the duration converted from milliseconds to days.'}, {'name': 'DurationToHours', 'args': [{'name': 'duration', 'type': 'int'}], 'returns': 'int', 'desc': 'Returns the duration converted from milliseconds to hours.'}, {'name': 'DurationToMinutes', 'args': [{'name': 'duration', 'type': 'int'}], 'returns': 'int', 'desc': 'Returns the duration converted from milliseconds to minutes.'}, {'name': 'DurationToSeconds', 'args': [{'name': 'duration', 'type': 'int'}], 'returns': 'int', 'desc': 'Returns the duration converted from milliseconds to seconds.'}, {'name': 'DurationToWeeks', 'args': [{'name': 'duration', 'type': 'int'}], 'returns': 'int', 'desc': 'Returns the duration converted from milliseconds to weeks.'}, {'name': 'FormatDate', 'args': [{'name': 'instant', 'type': 'enums.Instant'}, {'name': 'pattern', 'type': 'str'}], 'returns': 'str', 'desc': 'Converts and formats an instant into a string of date with the specified pattern. To learn\nmore about valid patterns, please see\nSimpleDateFormat.'}, {'name': 'FormatDateTime', 'args': [{'name': 'instant', 'type': 'enums.Instant'}, {'name': 'pattern', 'type': 'str'}], 'returns': 'str', 'desc': 'Converts and formats an instant into a string of date and time with the specified pattern.\nTo learn more about valid patterns, please see\nSimpleDateFormat.'}, {'name': 'FormatTime', 'args': [{'name': 'instant', 'type': 'enums.Instant'}], 'returns': 'str', 'desc': 'Converts and formats the given instant into a string with the specified pattern. To learn\nmore about valid patterns, please see\nSimpleDateFormat.'}, {'name': 'GetMillis', 'args': [{'name': 'instant', 'type': 'enums.Instant'}], 'returns': 'int', 'desc': 'Returns the instant in time measured as milliseconds since 1970.'}, {'name': 'Hour', 'args': [{'name': 'instant', 'type': 'enums.Instant'}], 'returns': 'int', 'desc': 'Returns the hours for the given date.'}, {'name': 'MakeDate', 'args': [{'name': 'year', 'type': 'int'}, {'name': 'month', 'type': 'int'}, {'name': 'day', 'type': 'int'}], 'returns': 'enums.Instant', 'desc': 'Returns an instant in time specified by year, month, date in UTC.\nValid values for the month field are 1-12 and 1-31 for the day field.'}, {'name': 'MakeInstant', 'args': [{'name': 'from', 'type': 'str'}], 'returns': 'enums.Instant', 'desc': 'Returns an instant in time specified by MM/dd/YYYY hh:mm:ss or MM/dd/YYYY or hh:mm.'}, {'name': 'MakeInstantFromMillis', 'args': [{'name': 'millis', 'type': 'int'}], 'returns': 'enums.Instant', 'desc': 'Returns an instant in time specified by the milliseconds since 1970 in UTC.'}, {'name': 'MakeInstantFromParts', 'args': [{'name': 'year', 'type': 'int'}, {'name': 'month', 'type': 'int'}, {'name': 'day', 'type': 'int'}, {'name': 'hour', 'type': 'int'}, {'name': 'minute', 'type': 'int'}, {'name': 'second', 'type': 'int'}], 'returns': 'enums.Instant', 'desc': 'Returns an instant in time specified by year, month, date, hour, minute, second in UTC.'}, {'name': 'MakeTime', 'args': [{'name': 'hour', 'type': 'int'}, {'name': 'minute', 'type': 'int'}, {'name': 'second', 'type': 'int'}], 'returns': 'enums.Instant', 'desc': 'Returns an instant in time specified by hour, minute, second in UTC.'}, {'name': 'Minute', 'args': [{'name': 'instant', 'type': 'enums.Instant'}], 'returns': 'int', 'desc': 'Returns the minutes for the given date.'}, {'name': 'Month', 'args': [{'name': 'instant', 'type': 'enums.Instant'}], 'returns': 'int', 'desc': 'Returns the number of the month for the given instant.'}, {'name': 'MonthName', 'args': [{'name': 'instant', 'type': 'enums.Instant'}], 'returns': 'str', 'desc': 'Returns the name of the month for the given instant.'}, {'name': 'Now', 'args': [], 'returns': 'enums.Instant', 'desc': "Returns the current instant in time read from phone's clock."}, {'name': 'Second', 'args': [{'name': 'instant', 'type': 'enums.Instant'}], 'returns': 'int', 'desc': 'Returns the seconds for the given instant.'}, {'name': 'SystemTime', 'args': [], 'returns': 'int', 'desc': "Returns the phone's internal time."}, {'name': 'Weekday', 'args': [{'name': 'instant', 'type': 'enums.Instant'}], 'returns': 'int', 'desc': 'Returns the weekday for the given instant.'}, {'name': 'WeekdayName', 'args': [{'name': 'instant', 'type': 'enums.Instant'}], 'returns': 'str', 'desc': 'Returns the name of the weekday for the given instant.'}, {'name': 'Year', 'args': [{'name': 'instant', 'type': 'enums.Instant'}], 'returns': 'int', 'desc': 'Returns the year of the given instant.'}]}

    def __init__(self, /, *, parent: Component=..., TimerAlwaysFires: bool=..., TimerEnabled: bool=..., TimerInterval: int=...):
        raise NotImplementedError

    @property
    def TimerAlwaysFires(self) -> bool:
        """Will fire even when application is not showing on the screen if true"""
        raise NotImplementedError

    @TimerAlwaysFires.setter
    def TimerAlwaysFires(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def TimerEnabled(self) -> bool:
        """Specifies whether the Timer event should run."""
        raise NotImplementedError

    @TimerEnabled.setter
    def TimerEnabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def TimerInterval(self) -> int:
        """Specifies the interval between subsequent Timer events.

   Note: Drift may occur over time and that the system may not honor the
timing specified here if the app or another process on the phone is busy.
"""
        raise NotImplementedError

    @TimerInterval.setter
    def TimerInterval(self, value: int, /) -> None:
        raise NotImplementedError

    def AddDays(self, instant: enums.Instant, quantity: int, /) -> enums.Instant:
        """Returns an instant in time some days after the given instant."""
        raise NotImplementedError

    def AddDuration(self, instant: enums.Instant, quantity: int, /) -> enums.Instant:
        """Returns an instant in time some duration after the argument"""
        raise NotImplementedError

    def AddHours(self, instant: enums.Instant, quantity: int, /) -> enums.Instant:
        """Returns an instant in time some hours after the given instant."""
        raise NotImplementedError

    def AddMinutes(self, instant: enums.Instant, quantity: int, /) -> enums.Instant:
        """Returns an instant in time some minutes after the given instant."""
        raise NotImplementedError

    def AddMonths(self, instant: enums.Instant, quantity: int, /) -> enums.Instant:
        """Returns an instant in time some months after the given instant."""
        raise NotImplementedError

    def AddSeconds(self, instant: enums.Instant, quantity: int, /) -> enums.Instant:
        """Returns an instant in time some seconds after the given instant."""
        raise NotImplementedError

    def AddWeeks(self, instant: enums.Instant, quantity: int, /) -> enums.Instant:
        """Returns An instant in time some weeks after the given instant."""
        raise NotImplementedError

    def AddYears(self, instant: enums.Instant, quantity: int, /) -> enums.Instant:
        """Returns an instant in time some years after the given instant."""
        raise NotImplementedError

    def DayOfMonth(self, instant: enums.Instant, /) -> int:
        """Returns the day of the month."""
        raise NotImplementedError

    def Duration(self, start: enums.Instant, end: enums.Instant, /) -> int:
        """Returns the milliseconds by which end follows start (+ or -)"""
        raise NotImplementedError

    def DurationToDays(self, duration: int, /) -> int:
        """Returns the duration converted from milliseconds to days."""
        raise NotImplementedError

    def DurationToHours(self, duration: int, /) -> int:
        """Returns the duration converted from milliseconds to hours."""
        raise NotImplementedError

    def DurationToMinutes(self, duration: int, /) -> int:
        """Returns the duration converted from milliseconds to minutes."""
        raise NotImplementedError

    def DurationToSeconds(self, duration: int, /) -> int:
        """Returns the duration converted from milliseconds to seconds."""
        raise NotImplementedError

    def DurationToWeeks(self, duration: int, /) -> int:
        """Returns the duration converted from milliseconds to weeks."""
        raise NotImplementedError

    def FormatDate(self, instant: enums.Instant, pattern: str, /) -> str:
        """Converts and formats an instant into a string of date with the specified pattern. To learn
more about valid patterns, please see
SimpleDateFormat."""
        raise NotImplementedError

    def FormatDateTime(self, instant: enums.Instant, pattern: str, /) -> str:
        """Converts and formats an instant into a string of date and time with the specified pattern.
To learn more about valid patterns, please see
SimpleDateFormat."""
        raise NotImplementedError

    def FormatTime(self, instant: enums.Instant, /) -> str:
        """Converts and formats the given instant into a string with the specified pattern. To learn
more about valid patterns, please see
SimpleDateFormat."""
        raise NotImplementedError

    def GetMillis(self, instant: enums.Instant, /) -> int:
        """Returns the instant in time measured as milliseconds since 1970."""
        raise NotImplementedError

    def Hour(self, instant: enums.Instant, /) -> int:
        """Returns the hours for the given date."""
        raise NotImplementedError

    def MakeDate(self, year: int, month: int, day: int, /) -> enums.Instant:
        """Returns an instant in time specified by year, month, date in UTC.
Valid values for the month field are 1-12 and 1-31 for the day field."""
        raise NotImplementedError

    def MakeInstant(self, from_: str, /) -> enums.Instant:
        """Returns an instant in time specified by MM/dd/YYYY hh:mm:ss or MM/dd/YYYY or hh:mm."""
        raise NotImplementedError

    def MakeInstantFromMillis(self, millis: int, /) -> enums.Instant:
        """Returns an instant in time specified by the milliseconds since 1970 in UTC."""
        raise NotImplementedError

    def MakeInstantFromParts(self, year: int, month: int, day: int, hour: int, minute: int, second: int, /) -> enums.Instant:
        """Returns an instant in time specified by year, month, date, hour, minute, second in UTC."""
        raise NotImplementedError

    def MakeTime(self, hour: int, minute: int, second: int, /) -> enums.Instant:
        """Returns an instant in time specified by hour, minute, second in UTC."""
        raise NotImplementedError

    def Minute(self, instant: enums.Instant, /) -> int:
        """Returns the minutes for the given date."""
        raise NotImplementedError

    def Month(self, instant: enums.Instant, /) -> int:
        """Returns the number of the month for the given instant."""
        raise NotImplementedError

    def MonthName(self, instant: enums.Instant, /) -> str:
        """Returns the name of the month for the given instant."""
        raise NotImplementedError

    def Now(self, /) -> enums.Instant:
        """Returns the current instant in time read from phone's clock."""
        raise NotImplementedError

    def Second(self, instant: enums.Instant, /) -> int:
        """Returns the seconds for the given instant."""
        raise NotImplementedError

    def SystemTime(self, /) -> int:
        """Returns the phone's internal time."""
        raise NotImplementedError

    def Weekday(self, instant: enums.Instant, /) -> int:
        """Returns the weekday for the given instant."""
        raise NotImplementedError

    def WeekdayName(self, instant: enums.Instant, /) -> str:
        """Returns the name of the weekday for the given instant."""
        raise NotImplementedError

    def Year(self, instant: enums.Instant, /) -> int:
        """Returns the year of the given instant."""
        raise NotImplementedError

    def on_Timer(self, callback: Callable[[], None], /) -> None:
        """Timer()

The Timer event runs when the timer has gone off."""
        raise NotImplementedError

    @staticmethod
    def on_any_Timer(callback: Callable[['Clock', bool], None], /) -> None:
        """Timer()

The Timer event runs when the timer has gone off."""
        raise NotImplementedError

class GyroscopeSensor(Component):
    """Component providing data from the device's gyroscope sensor."""
    __data__ = {'desc': "Component providing data from the device's gyroscope sensor.", 'properties': [{'name': 'Available', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Indicates whether a gyroscope sensor is available.'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Enabled property getter method.'}, {'name': 'XAngularVelocity', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'The angular velocity around the X axis, in degrees per second.'}, {'name': 'YAngularVelocity', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'The angular velocity around the Y axis, in degrees per second.'}, {'name': 'ZAngularVelocity', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'The angular velocity around the Z axis, in degrees per second.'}], 'events': [{'name': 'GyroscopeChanged', 'args': [{'name': 'xAngularVelocity', 'type': 'int'}, {'name': 'yAngularVelocity', 'type': 'int'}, {'name': 'zAngularVelocity', 'type': 'int'}, {'name': 'timestamp', 'type': 'int'}], 'desc': 'Indicates that the gyroscope sensor data has changed. The timestamp parameter is the time in nanoseconds at which the event occurred.'}], 'methods': []}

    def __init__(self, /, *, parent: Component=..., Enabled: bool=...):
        raise NotImplementedError

    @property
    def Available(self) -> bool:
        """Indicates whether a gyroscope sensor is available."""
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Enabled property getter method."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def XAngularVelocity(self) -> int:
        """The angular velocity around the X axis, in degrees per second."""
        raise NotImplementedError

    @property
    def YAngularVelocity(self) -> int:
        """The angular velocity around the Y axis, in degrees per second."""
        raise NotImplementedError

    @property
    def ZAngularVelocity(self) -> int:
        """The angular velocity around the Z axis, in degrees per second."""
        raise NotImplementedError

    def on_GyroscopeChanged(self, callback: Callable[[int, int, int, int], None], /) -> None:
        """GyroscopeChanged(xAngularVelocity, yAngularVelocity, zAngularVelocity, timestamp)

Indicates that the gyroscope sensor data has changed. The timestamp parameter is the time in nanoseconds at which the event occurred."""
        raise NotImplementedError

    @staticmethod
    def on_any_GyroscopeChanged(callback: Callable[['GyroscopeSensor', bool, int, int, int, int], None], /) -> None:
        """GyroscopeChanged(xAngularVelocity, yAngularVelocity, zAngularVelocity, timestamp)

Indicates that the gyroscope sensor data has changed. The timestamp parameter is the time in nanoseconds at which the event occurred."""
        raise NotImplementedError

class Hygrometer(Component):
    """Physical world component that can measure the relative ambient air 
humidity if supported by the hardware."""
    __data__ = {'desc': 'Physical world component that can measure the relative ambient air \nhumidity if supported by the hardware.', 'properties': [{'name': 'Available', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Specifies whether or not the device has the hardware to support the Hygrometer component.'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the sensor should generate events.  If true,\nthe sensor will generate events.  Otherwise, no events are\ngenerated.'}, {'name': 'Humidity', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the relative ambient humidity as a percentage.\nThe sensor must be enabled and available \nto return meaningful values.'}, {'name': 'RefreshTime', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'The requested minimum time in milliseconds between changes in readings being reported. Android is not guaranteed to honor the request. Setting this property has no effect on pre-Gingerbread devices.'}], 'events': [{'name': 'HumidityChanged', 'args': [{'name': 'humidity', 'type': 'int'}], 'desc': 'Indicates the relative humidity changed.'}], 'methods': []}

    def __init__(self, /, *, parent: Component=..., Enabled: bool=..., RefreshTime: int=...):
        raise NotImplementedError

    @property
    def Available(self) -> bool:
        """Specifies whether or not the device has the hardware to support the Hygrometer component."""
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Specifies whether the sensor should generate events.  If true,
the sensor will generate events.  Otherwise, no events are
generated."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Humidity(self) -> int:
        """Returns the relative ambient humidity as a percentage.
The sensor must be enabled and available 
to return meaningful values."""
        raise NotImplementedError

    @property
    def RefreshTime(self) -> int:
        """The requested minimum time in milliseconds between changes in readings being reported. Android is not guaranteed to honor the request. Setting this property has no effect on pre-Gingerbread devices."""
        raise NotImplementedError

    @RefreshTime.setter
    def RefreshTime(self, value: int, /) -> None:
        raise NotImplementedError

    def on_HumidityChanged(self, callback: Callable[[int], None], /) -> None:
        """HumidityChanged(humidity)

Indicates the relative humidity changed."""
        raise NotImplementedError

    @staticmethod
    def on_any_HumidityChanged(callback: Callable[['Hygrometer', bool, int], None], /) -> None:
        """HumidityChanged(humidity)

Indicates the relative humidity changed."""
        raise NotImplementedError

class LightSensor(Component):
    """Physical world component that can measure the light level."""
    __data__ = {'desc': 'Physical world component that can measure the light level.', 'properties': [{'name': 'Available', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Specifies whether or not the device has the hardware to support the LightSensor component.'}, {'name': 'AverageLux', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the brightness in lux by averaging the previous 10 measured values.\nThe sensor must be enabled and available to return meaningful values.'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the sensor should generate events.  If true,\nthe sensor will generate events.  Otherwise, no events are\ngenerated.'}, {'name': 'Lux', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the last measured brightness in lux.\nThe sensor must be enabled and available to return meaningful values.'}, {'name': 'RefreshTime', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'The requested minimum time in milliseconds between changes in readings being reported. Android is not guaranteed to honor the request. Setting this property has no effect on pre-Gingerbread devices.'}], 'events': [{'name': 'LightChanged', 'args': [{'name': 'lux', 'type': 'int'}], 'desc': 'Indicates the light level changed.'}], 'methods': []}

    def __init__(self, /, *, parent: Component=..., Enabled: bool=..., RefreshTime: int=...):
        raise NotImplementedError

    @property
    def Available(self) -> bool:
        """Specifies whether or not the device has the hardware to support the LightSensor component."""
        raise NotImplementedError

    @property
    def AverageLux(self) -> int:
        """Returns the brightness in lux by averaging the previous 10 measured values.
The sensor must be enabled and available to return meaningful values."""
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Specifies whether the sensor should generate events.  If true,
the sensor will generate events.  Otherwise, no events are
generated."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Lux(self) -> int:
        """Returns the last measured brightness in lux.
The sensor must be enabled and available to return meaningful values."""
        raise NotImplementedError

    @property
    def RefreshTime(self) -> int:
        """The requested minimum time in milliseconds between changes in readings being reported. Android is not guaranteed to honor the request. Setting this property has no effect on pre-Gingerbread devices."""
        raise NotImplementedError

    @RefreshTime.setter
    def RefreshTime(self, value: int, /) -> None:
        raise NotImplementedError

    def on_LightChanged(self, callback: Callable[[int], None], /) -> None:
        """LightChanged(lux)

Indicates the light level changed."""
        raise NotImplementedError

    @staticmethod
    def on_any_LightChanged(callback: Callable[['LightSensor', bool, int], None], /) -> None:
        """LightChanged(lux)

Indicates the light level changed."""
        raise NotImplementedError

class LocationSensor(Component):
    """Non-visible component providing location information, including Latitude,
Longitude, Altitude (if supported by the device), speed (if supported by
the device), and address. This can also perform "geocoding", converting a given address (not
necessarily the current one) to a latitude (with the LatitudeFromAddress
method) and a longitude (with the LongitudeFromAddress method)."""
    __data__ = {'desc': 'Non-visible component providing location information, including Latitude,\nLongitude, Altitude (if supported by the device), speed (if supported by\nthe device), and address. This can also perform "geocoding", converting a given address (not\nnecessarily the current one) to a latitude (with the LatitudeFromAddress\nmethod) and a longitude (with the LongitudeFromAddress method).', 'properties': [{'name': 'Accuracy', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': "The LocationSensor will be able to locate the device with a varying degree of confidence,\nbased on the quality of satellite, cell towers, and other data used to estimate location.\nThe Accuracy value is the radius in meters around the sensor's detected location. The device\nhas a 68% chance to be located within this radius. More precise location detection will result\nin a smaller accuracy number, which allows the app to have more confidence where the device\nis actually located.\n\n   If the accuracy is not known, the return value is 0.0\n"}, {'name': 'Altitude', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Altitude of the device measured in meters, if available.\n\n   Altitude is measured from the\nWorld Geodetic System 84 reference ellipsoid,\nnot sea level.\nNote that it is difficult for devices to accurately sense altitude. Altitude reported on a\nphone/tablet can easily be off by 30 meters or more.\n'}, {'name': 'AvailableProviders', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': 'List of available service providers, such as gps or network. This information is provided\nas a list and in text form.'}, {'name': 'CurrentAddress', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': "Physical street address of the device from Google's map database.\n\n   The address might not always be available from the provider, and the address reported may not\nalways be of the building where the device is located.\nIf Google has no address information available for a particular location, this will return\nNo address available.\n"}, {'name': 'DistanceInterval', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Determines the minimum distance interval, in meters, that the sensor will try to use for\nsending out location updates. For example, if this is set to 50, then the sensor will fire a\nLocationChanged event only after 50 meters have been\ntraversed. However, the sensor does not guarantee that an update will be received at exactly\nthe distance interval. It may take more than 5 meters to fire an event, for instance.\n\n   It is also useful to check against Accuracy when using this property. When your\ndevice is moving, the accuracy of the detected location is constantly changing.\n'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'If true, the LocationSensor will attempt to read location information from\nGPS, WiFi location, or other means available on the device. This setting does not control\nwhether location information is actually available. Device location must be enabled or\ndisabled in the device settings.'}, {'name': 'HasAccuracy', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'If true, the device can report its accuracy level.'}, {'name': 'HasAltitude', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'If true, the device can report its altitude.'}, {'name': 'HasLongitudeLatitude', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'If true, the device can report longitude and latitude.  It is\nalways the case that either both or neither are.'}, {'name': 'Latitude', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'The most recently available latitude value in degrees reported to 5 decimal places.\nIf no value is available, 0 will be returned.\nLatitude is a value between 90 (north) and -90 (south), where 0 marks the Equator.'}, {'name': 'Longitude', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'The most recent available longitude value in degrees reported to 5 decimal places.\nIf no value is available, 0 will be returned.\nLongitude is a value between 180 (east) and -180 (west), where 0 marks the Prime Meridian.'}, {'name': 'ProviderLocked', 'type': 'bool', 'ro': False, 'do': False, 'bo': True, 'desc': 'The device will not change the service provider.\n\n   It is possible for a device to switch service providers when the current provider is unable\nto provide adequate location information. ProviderLocked is a Boolean value: true/false.\nSet to true to prevent providers from changing. Set to false\nto allow for automatic switching when necessary.\n'}, {'name': 'ProviderName', 'type': 'str', 'ro': False, 'do': False, 'bo': True, 'desc': 'The current service provider. The provider will most likely be either GPS or network.'}, {'name': 'TimeInterval', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Determines the minimum time interval, in milliseconds, that the sensor will try to use for\nsending out location updates. However, location updates will only be received when the\nlocation of the phone actually changes, and use of the specified time interval is not\nguaranteed. For example, if 30000 is used as the time interval, location updates will never\nbe fired sooner than 30000ms, but they may be fired anytime after.\n\n   Values smaller than 30000ms (30 seconds) are not practical for most devices. Small values\nmay drain battery and overwork the GPS.\n'}], 'events': [{'name': 'LocationChanged', 'args': [{'name': 'latitude', 'type': 'int'}, {'name': 'longitude', 'type': 'int'}, {'name': 'altitude', 'type': 'int'}, {'name': 'speed', 'type': 'int'}], 'desc': 'Indicates that a new location has been detected. Speed is reported in meters/second\nOther values match their properties.'}, {'name': 'StatusChanged', 'args': [{'name': 'provider', 'type': 'str'}, {'name': 'status', 'type': 'str'}], 'desc': 'Indicates that the status of the location provider service has changed, such as when a\nprovider is lost or a new provider starts being used.'}], 'methods': [{'name': 'LatitudeFromAddress', 'args': [{'name': 'locationName', 'type': 'str'}], 'returns': 'int', 'desc': 'Derives latitude from the given locationName.'}, {'name': 'LongitudeFromAddress', 'args': [{'name': 'locationName', 'type': 'str'}], 'returns': 'int', 'desc': 'Derives longitude from the given locationName.'}]}

    def __init__(self, /, *, parent: Component=..., DistanceInterval: int=..., Enabled: bool=..., TimeInterval: int=...):
        raise NotImplementedError

    @property
    def Accuracy(self) -> int:
        """The LocationSensor will be able to locate the device with a varying degree of confidence,
based on the quality of satellite, cell towers, and other data used to estimate location.
The Accuracy value is the radius in meters around the sensor's detected location. The device
has a 68% chance to be located within this radius. More precise location detection will result
in a smaller accuracy number, which allows the app to have more confidence where the device
is actually located.

   If the accuracy is not known, the return value is 0.0
"""
        raise NotImplementedError

    @property
    def Altitude(self) -> int:
        """Altitude of the device measured in meters, if available.

   Altitude is measured from the
World Geodetic System 84 reference ellipsoid,
not sea level.
Note that it is difficult for devices to accurately sense altitude. Altitude reported on a
phone/tablet can easily be off by 30 meters or more.
"""
        raise NotImplementedError

    @property
    def AvailableProviders(self) -> list:
        """List of available service providers, such as gps or network. This information is provided
as a list and in text form."""
        raise NotImplementedError

    @property
    def CurrentAddress(self) -> str:
        """Physical street address of the device from Google's map database.

   The address might not always be available from the provider, and the address reported may not
always be of the building where the device is located.
If Google has no address information available for a particular location, this will return
No address available.
"""
        raise NotImplementedError

    @property
    def DistanceInterval(self) -> int:
        """Determines the minimum distance interval, in meters, that the sensor will try to use for
sending out location updates. For example, if this is set to 50, then the sensor will fire a
LocationChanged event only after 50 meters have been
traversed. However, the sensor does not guarantee that an update will be received at exactly
the distance interval. It may take more than 5 meters to fire an event, for instance.

   It is also useful to check against Accuracy when using this property. When your
device is moving, the accuracy of the detected location is constantly changing.
"""
        raise NotImplementedError

    @DistanceInterval.setter
    def DistanceInterval(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """If true, the LocationSensor will attempt to read location information from
GPS, WiFi location, or other means available on the device. This setting does not control
whether location information is actually available. Device location must be enabled or
disabled in the device settings."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def HasAccuracy(self) -> bool:
        """If true, the device can report its accuracy level."""
        raise NotImplementedError

    @property
    def HasAltitude(self) -> bool:
        """If true, the device can report its altitude."""
        raise NotImplementedError

    @property
    def HasLongitudeLatitude(self) -> bool:
        """If true, the device can report longitude and latitude.  It is
always the case that either both or neither are."""
        raise NotImplementedError

    @property
    def Latitude(self) -> int:
        """The most recently available latitude value in degrees reported to 5 decimal places.
If no value is available, 0 will be returned.
Latitude is a value between 90 (north) and -90 (south), where 0 marks the Equator."""
        raise NotImplementedError

    @property
    def Longitude(self) -> int:
        """The most recent available longitude value in degrees reported to 5 decimal places.
If no value is available, 0 will be returned.
Longitude is a value between 180 (east) and -180 (west), where 0 marks the Prime Meridian."""
        raise NotImplementedError

    @property
    def ProviderLocked(self) -> bool:
        """The device will not change the service provider.

   It is possible for a device to switch service providers when the current provider is unable
to provide adequate location information. ProviderLocked is a Boolean value: true/false.
Set to true to prevent providers from changing. Set to false
to allow for automatic switching when necessary.
"""
        raise NotImplementedError

    @ProviderLocked.setter
    def ProviderLocked(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def ProviderName(self) -> str:
        """The current service provider. The provider will most likely be either GPS or network."""
        raise NotImplementedError

    @ProviderName.setter
    def ProviderName(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def TimeInterval(self) -> int:
        """Determines the minimum time interval, in milliseconds, that the sensor will try to use for
sending out location updates. However, location updates will only be received when the
location of the phone actually changes, and use of the specified time interval is not
guaranteed. For example, if 30000 is used as the time interval, location updates will never
be fired sooner than 30000ms, but they may be fired anytime after.

   Values smaller than 30000ms (30 seconds) are not practical for most devices. Small values
may drain battery and overwork the GPS.
"""
        raise NotImplementedError

    @TimeInterval.setter
    def TimeInterval(self, value: int, /) -> None:
        raise NotImplementedError

    def LatitudeFromAddress(self, locationName: str, /) -> int:
        """Derives latitude from the given locationName."""
        raise NotImplementedError

    def LongitudeFromAddress(self, locationName: str, /) -> int:
        """Derives longitude from the given locationName."""
        raise NotImplementedError

    def on_LocationChanged(self, callback: Callable[[int, int, int, int], None], /) -> None:
        """LocationChanged(latitude, longitude, altitude, speed)

Indicates that a new location has been detected. Speed is reported in meters/second
Other values match their properties."""
        raise NotImplementedError

    @staticmethod
    def on_any_LocationChanged(callback: Callable[['LocationSensor', bool, int, int, int, int], None], /) -> None:
        """LocationChanged(latitude, longitude, altitude, speed)

Indicates that a new location has been detected. Speed is reported in meters/second
Other values match their properties."""
        raise NotImplementedError

    def on_StatusChanged(self, callback: Callable[[str, str], None], /) -> None:
        """StatusChanged(provider, status)

Indicates that the status of the location provider service has changed, such as when a
provider is lost or a new provider starts being used."""
        raise NotImplementedError

    @staticmethod
    def on_any_StatusChanged(callback: Callable[['LocationSensor', bool, str, str], None], /) -> None:
        """StatusChanged(provider, status)

Indicates that the status of the location provider service has changed, such as when a
provider is lost or a new provider starts being used."""
        raise NotImplementedError

class MagneticFieldSensor(Component):
    """Component for MagneticFieldSensor"""
    __data__ = {'desc': 'Component for MagneticFieldSensor', 'properties': [{'name': 'AbsoluteStrength', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Indicates the absolute strength of the field.'}, {'name': 'Available', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Indicates that there is a magnetic field sensor in the device and it is available.'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Indicates whether or not the magnetic field sensor is enabled and working.'}, {'name': 'MaximumRange', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Indicates the maximum range the magnetic sensor can reach.'}, {'name': 'XStrength', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': "Indicates the field's strength in the X-axis."}, {'name': 'YStrength', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': "Indicates the field's strength in the Y-axis."}, {'name': 'ZStrength', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': "Indicates the field's strength in the Z-axis."}], 'events': [{'name': 'MagneticChanged', 'args': [{'name': 'xStrength', 'type': 'int'}, {'name': 'yStrength', 'type': 'int'}, {'name': 'zStrength', 'type': 'int'}, {'name': 'absoluteStrength', 'type': 'int'}], 'desc': 'Triggers when magnetic field has changed, setting the new values in parameters.'}], 'methods': []}

    def __init__(self, /, *, parent: Component=..., Enabled: bool=...):
        raise NotImplementedError

    @property
    def AbsoluteStrength(self) -> int:
        """Indicates the absolute strength of the field."""
        raise NotImplementedError

    @property
    def Available(self) -> bool:
        """Indicates that there is a magnetic field sensor in the device and it is available."""
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Indicates whether or not the magnetic field sensor is enabled and working."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def MaximumRange(self) -> int:
        """Indicates the maximum range the magnetic sensor can reach."""
        raise NotImplementedError

    @property
    def XStrength(self) -> int:
        """Indicates the field's strength in the X-axis."""
        raise NotImplementedError

    @property
    def YStrength(self) -> int:
        """Indicates the field's strength in the Y-axis."""
        raise NotImplementedError

    @property
    def ZStrength(self) -> int:
        """Indicates the field's strength in the Z-axis."""
        raise NotImplementedError

    def on_MagneticChanged(self, callback: Callable[[int, int, int, int], None], /) -> None:
        """MagneticChanged(xStrength, yStrength, zStrength, absoluteStrength)

Triggers when magnetic field has changed, setting the new values in parameters."""
        raise NotImplementedError

    @staticmethod
    def on_any_MagneticChanged(callback: Callable[['MagneticFieldSensor', bool, int, int, int, int], None], /) -> None:
        """MagneticChanged(xStrength, yStrength, zStrength, absoluteStrength)

Triggers when magnetic field has changed, setting the new values in parameters."""
        raise NotImplementedError

class NearField(Component):
    """Non-visible component to provide NFC capabilities. For now this component supports the reading
and writing of text tags only (if supported by the device)."""
    __data__ = {'desc': 'Non-visible component to provide NFC capabilities. For now this component supports the reading\nand writing of text tags only (if supported by the device).', 'properties': [{'name': 'LastMessage', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the content of the most recently received tag.'}, {'name': 'ReadMode', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the NFC hardware should operate in read mode (true) or\nwrite mode (false).'}, {'name': 'TextToWrite', 'type': 'str', 'ro': False, 'do': False, 'bo': True, 'desc': 'Specifies the content that will be written to the tag when in write mode. This method has no\neffect if ReadMode is true.'}, {'name': 'WriteType', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the write type for the NFC component. For this version of the component, it is always\n1.'}], 'events': [{'name': 'TagRead', 'args': [{'name': 'message', 'type': 'str'}], 'desc': 'Indicates that a new tag has been detected.\nCurrently this is only a plain text tag, as specified in the\nmanifest.'}, {'name': 'TagWritten', 'args': [], 'desc': 'Indicates that a tag has come into range of the NFC sensor and has been written.'}], 'methods': []}

    def __init__(self, /, *, parent: Component=..., ReadMode: bool=...):
        raise NotImplementedError

    @property
    def LastMessage(self) -> str:
        """Returns the content of the most recently received tag."""
        raise NotImplementedError

    @property
    def ReadMode(self) -> bool:
        """Specifies whether the NFC hardware should operate in read mode (true) or
write mode (false)."""
        raise NotImplementedError

    @ReadMode.setter
    def ReadMode(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def TextToWrite(self) -> str:
        """Specifies the content that will be written to the tag when in write mode. This method has no
effect if ReadMode is true."""
        raise NotImplementedError

    @TextToWrite.setter
    def TextToWrite(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def WriteType(self) -> int:
        """Returns the write type for the NFC component. For this version of the component, it is always
1."""
        raise NotImplementedError

    def on_TagRead(self, callback: Callable[[str], None], /) -> None:
        """TagRead(message)

Indicates that a new tag has been detected.
Currently this is only a plain text tag, as specified in the
manifest."""
        raise NotImplementedError

    @staticmethod
    def on_any_TagRead(callback: Callable[['NearField', bool, str], None], /) -> None:
        """TagRead(message)

Indicates that a new tag has been detected.
Currently this is only a plain text tag, as specified in the
manifest."""
        raise NotImplementedError

    def on_TagWritten(self, callback: Callable[[], None], /) -> None:
        """TagWritten()

Indicates that a tag has come into range of the NFC sensor and has been written."""
        raise NotImplementedError

    @staticmethod
    def on_any_TagWritten(callback: Callable[['NearField', bool], None], /) -> None:
        """TagWritten()

Indicates that a tag has come into range of the NFC sensor and has been written."""
        raise NotImplementedError

class OrientationSensor(Component):
    """Use an orientation sensor component to determine the phone's spatial orientation."""
    __data__ = {'desc': "Use an orientation sensor component to determine the phone's spatial orientation.", 'properties': [{'name': 'Angle', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns an angle that tells the direction in which the device is tiled. That is, it tells the\ndirection of the force that would be felt by a ball rolling on the surface of the device.'}, {'name': 'Available', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Indicates whether the orientation sensor is present on the device.'}, {'name': 'Azimuth', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the azimuth angle of the device.\nTo return meaningful values the sensor must be enabled.'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the orientation sensor is enabled.'}, {'name': 'Magnitude', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns a number between 0 and 1 indicating how much the device\nis tilted. It gives the magnitude of the force that would be felt\nby a ball rolling on the surface of the device. For the angle of\ntilt, use Angle.'}, {'name': 'Pitch', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the pitch angle of the device.\nTo return meaningful values the sensor must be enabled.'}, {'name': 'Roll', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the roll angle of the device.\nTo return meaningful values the sensor must be enabled.'}], 'events': [{'name': 'OrientationChanged', 'args': [{'name': 'azimuth', 'type': 'int'}, {'name': 'pitch', 'type': 'int'}, {'name': 'roll', 'type': 'int'}], 'desc': 'The OrientationChanged event handler is run when the orientation has changed.'}], 'methods': []}

    def __init__(self, /, *, parent: Component=..., Enabled: bool=...):
        raise NotImplementedError

    @property
    def Angle(self) -> int:
        """Returns an angle that tells the direction in which the device is tiled. That is, it tells the
direction of the force that would be felt by a ball rolling on the surface of the device."""
        raise NotImplementedError

    @property
    def Available(self) -> bool:
        """Indicates whether the orientation sensor is present on the device."""
        raise NotImplementedError

    @property
    def Azimuth(self) -> int:
        """Returns the azimuth angle of the device.
To return meaningful values the sensor must be enabled."""
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Specifies whether the orientation sensor is enabled."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Magnitude(self) -> int:
        """Returns a number between 0 and 1 indicating how much the device
is tilted. It gives the magnitude of the force that would be felt
by a ball rolling on the surface of the device. For the angle of
tilt, use Angle."""
        raise NotImplementedError

    @property
    def Pitch(self) -> int:
        """Returns the pitch angle of the device.
To return meaningful values the sensor must be enabled."""
        raise NotImplementedError

    @property
    def Roll(self) -> int:
        """Returns the roll angle of the device.
To return meaningful values the sensor must be enabled."""
        raise NotImplementedError

    def on_OrientationChanged(self, callback: Callable[[int, int, int], None], /) -> None:
        """OrientationChanged(azimuth, pitch, roll)

The OrientationChanged event handler is run when the orientation has changed."""
        raise NotImplementedError

    @staticmethod
    def on_any_OrientationChanged(callback: Callable[['OrientationSensor', bool, int, int, int], None], /) -> None:
        """OrientationChanged(azimuth, pitch, roll)

The OrientationChanged event handler is run when the orientation has changed."""
        raise NotImplementedError

class Pedometer(Component):
    """This component keeps count of steps using the accelerometer."""
    __data__ = {'desc': 'This component keeps count of steps using the accelerometer.', 'properties': [{'name': 'Distance', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the approximate distance traveled in meters.'}, {'name': 'ElapsedTime', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the time elapsed in milliseconds since the pedometer has started.'}, {'name': 'SimpleSteps', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the number of simple steps taken since the pedometer has started.'}, {'name': 'StopDetectionTimeout', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Returns the duration of idleness (no steps detected) after which to go into a "stopped" state.'}, {'name': 'StrideLength', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Returns the current estimate of stride length in meters, if calibrated, or returns the\ndefault (0.73 m) otherwise.'}, {'name': 'WalkSteps', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the number of walk steps taken since the pedometer has started.'}], 'events': [{'name': 'SimpleStep', 'args': [{'name': 'simpleSteps', 'type': 'int'}, {'name': 'distance', 'type': 'int'}], 'desc': 'This event is run when a raw step is detected.'}, {'name': 'WalkStep', 'args': [{'name': 'walkSteps', 'type': 'int'}, {'name': 'distance', 'type': 'int'}], 'desc': 'This event is run when a walking step is detected. A walking step is a step that appears to be involved in forward motion.'}], 'methods': [{'name': 'Reset', 'args': [], 'returns': None, 'desc': 'Resets the step counter, distance measure and time running.'}, {'name': 'Save', 'args': [], 'returns': None, 'desc': 'Saves the pedometer state to the phone. Permits permits accumulation of steps and distance between invocations of an App that uses the pedometer. Different Apps will have their own saved state.'}, {'name': 'Start', 'args': [], 'returns': None, 'desc': 'Starts the pedometer.'}, {'name': 'Stop', 'args': [], 'returns': None, 'desc': 'Stops the pedometer.'}]}

    def __init__(self, /, *, parent: Component=..., StopDetectionTimeout: int=..., StrideLength: int=...):
        raise NotImplementedError

    @property
    def Distance(self) -> int:
        """Returns the approximate distance traveled in meters."""
        raise NotImplementedError

    @property
    def ElapsedTime(self) -> int:
        """Returns the time elapsed in milliseconds since the pedometer has started."""
        raise NotImplementedError

    @property
    def SimpleSteps(self) -> int:
        """Returns the number of simple steps taken since the pedometer has started."""
        raise NotImplementedError

    @property
    def StopDetectionTimeout(self) -> int:
        """Returns the duration of idleness (no steps detected) after which to go into a "stopped" state."""
        raise NotImplementedError

    @StopDetectionTimeout.setter
    def StopDetectionTimeout(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def StrideLength(self) -> int:
        """Returns the current estimate of stride length in meters, if calibrated, or returns the
default (0.73 m) otherwise."""
        raise NotImplementedError

    @StrideLength.setter
    def StrideLength(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WalkSteps(self) -> int:
        """Returns the number of walk steps taken since the pedometer has started."""
        raise NotImplementedError

    def Reset(self, /) -> None:
        """Resets the step counter, distance measure and time running."""
        raise NotImplementedError

    def Save(self, /) -> None:
        """Saves the pedometer state to the phone. Permits permits accumulation of steps and distance between invocations of an App that uses the pedometer. Different Apps will have their own saved state."""
        raise NotImplementedError

    def Start(self, /) -> None:
        """Starts the pedometer."""
        raise NotImplementedError

    def Stop(self, /) -> None:
        """Stops the pedometer."""
        raise NotImplementedError

    def on_SimpleStep(self, callback: Callable[[int, int], None], /) -> None:
        """SimpleStep(simpleSteps, distance)

This event is run when a raw step is detected."""
        raise NotImplementedError

    @staticmethod
    def on_any_SimpleStep(callback: Callable[['Pedometer', bool, int, int], None], /) -> None:
        """SimpleStep(simpleSteps, distance)

This event is run when a raw step is detected."""
        raise NotImplementedError

    def on_WalkStep(self, callback: Callable[[int, int], None], /) -> None:
        """WalkStep(walkSteps, distance)

This event is run when a walking step is detected. A walking step is a step that appears to be involved in forward motion."""
        raise NotImplementedError

    @staticmethod
    def on_any_WalkStep(callback: Callable[['Pedometer', bool, int, int], None], /) -> None:
        """WalkStep(walkSteps, distance)

This event is run when a walking step is detected. A walking step is a step that appears to be involved in forward motion."""
        raise NotImplementedError

class ProximitySensor(Component):
    """A sensor component that can measure the proximity of an object (in cm) relative to the view
screen of a device. This sensor is typically used to determine whether a handset is being held
up to a persons ear; i.e. lets you determine how far away an object is from a device. Many
devices return the absolute distance, in cm, but some return only near and far values. In this
case, the sensor usually reports its maximum range value in the far state and a lesser value
in the near state. It reports the following value:"""
    __data__ = {'desc': 'A sensor component that can measure the proximity of an object (in cm) relative to the view\nscreen of a device. This sensor is typically used to determine whether a handset is being held\nup to a persons ear; i.e. lets you determine how far away an object is from a device. Many\ndevices return the absolute distance, in cm, but some return only near and far values. In this\ncase, the sensor usually reports its maximum range value in the far state and a lesser value\nin the near state. It reports the following value:', 'properties': [{'name': 'Available', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Reports whether or not the device has a proximity sensor.'}, {'name': 'Distance', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the distance from the object to the device.\nThe sensor must be enabled to return meaningful values.'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'If true, the sensor will generate events.  Otherwise, no events\nare generated.'}, {'name': 'KeepRunningWhenOnPause', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Returns value of keepRunningWhenOnPause.'}, {'name': 'MaximumRange', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Determines a sensor\'s maximum range. Some proximity sensors return binary values\nthat represent "near" or "far." In this case, the sensor usually reports\nits maximum range value in the far state and a lesser value in the near state.\nTypically, the far value is a value > 5 cm, but this can vary from sensor to sensor.'}], 'events': [{'name': 'ProximityChanged', 'args': [{'name': 'distance', 'type': 'int'}], 'desc': 'Triggered when distance (in cm) of the object to the device changes.'}], 'methods': []}

    def __init__(self, /, *, parent: Component=..., Enabled: bool=..., KeepRunningWhenOnPause: bool=...):
        raise NotImplementedError

    @property
    def Available(self) -> bool:
        """Reports whether or not the device has a proximity sensor."""
        raise NotImplementedError

    @property
    def Distance(self) -> int:
        """Returns the distance from the object to the device.
The sensor must be enabled to return meaningful values."""
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """If true, the sensor will generate events.  Otherwise, no events
are generated."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def KeepRunningWhenOnPause(self) -> bool:
        """Returns value of keepRunningWhenOnPause."""
        raise NotImplementedError

    @KeepRunningWhenOnPause.setter
    def KeepRunningWhenOnPause(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def MaximumRange(self) -> int:
        """Determines a sensor's maximum range. Some proximity sensors return binary values
that represent "near" or "far." In this case, the sensor usually reports
its maximum range value in the far state and a lesser value in the near state.
Typically, the far value is a value > 5 cm, but this can vary from sensor to sensor."""
        raise NotImplementedError

    def on_ProximityChanged(self, callback: Callable[[int], None], /) -> None:
        """ProximityChanged(distance)

Triggered when distance (in cm) of the object to the device changes."""
        raise NotImplementedError

    @staticmethod
    def on_any_ProximityChanged(callback: Callable[['ProximitySensor', bool, int], None], /) -> None:
        """ProximityChanged(distance)

Triggered when distance (in cm) of the object to the device changes."""
        raise NotImplementedError

class Thermometer(Component):
    """Physical world component that can measure the ambient air temperature if
supported by the hardware."""
    __data__ = {'desc': 'Physical world component that can measure the ambient air temperature if\nsupported by the hardware.', 'properties': [{'name': 'Available', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Specifies whether or not the device has the hardware to support the Thermometer component.'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the sensor should generate events.  If true,\nthe sensor will generate events.  Otherwise, no events are\ngenerated.'}, {'name': 'RefreshTime', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'The requested minimum time in milliseconds between changes in readings being reported. Android is not guaranteed to honor the request. Setting this property has no effect on pre-Gingerbread devices.'}, {'name': 'Temperature', 'type': 'int', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the temperature in degrees Celsius.\nThe sensor must be enabled and available \nto return meaningful values.'}], 'events': [{'name': 'TemperatureChanged', 'args': [{'name': 'temperature', 'type': 'int'}], 'desc': 'Indicates a change of temperature, provided in degrees Celsius.'}], 'methods': []}

    def __init__(self, /, *, parent: Component=..., Enabled: bool=..., RefreshTime: int=...):
        raise NotImplementedError

    @property
    def Available(self) -> bool:
        """Specifies whether or not the device has the hardware to support the Thermometer component."""
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Specifies whether the sensor should generate events.  If true,
the sensor will generate events.  Otherwise, no events are
generated."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def RefreshTime(self) -> int:
        """The requested minimum time in milliseconds between changes in readings being reported. Android is not guaranteed to honor the request. Setting this property has no effect on pre-Gingerbread devices."""
        raise NotImplementedError

    @RefreshTime.setter
    def RefreshTime(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Temperature(self) -> int:
        """Returns the temperature in degrees Celsius.
The sensor must be enabled and available 
to return meaningful values."""
        raise NotImplementedError

    def on_TemperatureChanged(self, callback: Callable[[int], None], /) -> None:
        """TemperatureChanged(temperature)

Indicates a change of temperature, provided in degrees Celsius."""
        raise NotImplementedError

    @staticmethod
    def on_any_TemperatureChanged(callback: Callable[['Thermometer', bool, int], None], /) -> None:
        """TemperatureChanged(temperature)

Indicates a change of temperature, provided in degrees Celsius."""
        raise NotImplementedError

class ContactPicker(Component):
    """A button that, when clicked on, displays a list of the contacts to choose among. After the user
has made a selection, the following properties will be set to information about the chosen
contact:"""
    __data__ = {'desc': 'A button that, when clicked on, displays a list of the contacts to choose among. After the user\nhas made a selection, the following properties will be set to information about the chosen\ncontact:', 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the ContactPicker's background color as an alpha-red-green-blue\ninteger.  If an Image has been set, the color\nchange will not be visible until the Image is removed."}, {'name': 'ContactName', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the full name of the selected contact, or the empty string if a name is unavailable.'}, {'name': 'ContactUri', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns a URI that specifies the location of the contact on the device.'}, {'name': 'EmailAddress', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the primary email address of the selected contact, or the empty string if an email\naddress is unavailable.'}, {'name': 'EmailAddressList', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns a list of email addresses associated with the selected contact.'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the ContactPicker should be active and clickable.'}, {'name': 'FontBold', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the text of the ContactPicker should be bold.\nSome fonts do not support bold.'}, {'name': 'FontItalic', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the text of the ContactPicker should be italic.\nSome fonts do not support italic.'}, {'name': 'FontSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text font size of the ContactPicker, measured in sp(scale-independent pixels).'}, {'name': 'FontTypeface', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the text font face of the ContactPicker as default, serif, sans\nserif, monospace, or custom font typeface. To add a custom typeface,\nupload a .ttf file to the project's media."}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the ContactPicker's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the ContactPicker's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Image', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the path of the ContactPicker's image. If there is both an Image and a\nBackgroundColor specified, only the Image will be visible."}, {'name': 'PhoneNumber', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the primary phone number associated with the selected contact, or the empty string if\nno phone number is associated with the contact.'}, {'name': 'PhoneNumberList', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns a list of phone numbers associated with the selected contact.'}, {'name': 'Picture', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': "Returns a picture URI for the selected contact, which can be\nused to retrieve the contact's photo and other fields."}, {'name': 'Shape', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies the shape of the ContactPicker. The valid values for this property are 0 (default),\n1 (rounded), 2 (rectangle), and 3 (oval). The Shape will not be visible if an\nImage is used.'}, {'name': 'ShowFeedback', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies if a visual feedback should be shown when a ContactPicker with an assigned\nImage is pressed.'}, {'name': 'Text', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text displayed by the ContactPicker.'}, {'name': 'TextAlignment', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the alignment of the ContactPicker's text. Valid values are:\n0 (normal; e.g., left-justified if text is written left to right),\n1 (center), or\n2 (opposite; e.g., right-justified if text is written left to right)."}, {'name': 'TextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text color of the ContactPicker as an alpha-red-green-blue\ninteger.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the ContactPicker should be visible on the screen.  Value is true\nif the ContactPicker is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the ContactPicker, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the ContactPicker as a percentage\nof the Screen's Width."}], 'events': [{'name': 'AfterPicking', 'args': [], 'desc': 'Event to be raised after the ContactPicker activity returns its\nresult and the properties have been filled in.'}, {'name': 'BeforePicking', 'args': [], 'desc': 'Event to raise when the ContactPicker is clicked or the picker is shown\nusing the Open method.  This event occurs before the picker is displayed, and\ncan be used to prepare the picker before it is shown.'}, {'name': 'GotFocus', 'args': [], 'desc': 'Indicates the cursor moved over the ContactPicker so it is now possible\nto click it.'}, {'name': 'LostFocus', 'args': [], 'desc': 'Indicates the cursor moved away from the ContactPicker so it is now no\nlonger possible to click it.'}, {'name': 'TouchDown', 'args': [], 'desc': 'Indicates that the ContactPicker was pressed down.'}, {'name': 'TouchUp', 'args': [], 'desc': 'Indicates that the ContactPicker has been released.'}], 'methods': [{'name': 'Open', 'args': [], 'returns': None, 'desc': 'Opens the ContactPicker, as though the user clicked on it.'}, {'name': 'ViewContact', 'args': [{'name': 'uri', 'type': 'str'}], 'returns': None, 'desc': "Opens the selected contact's entry in the device's default Contacts app."}]}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., Enabled: bool=..., FontBold: bool=..., FontItalic: bool=..., FontSize: int=..., FontTypeface: str=..., Height: int=..., Image: str=..., Shape: int=..., ShowFeedback: bool=..., Text: str=..., TextAlignment: int=..., TextColor: enums.Color=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the ContactPicker's background color as an alpha-red-green-blue
integer.  If an Image has been set, the color
change will not be visible until the Image is removed."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def ContactName(self) -> str:
        """Returns the full name of the selected contact, or the empty string if a name is unavailable."""
        raise NotImplementedError

    @property
    def ContactUri(self) -> str:
        """Returns a URI that specifies the location of the contact on the device."""
        raise NotImplementedError

    @property
    def EmailAddress(self) -> str:
        """Returns the primary email address of the selected contact, or the empty string if an email
address is unavailable."""
        raise NotImplementedError

    @property
    def EmailAddressList(self) -> list:
        """Returns a list of email addresses associated with the selected contact."""
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Specifies whether the ContactPicker should be active and clickable."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontBold(self) -> bool:
        """Specifies whether the text of the ContactPicker should be bold.
Some fonts do not support bold."""
        raise NotImplementedError

    @FontBold.setter
    def FontBold(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontItalic(self) -> bool:
        """Specifies whether the text of the ContactPicker should be italic.
Some fonts do not support italic."""
        raise NotImplementedError

    @FontItalic.setter
    def FontItalic(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontSize(self) -> int:
        """Specifies the text font size of the ContactPicker, measured in sp(scale-independent pixels)."""
        raise NotImplementedError

    @FontSize.setter
    def FontSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the ContactPicker's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the ContactPicker's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Image(self) -> str:
        """Specifies the path of the ContactPicker's image. If there is both an Image and a
BackgroundColor specified, only the Image will be visible."""
        raise NotImplementedError

    @Image.setter
    def Image(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def PhoneNumber(self) -> str:
        """Returns the primary phone number associated with the selected contact, or the empty string if
no phone number is associated with the contact."""
        raise NotImplementedError

    @property
    def PhoneNumberList(self) -> list:
        """Returns a list of phone numbers associated with the selected contact."""
        raise NotImplementedError

    @property
    def Picture(self) -> str:
        """Returns a picture URI for the selected contact, which can be
used to retrieve the contact's photo and other fields."""
        raise NotImplementedError

    @property
    def ShowFeedback(self) -> bool:
        """Specifies if a visual feedback should be shown when a ContactPicker with an assigned
Image is pressed."""
        raise NotImplementedError

    @ShowFeedback.setter
    def ShowFeedback(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Text(self) -> str:
        """Specifies the text displayed by the ContactPicker."""
        raise NotImplementedError

    @Text.setter
    def Text(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def TextColor(self) -> enums.Color:
        """Specifies the text color of the ContactPicker as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @TextColor.setter
    def TextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the ContactPicker should be visible on the screen.  Value is true
if the ContactPicker is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the ContactPicker, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the ContactPicker as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def Open(self, /) -> None:
        """Opens the ContactPicker, as though the user clicked on it."""
        raise NotImplementedError

    def ViewContact(self, uri: str, /) -> None:
        """Opens the selected contact's entry in the device's default Contacts app."""
        raise NotImplementedError

    def on_AfterPicking(self, callback: Callable[[], None], /) -> None:
        """AfterPicking()

Event to be raised after the ContactPicker activity returns its
result and the properties have been filled in."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterPicking(callback: Callable[['ContactPicker', bool], None], /) -> None:
        """AfterPicking()

Event to be raised after the ContactPicker activity returns its
result and the properties have been filled in."""
        raise NotImplementedError

    def on_BeforePicking(self, callback: Callable[[], None], /) -> None:
        """BeforePicking()

Event to raise when the ContactPicker is clicked or the picker is shown
using the Open method.  This event occurs before the picker is displayed, and
can be used to prepare the picker before it is shown."""
        raise NotImplementedError

    @staticmethod
    def on_any_BeforePicking(callback: Callable[['ContactPicker', bool], None], /) -> None:
        """BeforePicking()

Event to raise when the ContactPicker is clicked or the picker is shown
using the Open method.  This event occurs before the picker is displayed, and
can be used to prepare the picker before it is shown."""
        raise NotImplementedError

    def on_GotFocus(self, callback: Callable[[], None], /) -> None:
        """GotFocus()

Indicates the cursor moved over the ContactPicker so it is now possible
to click it."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotFocus(callback: Callable[['ContactPicker', bool], None], /) -> None:
        """GotFocus()

Indicates the cursor moved over the ContactPicker so it is now possible
to click it."""
        raise NotImplementedError

    def on_LostFocus(self, callback: Callable[[], None], /) -> None:
        """LostFocus()

Indicates the cursor moved away from the ContactPicker so it is now no
longer possible to click it."""
        raise NotImplementedError

    @staticmethod
    def on_any_LostFocus(callback: Callable[['ContactPicker', bool], None], /) -> None:
        """LostFocus()

Indicates the cursor moved away from the ContactPicker so it is now no
longer possible to click it."""
        raise NotImplementedError

    def on_TouchDown(self, callback: Callable[[], None], /) -> None:
        """TouchDown()

Indicates that the ContactPicker was pressed down."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchDown(callback: Callable[['ContactPicker', bool], None], /) -> None:
        """TouchDown()

Indicates that the ContactPicker was pressed down."""
        raise NotImplementedError

    def on_TouchUp(self, callback: Callable[[], None], /) -> None:
        """TouchUp()

Indicates that the ContactPicker has been released."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchUp(callback: Callable[['ContactPicker', bool], None], /) -> None:
        """TouchUp()

Indicates that the ContactPicker has been released."""
        raise NotImplementedError

class EmailPicker(Component):
    """An EmailPicker is a kind of text box. If the user begins entering the name or email address of
a contact, the phone will show a dropdown menu of choices that complete the entry. If there are
many contacts, the dropdown can take several seconds to appear, and can show intermediate
results while the matches are being computed."""
    __data__ = {'desc': 'An EmailPicker is a kind of text box. If the user begins entering the name or email address of\na contact, the phone will show a dropdown menu of choices that complete the entry. If there are\nmany contacts, the dropdown can take several seconds to appear, and can show intermediate\nresults while the matches are being computed.', 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "The background color of the EmailPicker`. You can choose a color by name in the Designer or in\nthe Blocks Editor. The default background color is 'default' (shaded 3-D look)."}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'If set, user can enter text into the EmailPicker.'}, {'name': 'FontBold', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies whether the text of the EmailPicker should be bold.\nSome fonts do not support bold.'}, {'name': 'FontItalic', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies whether the text of the EmailPicker should be italic.\nSome fonts do not support italic.'}, {'name': 'FontSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text font size of the EmailPicker, measured in sp(scale-independent pixels).'}, {'name': 'FontTypeface', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'The text font face of the EmailPicker. Valid values are 0 (default), 1 (serif), 2 (sans\nserif), or 3 (monospace).'}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the EmailPicker's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the EmailPicker's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Hint', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'EmailPicker hint for the user.'}, {'name': 'Text', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'The text in the EmailPicker, which can be set by the programmer in the Designer or Blocks Editor,\nor it can be entered by the user (unless the Enabled property is false).'}, {'name': 'TextAlignment', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the alignment of the EmailPicker's text. Valid values are:\n0 (normal; e.g., left-justified if text is written left to right),\n1 (center), or\n2 (opposite; e.g., right-justified if text is written left to right)."}, {'name': 'TextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text color of the EmailPicker as an alpha-red-green-blue\ninteger.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the EmailPicker should be visible on the screen.  Value is true\nif the EmailPicker is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the EmailPicker, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the EmailPicker as a percentage\nof the Screen's Width."}], 'events': [{'name': 'GotFocus', 'args': [], 'desc': 'Event raised when the EmailPicker is selected for input, such as by\nthe user touching it.'}, {'name': 'LostFocus', 'args': [], 'desc': 'Event raised when the EmailPicker is no longer selected for input, such\nas if the user touches a different text box.'}], 'methods': [{'name': 'RequestFocus', 'args': [], 'returns': None, 'desc': 'Request focus to current EmailPicker.'}]}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., Enabled: bool=..., FontBold: bool=..., FontItalic: bool=..., FontSize: int=..., FontTypeface: str=..., Height: int=..., Hint: str=..., Text: str=..., TextAlignment: int=..., TextColor: enums.Color=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """The background color of the EmailPicker`. You can choose a color by name in the Designer or in
the Blocks Editor. The default background color is 'default' (shaded 3-D look)."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """If set, user can enter text into the EmailPicker."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontSize(self) -> int:
        """Specifies the text font size of the EmailPicker, measured in sp(scale-independent pixels)."""
        raise NotImplementedError

    @FontSize.setter
    def FontSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the EmailPicker's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the EmailPicker's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Hint(self) -> str:
        """EmailPicker hint for the user."""
        raise NotImplementedError

    @Hint.setter
    def Hint(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Text(self) -> str:
        """The text in the EmailPicker, which can be set by the programmer in the Designer or Blocks Editor,
or it can be entered by the user (unless the Enabled property is false)."""
        raise NotImplementedError

    @Text.setter
    def Text(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def TextColor(self) -> enums.Color:
        """Specifies the text color of the EmailPicker as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @TextColor.setter
    def TextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the EmailPicker should be visible on the screen.  Value is true
if the EmailPicker is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the EmailPicker, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the EmailPicker as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def RequestFocus(self, /) -> None:
        """Request focus to current EmailPicker."""
        raise NotImplementedError

    def on_GotFocus(self, callback: Callable[[], None], /) -> None:
        """GotFocus()

Event raised when the EmailPicker is selected for input, such as by
the user touching it."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotFocus(callback: Callable[['EmailPicker', bool], None], /) -> None:
        """GotFocus()

Event raised when the EmailPicker is selected for input, such as by
the user touching it."""
        raise NotImplementedError

    def on_LostFocus(self, callback: Callable[[], None], /) -> None:
        """LostFocus()

Event raised when the EmailPicker is no longer selected for input, such
as if the user touches a different text box."""
        raise NotImplementedError

    @staticmethod
    def on_any_LostFocus(callback: Callable[['EmailPicker', bool], None], /) -> None:
        """LostFocus()

Event raised when the EmailPicker is no longer selected for input, such
as if the user touches a different text box."""
        raise NotImplementedError

class PhoneCall(Component):
    """A non-visible component that makes a phone call to the number specified in the
PhoneNumber property, which can be set either in the Designer or Blocks Editor.
The component has a MakePhoneCall method, enabling the program to launch a phone call.
You may also use MakePhoneCallDirect to directly initiate a phone call without user
interaction. However, apps using this block may require further review by Google if submitted
to the Play Store so it is advised to use MakePhoneCall instead."""
    __data__ = {'desc': 'A non-visible component that makes a phone call to the number specified in the\nPhoneNumber property, which can be set either in the Designer or Blocks Editor.\nThe component has a MakePhoneCall method, enabling the program to launch a phone call.\nYou may also use MakePhoneCallDirect to directly initiate a phone call without user\ninteraction. However, apps using this block may require further review by Google if submitted\nto the Play Store so it is advised to use MakePhoneCall instead.', 'properties': [{'name': 'PhoneNumber', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the phone number to call.'}], 'events': [{'name': 'IncomingCallAnswered', 'args': [{'name': 'phoneNumber', 'type': 'str'}], 'desc': 'Event indicating that an incoming phone call is answered. phoneNumber is\nthe incoming call phone number.'}, {'name': 'PhoneCallEnded', 'args': [{'name': 'status', 'type': 'int'}, {'name': 'phoneNumber', 'type': 'str'}], 'desc': 'Event indicating that a phone call has ended. The status can be any of:\n\n   \n1: Incoming call was missed or rejected\n2: Incoming call was answered and hung up\n3: Outgoing call was hung up.\n\n'}, {'name': 'PhoneCallStarted', 'args': [{'name': 'status', 'type': 'int'}, {'name': 'phoneNumber', 'type': 'str'}], 'desc': 'Event indicating that a phone call has started. The status can be any of:\n\n   \n1: Incoming call is ringing\n2: Outgoing call is dialled\n\n'}], 'methods': [{'name': 'MakePhoneCall', 'args': [], 'returns': None, 'desc': 'Launches the default dialer app set to start a phone call using the number in the\nPhoneNumber property.'}, {'name': 'MakePhoneCallDirect', 'args': [], 'returns': None, 'desc': 'Directly initiates a phone call using the number in the PhoneNumber property,\nbypassing user interaction to start the call. Most apps should use\nMakePhoneCall instead, which requires no permissions.'}]}

    def __init__(self, /, *, parent: Component=..., PhoneNumber: str=...):
        raise NotImplementedError

    @property
    def PhoneNumber(self) -> str:
        """Specifies the phone number to call."""
        raise NotImplementedError

    @PhoneNumber.setter
    def PhoneNumber(self, value: str, /) -> None:
        raise NotImplementedError

    def MakePhoneCall(self, /) -> None:
        """Launches the default dialer app set to start a phone call using the number in the
PhoneNumber property."""
        raise NotImplementedError

    def MakePhoneCallDirect(self, /) -> None:
        """Directly initiates a phone call using the number in the PhoneNumber property,
bypassing user interaction to start the call. Most apps should use
MakePhoneCall instead, which requires no permissions."""
        raise NotImplementedError

    def on_IncomingCallAnswered(self, callback: Callable[[str], None], /) -> None:
        """IncomingCallAnswered(phoneNumber)

Event indicating that an incoming phone call is answered. phoneNumber is
the incoming call phone number."""
        raise NotImplementedError

    @staticmethod
    def on_any_IncomingCallAnswered(callback: Callable[['PhoneCall', bool, str], None], /) -> None:
        """IncomingCallAnswered(phoneNumber)

Event indicating that an incoming phone call is answered. phoneNumber is
the incoming call phone number."""
        raise NotImplementedError

    def on_PhoneCallEnded(self, callback: Callable[[int, str], None], /) -> None:
        """PhoneCallEnded(status, phoneNumber)

Event indicating that a phone call has ended. The status can be any of:

   
1: Incoming call was missed or rejected
2: Incoming call was answered and hung up
3: Outgoing call was hung up.

"""
        raise NotImplementedError

    @staticmethod
    def on_any_PhoneCallEnded(callback: Callable[['PhoneCall', bool, int, str], None], /) -> None:
        """PhoneCallEnded(status, phoneNumber)

Event indicating that a phone call has ended. The status can be any of:

   
1: Incoming call was missed or rejected
2: Incoming call was answered and hung up
3: Outgoing call was hung up.

"""
        raise NotImplementedError

    def on_PhoneCallStarted(self, callback: Callable[[int, str], None], /) -> None:
        """PhoneCallStarted(status, phoneNumber)

Event indicating that a phone call has started. The status can be any of:

   
1: Incoming call is ringing
2: Outgoing call is dialled

"""
        raise NotImplementedError

    @staticmethod
    def on_any_PhoneCallStarted(callback: Callable[['PhoneCall', bool, int, str], None], /) -> None:
        """PhoneCallStarted(status, phoneNumber)

Event indicating that a phone call has started. The status can be any of:

   
1: Incoming call is ringing
2: Outgoing call is dialled

"""
        raise NotImplementedError

class PhoneNumberPicker(Component):
    """A button that, when clicked on, displays a list of the contacts' phone numbers to choose among.
After the user has made a selection, the following properties will be set to information about
the chosen contact:"""
    __data__ = {'desc': "A button that, when clicked on, displays a list of the contacts' phone numbers to choose among.\nAfter the user has made a selection, the following properties will be set to information about\nthe chosen contact:", 'properties': [{'name': 'BackgroundColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the PhoneNumberPicker's background color as an alpha-red-green-blue\ninteger.  If an Image has been set, the color\nchange will not be visible until the Image is removed."}, {'name': 'ContactName', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the full name of the selected contact, or the empty string if a name is unavailable.'}, {'name': 'ContactUri', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns a URI that specifies the location of the contact on the device.'}, {'name': 'EmailAddress', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the primary email address of the selected contact, or the empty string if an email\naddress is unavailable.'}, {'name': 'EmailAddressList', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns a list of email addresses associated with the selected contact.'}, {'name': 'Enabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the PhoneNumberPicker should be active and clickable.'}, {'name': 'FontBold', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the text of the PhoneNumberPicker should be bold.\nSome fonts do not support bold.'}, {'name': 'FontItalic', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the text of the PhoneNumberPicker should be italic.\nSome fonts do not support italic.'}, {'name': 'FontSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text font size of the PhoneNumberPicker, measured in sp(scale-independent pixels).'}, {'name': 'FontTypeface', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the text font face of the PhoneNumberPicker as default, serif, sans\nserif, monospace, or custom font typeface. To add a custom typeface,\nupload a .ttf file to the project's media."}, {'name': 'Height', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the PhoneNumberPicker's vertical height, measured in pixels."}, {'name': 'HeightPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the PhoneNumberPicker's vertical height as a percentage\nof the Screen's Height."}, {'name': 'Image', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': "Specifies the path of the PhoneNumberPicker's image. If there is both an Image and a\nBackgroundColor specified, only the Image will be visible."}, {'name': 'PhoneNumber', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the primary phone number associated with the selected contact, or the empty string if\nno phone number is associated with the contact.'}, {'name': 'PhoneNumberList', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns a list of phone numbers associated with the selected contact.'}, {'name': 'Picture', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': "Returns a picture URI for the selected contact, which can be\nused to retrieve the contact's photo and other fields."}, {'name': 'Shape', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies the shape of the PhoneNumberPicker. The valid values for this property are 0 (default),\n1 (rounded), 2 (rectangle), and 3 (oval). The Shape will not be visible if an\nImage is used.'}, {'name': 'ShowFeedback', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies if a visual feedback should be shown when a PhoneNumberPicker with an assigned\nImage is pressed.'}, {'name': 'Text', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text displayed by the PhoneNumberPicker.'}, {'name': 'TextAlignment', 'type': 'int', 'ro': False, 'do': True, 'bo': False, 'desc': "Specifies the alignment of the PhoneNumberPicker's text. Valid values are:\n0 (normal; e.g., left-justified if text is written left to right),\n1 (center), or\n2 (opposite; e.g., right-justified if text is written left to right)."}, {'name': 'TextColor', 'type': 'enums.Color', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the text color of the PhoneNumberPicker as an alpha-red-green-blue\ninteger.'}, {'name': 'Visible', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the PhoneNumberPicker should be visible on the screen.  Value is true\nif the PhoneNumberPicker is showing and false if hidden.'}, {'name': 'Width', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the horizontal width of the PhoneNumberPicker, measured in pixels.'}, {'name': 'WidthPercent', 'type': 'int', 'ro': False, 'do': False, 'bo': True, 'desc': "Specifies the horizontal width of the PhoneNumberPicker as a percentage\nof the Screen's Width."}], 'events': [{'name': 'AfterPicking', 'args': [], 'desc': 'Event to be raised after the PhoneNumberPicker activity returns its\nresult and the properties have been filled in.'}, {'name': 'BeforePicking', 'args': [], 'desc': 'Event to raise when the PhoneNumberPicker is clicked or the picker is shown\nusing the Open method.  This event occurs before the picker is displayed, and\ncan be used to prepare the picker before it is shown.'}, {'name': 'GotFocus', 'args': [], 'desc': 'Indicates the cursor moved over the PhoneNumberPicker so it is now possible\nto click it.'}, {'name': 'LostFocus', 'args': [], 'desc': 'Indicates the cursor moved away from the PhoneNumberPicker so it is now no\nlonger possible to click it.'}, {'name': 'TouchDown', 'args': [], 'desc': 'Indicates that the PhoneNumberPicker was pressed down.'}, {'name': 'TouchUp', 'args': [], 'desc': 'Indicates that the PhoneNumberPicker has been released.'}], 'methods': [{'name': 'Open', 'args': [], 'returns': None, 'desc': 'Opens the PhoneNumberPicker, as though the user clicked on it.'}, {'name': 'ViewContact', 'args': [{'name': 'uri', 'type': 'str'}], 'returns': None, 'desc': "Opens the selected contact's entry in the device's default Contacts app."}]}

    def __init__(self, /, *, parent: Component=..., BackgroundColor: enums.Color=..., Enabled: bool=..., FontBold: bool=..., FontItalic: bool=..., FontSize: int=..., FontTypeface: str=..., Height: int=..., Image: str=..., Shape: int=..., ShowFeedback: bool=..., Text: str=..., TextAlignment: int=..., TextColor: enums.Color=..., Visible: bool=..., Width: int=...):
        raise NotImplementedError

    @property
    def BackgroundColor(self) -> enums.Color:
        """Specifies the PhoneNumberPicker's background color as an alpha-red-green-blue
integer.  If an Image has been set, the color
change will not be visible until the Image is removed."""
        raise NotImplementedError

    @BackgroundColor.setter
    def BackgroundColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def ContactName(self) -> str:
        """Returns the full name of the selected contact, or the empty string if a name is unavailable."""
        raise NotImplementedError

    @property
    def ContactUri(self) -> str:
        """Returns a URI that specifies the location of the contact on the device."""
        raise NotImplementedError

    @property
    def EmailAddress(self) -> str:
        """Returns the primary email address of the selected contact, or the empty string if an email
address is unavailable."""
        raise NotImplementedError

    @property
    def EmailAddressList(self) -> list:
        """Returns a list of email addresses associated with the selected contact."""
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Specifies whether the PhoneNumberPicker should be active and clickable."""
        raise NotImplementedError

    @Enabled.setter
    def Enabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontBold(self) -> bool:
        """Specifies whether the text of the PhoneNumberPicker should be bold.
Some fonts do not support bold."""
        raise NotImplementedError

    @FontBold.setter
    def FontBold(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontItalic(self) -> bool:
        """Specifies whether the text of the PhoneNumberPicker should be italic.
Some fonts do not support italic."""
        raise NotImplementedError

    @FontItalic.setter
    def FontItalic(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def FontSize(self) -> int:
        """Specifies the text font size of the PhoneNumberPicker, measured in sp(scale-independent pixels)."""
        raise NotImplementedError

    @FontSize.setter
    def FontSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Height(self) -> int:
        """Specifies the PhoneNumberPicker's vertical height, measured in pixels."""
        raise NotImplementedError

    @Height.setter
    def Height(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def HeightPercent(self) -> int:
        """Specifies the PhoneNumberPicker's vertical height as a percentage
of the Screen's Height."""
        raise NotImplementedError

    @HeightPercent.setter
    def HeightPercent(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Image(self) -> str:
        """Specifies the path of the PhoneNumberPicker's image. If there is both an Image and a
BackgroundColor specified, only the Image will be visible."""
        raise NotImplementedError

    @Image.setter
    def Image(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def PhoneNumber(self) -> str:
        """Returns the primary phone number associated with the selected contact, or the empty string if
no phone number is associated with the contact."""
        raise NotImplementedError

    @property
    def PhoneNumberList(self) -> list:
        """Returns a list of phone numbers associated with the selected contact."""
        raise NotImplementedError

    @property
    def Picture(self) -> str:
        """Returns a picture URI for the selected contact, which can be
used to retrieve the contact's photo and other fields."""
        raise NotImplementedError

    @property
    def ShowFeedback(self) -> bool:
        """Specifies if a visual feedback should be shown when a PhoneNumberPicker with an assigned
Image is pressed."""
        raise NotImplementedError

    @ShowFeedback.setter
    def ShowFeedback(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Text(self) -> str:
        """Specifies the text displayed by the PhoneNumberPicker."""
        raise NotImplementedError

    @Text.setter
    def Text(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def TextColor(self) -> enums.Color:
        """Specifies the text color of the PhoneNumberPicker as an alpha-red-green-blue
integer."""
        raise NotImplementedError

    @TextColor.setter
    def TextColor(self, value: enums.Color, /) -> None:
        raise NotImplementedError

    @property
    def Visible(self) -> bool:
        """Specifies whether the PhoneNumberPicker should be visible on the screen.  Value is true
if the PhoneNumberPicker is showing and false if hidden."""
        raise NotImplementedError

    @Visible.setter
    def Visible(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Width(self) -> int:
        """Specifies the horizontal width of the PhoneNumberPicker, measured in pixels."""
        raise NotImplementedError

    @Width.setter
    def Width(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def WidthPercent(self) -> int:
        """Specifies the horizontal width of the PhoneNumberPicker as a percentage
of the Screen's Width."""
        raise NotImplementedError

    @WidthPercent.setter
    def WidthPercent(self, value: int, /) -> None:
        raise NotImplementedError

    def Open(self, /) -> None:
        """Opens the PhoneNumberPicker, as though the user clicked on it."""
        raise NotImplementedError

    def ViewContact(self, uri: str, /) -> None:
        """Opens the selected contact's entry in the device's default Contacts app."""
        raise NotImplementedError

    def on_AfterPicking(self, callback: Callable[[], None], /) -> None:
        """AfterPicking()

Event to be raised after the PhoneNumberPicker activity returns its
result and the properties have been filled in."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterPicking(callback: Callable[['PhoneNumberPicker', bool], None], /) -> None:
        """AfterPicking()

Event to be raised after the PhoneNumberPicker activity returns its
result and the properties have been filled in."""
        raise NotImplementedError

    def on_BeforePicking(self, callback: Callable[[], None], /) -> None:
        """BeforePicking()

Event to raise when the PhoneNumberPicker is clicked or the picker is shown
using the Open method.  This event occurs before the picker is displayed, and
can be used to prepare the picker before it is shown."""
        raise NotImplementedError

    @staticmethod
    def on_any_BeforePicking(callback: Callable[['PhoneNumberPicker', bool], None], /) -> None:
        """BeforePicking()

Event to raise when the PhoneNumberPicker is clicked or the picker is shown
using the Open method.  This event occurs before the picker is displayed, and
can be used to prepare the picker before it is shown."""
        raise NotImplementedError

    def on_GotFocus(self, callback: Callable[[], None], /) -> None:
        """GotFocus()

Indicates the cursor moved over the PhoneNumberPicker so it is now possible
to click it."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotFocus(callback: Callable[['PhoneNumberPicker', bool], None], /) -> None:
        """GotFocus()

Indicates the cursor moved over the PhoneNumberPicker so it is now possible
to click it."""
        raise NotImplementedError

    def on_LostFocus(self, callback: Callable[[], None], /) -> None:
        """LostFocus()

Indicates the cursor moved away from the PhoneNumberPicker so it is now no
longer possible to click it."""
        raise NotImplementedError

    @staticmethod
    def on_any_LostFocus(callback: Callable[['PhoneNumberPicker', bool], None], /) -> None:
        """LostFocus()

Indicates the cursor moved away from the PhoneNumberPicker so it is now no
longer possible to click it."""
        raise NotImplementedError

    def on_TouchDown(self, callback: Callable[[], None], /) -> None:
        """TouchDown()

Indicates that the PhoneNumberPicker was pressed down."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchDown(callback: Callable[['PhoneNumberPicker', bool], None], /) -> None:
        """TouchDown()

Indicates that the PhoneNumberPicker was pressed down."""
        raise NotImplementedError

    def on_TouchUp(self, callback: Callable[[], None], /) -> None:
        """TouchUp()

Indicates that the PhoneNumberPicker has been released."""
        raise NotImplementedError

    @staticmethod
    def on_any_TouchUp(callback: Callable[['PhoneNumberPicker', bool], None], /) -> None:
        """TouchUp()

Indicates that the PhoneNumberPicker has been released."""
        raise NotImplementedError

class Sharing(Component):
    """Sharing is a non-visible component that enables sharing files and/or messages between your app
and other apps installed on a device. The component will display a list of the installed apps
that can handle the information provided, and will allow the user to choose one to share the
content with, for instance a mail app, a social network app, a texting app, and so on."""
    __data__ = {'desc': 'Sharing is a non-visible component that enables sharing files and/or messages between your app\nand other apps installed on a device. The component will display a list of the installed apps\nthat can handle the information provided, and will allow the user to choose one to share the\ncontent with, for instance a mail app, a social network app, a texting app, and so on.', 'properties': [], 'events': [], 'methods': [{'name': 'ShareFile', 'args': [{'name': 'file', 'type': 'str'}], 'returns': None, 'desc': 'Shares a file through any capable application installed on the phone by displaying a list of the available apps and allowing the user to choose one from the list. The selected app will open with the file inserted on it.'}, {'name': 'ShareFileWithMessage', 'args': [{'name': 'file', 'type': 'str'}, {'name': 'message', 'type': 'str'}], 'returns': None, 'desc': 'Shares both a file and a message through any capable application installed on the phone by displaying a list of available apps and allowing the user to  choose one from the list. The selected app will open with the file and message inserted on it.'}, {'name': 'ShareMessage', 'args': [{'name': 'message', 'type': 'str'}], 'returns': None, 'desc': 'Shares a message through any capable application installed on the phone by displaying a list of the available apps and allowing the user to choose one from the list. The selected app will open with the message inserted on it.'}]}

    def __init__(self, /, *, parent: Component=...):
        raise NotImplementedError

    def ShareFile(self, file: str, /) -> None:
        """Shares a file through any capable application installed on the phone by displaying a list of the available apps and allowing the user to choose one from the list. The selected app will open with the file inserted on it."""
        raise NotImplementedError

    def ShareFileWithMessage(self, file: str, message: str, /) -> None:
        """Shares both a file and a message through any capable application installed on the phone by displaying a list of available apps and allowing the user to  choose one from the list. The selected app will open with the file and message inserted on it."""
        raise NotImplementedError

    def ShareMessage(self, message: str, /) -> None:
        """Shares a message through any capable application installed on the phone by displaying a list of the available apps and allowing the user to choose one from the list. The selected app will open with the message inserted on it."""
        raise NotImplementedError

class Texting(Component):
    """A component that will, when the SendMessage method is called, launch the device's
preferred texting app to send the text message specified in the SendMessage property
to the phone number specified in the PhoneNumber property. You may also send text
messages without user interaction by calling SendMessageDirect instead, but this
adds dangerous permissions to your final app."""
    __data__ = {'desc': "A component that will, when the SendMessage method is called, launch the device's\npreferred texting app to send the text message specified in the SendMessage property\nto the phone number specified in the PhoneNumber property. You may also send text\nmessages without user interaction by calling SendMessageDirect instead, but this\nadds dangerous permissions to your final app.", 'properties': [{'name': 'GoogleVoiceEnabled', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'If this property is true, then SendMessage will attempt to send messages over\nWiFi, using Google voice.'}, {'name': 'Message', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'The message that will be sent when the SendMessage method is called.\nThe maximum length of a standard SMS message is usually 170. It may be less for languages\nusing diacritical marks.'}, {'name': 'PhoneNumber', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'The number that the message will be sent to when the SendMessage method is called.  The \nnumber is a text string with the specified digits (e.g., 6505551212).  Dashes, dots, \nand parentheses may be included (e.g., (650)-555-1212) but will be ignored; spaces\nshould not be included.'}, {'name': 'ReceivingEnabled', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'If set to 1 (OFF) no messages will be received. If set to 2 (FOREGROUND) or 3 (ALWAYS) the\ncomponent will respond to messages if it is running. In the case of 2 (FOREGROUND), messages\nreceived while the app is not running are discarded. In the case of 3 (ALWAYS), messages\nreceive while the app is not running will show a notification. Selecting the notification\nwill bring up the app and signal the MessageReceived event. Messages\nreceived when the app is dormant will be queued, and so several\nMessageReceived events might appear when the app awakens. As an app\ndeveloper, it would be a good idea to give your users control over this property, so they can\nmake their phones ignore text messages when your app is installed.'}], 'events': [{'name': 'MessageReceived', 'args': [{'name': 'number', 'type': 'str'}, {'name': 'messageText', 'type': 'str'}], 'desc': "Event that's raised when a text message is received by the phone. Using this block will add\ndangerous permissions\nthat will require additional approval if your app is submitted to the Google Play Store."}], 'methods': [{'name': 'SendMessage', 'args': [], 'returns': None, 'desc': "Launch the phone's default text messaging app with the message and phone number prepopulated."}, {'name': 'SendMessageDirect', 'args': [], 'returns': None, 'desc': 'Send a text message. Using this block will add\ndangerous permissions\nthat will require additional approval if your app is submitted to the Google Play Store.'}]}

    def __init__(self, /, *, parent: Component=..., GoogleVoiceEnabled: bool=..., Message: str=..., PhoneNumber: str=..., ReceivingEnabled: int=...):
        raise NotImplementedError

    @property
    def GoogleVoiceEnabled(self) -> bool:
        """If this property is true, then SendMessage will attempt to send messages over
WiFi, using Google voice."""
        raise NotImplementedError

    @GoogleVoiceEnabled.setter
    def GoogleVoiceEnabled(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Message(self) -> str:
        """The message that will be sent when the SendMessage method is called.
The maximum length of a standard SMS message is usually 170. It may be less for languages
using diacritical marks."""
        raise NotImplementedError

    @Message.setter
    def Message(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def PhoneNumber(self) -> str:
        """The number that the message will be sent to when the SendMessage method is called.  The 
number is a text string with the specified digits (e.g., 6505551212).  Dashes, dots, 
and parentheses may be included (e.g., (650)-555-1212) but will be ignored; spaces
should not be included."""
        raise NotImplementedError

    @PhoneNumber.setter
    def PhoneNumber(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def ReceivingEnabled(self) -> int:
        """If set to 1 (OFF) no messages will be received. If set to 2 (FOREGROUND) or 3 (ALWAYS) the
component will respond to messages if it is running. In the case of 2 (FOREGROUND), messages
received while the app is not running are discarded. In the case of 3 (ALWAYS), messages
receive while the app is not running will show a notification. Selecting the notification
will bring up the app and signal the MessageReceived event. Messages
received when the app is dormant will be queued, and so several
MessageReceived events might appear when the app awakens. As an app
developer, it would be a good idea to give your users control over this property, so they can
make their phones ignore text messages when your app is installed."""
        raise NotImplementedError

    @ReceivingEnabled.setter
    def ReceivingEnabled(self, value: int, /) -> None:
        raise NotImplementedError

    def SendMessage(self, /) -> None:
        """Launch the phone's default text messaging app with the message and phone number prepopulated."""
        raise NotImplementedError

    def SendMessageDirect(self, /) -> None:
        """Send a text message. Using this block will add
dangerous permissions
that will require additional approval if your app is submitted to the Google Play Store."""
        raise NotImplementedError

    def on_MessageReceived(self, callback: Callable[[str, str], None], /) -> None:
        """MessageReceived(number, messageText)

Event that's raised when a text message is received by the phone. Using this block will add
dangerous permissions
that will require additional approval if your app is submitted to the Google Play Store."""
        raise NotImplementedError

    @staticmethod
    def on_any_MessageReceived(callback: Callable[['Texting', bool, str, str], None], /) -> None:
        """MessageReceived(number, messageText)

Event that's raised when a text message is received by the phone. Using this block will add
dangerous permissions
that will require additional approval if your app is submitted to the Google Play Store."""
        raise NotImplementedError

class Twitter(Component):
    """A non-visible component that enables communication with Twitter. Once a
user has logged into their Twitter account (and the authorization has been confirmed successful
by the IsAuthorized event), many more operations are available:"""
    __data__ = {'desc': 'A non-visible component that enables communication with Twitter. Once a\nuser has logged into their Twitter account (and the authorization has been confirmed successful\nby the IsAuthorized event), many more operations are available:', 'properties': [{'name': 'ConsumerKey', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'The consumer key to be used when authorizing with Twitter via OAuth.'}, {'name': 'ConsumerSecret', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'The consumer secret to be used when authorizing with Twitter via OAuth.'}, {'name': 'DirectMessages', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': 'This property contains a list of the most recent messages mentioning the logged-in user.\nInitially, the list is empty. To set it, the program must:\n\n   \nCall the Authorize method.\nWait for the IsAuthorized event.\nCall the RequestDirectMessages method.\n4, Wait for the DirectMessagesReceived event.\n\nThe value of this property will then be set to the list of direct messages retrieved (and\nmaintain that value until any subsequent call to RequestDirectMessages).\n'}, {'name': 'Followers', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': 'This property contains a list of the followers of the logged-in user. Initially, the list is\nempty. To set it, the program must:\n\n   \nCall the Authorize method.\nWait for the IsAuthorized event.\nCall the RequestFollowers method.\nWait for the FollowersReceived event.\n\nThe value of this property will then be set to the list of followers (and maintain its value\nuntil any subsequent call to RequestFollowers).\n'}, {'name': 'FriendTimeline', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': 'This property contains the 20 most recent messages of users being followed. Initially, the\nlist is empty. To set it, the program must:\n\n   \nCall the Authorize method.\nWait for the IsAuthorized event.\nSpecify users to follow with one or more calls to the Follow method.\nCall the RequestFriendTimeline  method.\nWait for the FriendTimelineReceived event.\n\nThe value of this property will then be set to the list of messages (and maintain its value\nuntil any subsequent call to RequestFriendTimeline.\n'}, {'name': 'Mentions', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': 'This property contains a list of mentions of the logged-in user. Initially, the list is empty.\nTo set it, the program must:\n\n   \nCall the Authorize method.\nWait for the IsAuthorized event.\nCall the RequestMentions method.\nWait for the MentionsReceived event.\n\nThe value of this property will then be set to the list of mentions (and will maintain its\nvalue until any subsequent calls to RequestMentions).\n'}, {'name': 'SearchResults', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': 'This property, which is initially empty, is set to a list of search results after the program:\n\n   \nCalls the SearchTwitter method.\nWaits for the SearchSuccessful event.\n\nThe value of the property will then be the same as the parameter to\nSearchSuccessful. Note that it is not necessary to call the Authorize\nmethod before calling SearchTwitter.\n'}, {'name': 'Username', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'The user name of the authorized user. Empty if there is no authorized user.'}], 'events': [{'name': 'DirectMessagesReceived', 'args': [{'name': 'messages', 'type': 'list'}], 'desc': 'This event is raised when the recent messages requested through\nRequestDirectMessages have been retrieved. A list of the messages can then be found\nin the messages parameter or the DirectMessages property.'}, {'name': 'FollowersReceived', 'args': [{'name': 'followers2', 'type': 'list'}], 'desc': 'This event is raised when all of the followers of the logged-in user requested through\nRequestFollowers have been retrieved. A list of the followers can then be found in\nthe followers parameter or the Followers property.'}, {'name': 'FriendTimelineReceived', 'args': [{'name': 'timeline', 'type': 'list'}], 'desc': 'This event is raised when the messages requested through RequestFriendTimeline have\nbeen retrieved. The timeline parameter and the FriendTimeline\nproperty will contain a list of lists, where each sub-list contains a status update of the\nform (username message).'}, {'name': 'IsAuthorized', 'args': [], 'desc': 'This event is raised after the program calls Authorize if the authorization was\nsuccessful. It is also called after a call to CheckAuthorized if we already have a\nvalid access token. After this event has been raised, any other method for this component can\nbe called.'}, {'name': 'MentionsReceived', 'args': [{'name': 'mentions', 'type': 'list'}], 'desc': 'This event is raised when the mentions of the logged-in user requested through\nRequestMentions have been retrieved. A list of the mentions can then be found in\nthe mentions parameter or the Mentions property.'}, {'name': 'SearchSuccessful', 'args': [{'name': 'searchResults', 'type': 'list'}], 'desc': 'This event is raised when the results of the search requested through\nSearchTwitter have been retrieved. A list of the results can then be found in\nthe results parameter or the SearchResults property.'}], 'methods': [{'name': 'Authorize', 'args': [], 'returns': None, 'desc': "Redirects user to login to Twitter via the Web browser using the OAuth protocol if we don't already have authorization."}, {'name': 'CheckAuthorized', 'args': [], 'returns': None, 'desc': 'Check whether we already have access, and if so, causes the IsAuthorized event\nhandler to be called.'}, {'name': 'DeAuthorize', 'args': [], 'returns': None, 'desc': 'Removes Twitter authorization from this running app instance.'}, {'name': 'DirectMessage', 'args': [{'name': 'user', 'type': 'str'}, {'name': 'message', 'type': 'str'}], 'returns': None, 'desc': 'This sends a direct (private) message to the specified user. The message will be trimmed if it\nexceeds 160 characters.\n\n   Requirements: This should only be called after the IsAuthorized event has\nbeen raised, indicating that the user has successfully logged in to Twitter.\n'}, {'name': 'Follow', 'args': [{'name': 'user', 'type': 'str'}], 'returns': None, 'desc': 'Starts following a user.'}, {'name': 'RequestDirectMessages', 'args': [], 'returns': None, 'desc': 'Requests the 20 most recent direct messages sent to the logged-in user. When the messages have\nbeen retrieved, the system will raise the DirectMessagesReceived event and set\nthe DirectMessages property to the list of messages.\n\n   Requirements: This should only be called after the IsAuthorized event has\nbeen raised, indicating that the user has successfully logged in to Twitter.\n'}, {'name': 'RequestFollowers', 'args': [], 'returns': None, 'desc': 'Gets who is following you.'}, {'name': 'RequestFriendTimeline', 'args': [], 'returns': None, 'desc': "Gets the most recent 20 messages in the user's timeline."}, {'name': 'RequestMentions', 'args': [], 'returns': None, 'desc': 'Requests the 20 most recent mentions of the logged-in user. When the mentions have been\nretrieved, the system will raise the MentionsReceived event and set the\nMentions property to the list of mentions.\n\n   Requirements: This should only be called after the IsAuthorized event has\nbeen raised, indicating that the user has successfully logged in to Twitter.\n'}, {'name': 'SearchTwitter', 'args': [{'name': 'query', 'type': 'str'}], 'returns': None, 'desc': 'This searches Twitter for the given String query.\n\n   Requirements: This should only be called after the IsAuthorized event has\nbeen raised, indicating that the user has successfully logged in to Twitter.\n'}, {'name': 'StopFollowing', 'args': [{'name': 'user', 'type': 'str'}], 'returns': None, 'desc': 'Stops following a user.'}, {'name': 'Tweet', 'args': [{'name': 'status', 'type': 'str'}], 'returns': None, 'desc': 'This sends a tweet as the logged-in user with the specified Text, which will be trimmed if it\nexceeds 160 characters.\n\n   Requirements: This should only be called after the IsAuthorized event has\nbeen raised, indicating that the user has successfully logged in to Twitter.\n'}, {'name': 'TweetWithImage', 'args': [{'name': 'status', 'type': 'str'}, {'name': 'imagePath', 'type': 'str'}], 'returns': None, 'desc': 'This sends a tweet as the logged-in user with the specified Text and a path to the image to be\nuploaded, which will be trimmed if it exceeds 160 characters. If an image is not found or\ninvalid, the update will not be sent.\n\n   Requirements: This should only be called after the IsAuthorized event has\nbeen raised, indicating that the user has successfully logged in to Twitter.\n'}]}

    def __init__(self, /, *, parent: Component=..., ConsumerKey: str=..., ConsumerSecret: str=...):
        raise NotImplementedError

    @property
    def ConsumerKey(self) -> str:
        """The consumer key to be used when authorizing with Twitter via OAuth."""
        raise NotImplementedError

    @ConsumerKey.setter
    def ConsumerKey(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def ConsumerSecret(self) -> str:
        """The consumer secret to be used when authorizing with Twitter via OAuth."""
        raise NotImplementedError

    @ConsumerSecret.setter
    def ConsumerSecret(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def DirectMessages(self) -> list:
        """This property contains a list of the most recent messages mentioning the logged-in user.
Initially, the list is empty. To set it, the program must:

   
Call the Authorize method.
Wait for the IsAuthorized event.
Call the RequestDirectMessages method.
4, Wait for the DirectMessagesReceived event.

The value of this property will then be set to the list of direct messages retrieved (and
maintain that value until any subsequent call to RequestDirectMessages).
"""
        raise NotImplementedError

    @property
    def Followers(self) -> list:
        """This property contains a list of the followers of the logged-in user. Initially, the list is
empty. To set it, the program must:

   
Call the Authorize method.
Wait for the IsAuthorized event.
Call the RequestFollowers method.
Wait for the FollowersReceived event.

The value of this property will then be set to the list of followers (and maintain its value
until any subsequent call to RequestFollowers).
"""
        raise NotImplementedError

    @property
    def FriendTimeline(self) -> list:
        """This property contains the 20 most recent messages of users being followed. Initially, the
list is empty. To set it, the program must:

   
Call the Authorize method.
Wait for the IsAuthorized event.
Specify users to follow with one or more calls to the Follow method.
Call the RequestFriendTimeline  method.
Wait for the FriendTimelineReceived event.

The value of this property will then be set to the list of messages (and maintain its value
until any subsequent call to RequestFriendTimeline.
"""
        raise NotImplementedError

    @property
    def Mentions(self) -> list:
        """This property contains a list of mentions of the logged-in user. Initially, the list is empty.
To set it, the program must:

   
Call the Authorize method.
Wait for the IsAuthorized event.
Call the RequestMentions method.
Wait for the MentionsReceived event.

The value of this property will then be set to the list of mentions (and will maintain its
value until any subsequent calls to RequestMentions).
"""
        raise NotImplementedError

    @property
    def SearchResults(self) -> list:
        """This property, which is initially empty, is set to a list of search results after the program:

   
Calls the SearchTwitter method.
Waits for the SearchSuccessful event.

The value of the property will then be the same as the parameter to
SearchSuccessful. Note that it is not necessary to call the Authorize
method before calling SearchTwitter.
"""
        raise NotImplementedError

    @property
    def Username(self) -> str:
        """The user name of the authorized user. Empty if there is no authorized user."""
        raise NotImplementedError

    def Authorize(self, /) -> None:
        """Redirects user to login to Twitter via the Web browser using the OAuth protocol if we don't already have authorization."""
        raise NotImplementedError

    def CheckAuthorized(self, /) -> None:
        """Check whether we already have access, and if so, causes the IsAuthorized event
handler to be called."""
        raise NotImplementedError

    def DeAuthorize(self, /) -> None:
        """Removes Twitter authorization from this running app instance."""
        raise NotImplementedError

    def DirectMessage(self, user: str, message: str, /) -> None:
        """This sends a direct (private) message to the specified user. The message will be trimmed if it
exceeds 160 characters.

   Requirements: This should only be called after the IsAuthorized event has
been raised, indicating that the user has successfully logged in to Twitter.
"""
        raise NotImplementedError

    def Follow(self, user: str, /) -> None:
        """Starts following a user."""
        raise NotImplementedError

    def RequestDirectMessages(self, /) -> None:
        """Requests the 20 most recent direct messages sent to the logged-in user. When the messages have
been retrieved, the system will raise the DirectMessagesReceived event and set
the DirectMessages property to the list of messages.

   Requirements: This should only be called after the IsAuthorized event has
been raised, indicating that the user has successfully logged in to Twitter.
"""
        raise NotImplementedError

    def RequestFollowers(self, /) -> None:
        """Gets who is following you."""
        raise NotImplementedError

    def RequestFriendTimeline(self, /) -> None:
        """Gets the most recent 20 messages in the user's timeline."""
        raise NotImplementedError

    def RequestMentions(self, /) -> None:
        """Requests the 20 most recent mentions of the logged-in user. When the mentions have been
retrieved, the system will raise the MentionsReceived event and set the
Mentions property to the list of mentions.

   Requirements: This should only be called after the IsAuthorized event has
been raised, indicating that the user has successfully logged in to Twitter.
"""
        raise NotImplementedError

    def SearchTwitter(self, query: str, /) -> None:
        """This searches Twitter for the given String query.

   Requirements: This should only be called after the IsAuthorized event has
been raised, indicating that the user has successfully logged in to Twitter.
"""
        raise NotImplementedError

    def StopFollowing(self, user: str, /) -> None:
        """Stops following a user."""
        raise NotImplementedError

    def Tweet(self, status: str, /) -> None:
        """This sends a tweet as the logged-in user with the specified Text, which will be trimmed if it
exceeds 160 characters.

   Requirements: This should only be called after the IsAuthorized event has
been raised, indicating that the user has successfully logged in to Twitter.
"""
        raise NotImplementedError

    def TweetWithImage(self, status: str, imagePath: str, /) -> None:
        """This sends a tweet as the logged-in user with the specified Text and a path to the image to be
uploaded, which will be trimmed if it exceeds 160 characters. If an image is not found or
invalid, the update will not be sent.

   Requirements: This should only be called after the IsAuthorized event has
been raised, indicating that the user has successfully logged in to Twitter.
"""
        raise NotImplementedError

    def on_DirectMessagesReceived(self, callback: Callable[[list], None], /) -> None:
        """DirectMessagesReceived(messages)

This event is raised when the recent messages requested through
RequestDirectMessages have been retrieved. A list of the messages can then be found
in the messages parameter or the DirectMessages property."""
        raise NotImplementedError

    @staticmethod
    def on_any_DirectMessagesReceived(callback: Callable[['Twitter', bool, list], None], /) -> None:
        """DirectMessagesReceived(messages)

This event is raised when the recent messages requested through
RequestDirectMessages have been retrieved. A list of the messages can then be found
in the messages parameter or the DirectMessages property."""
        raise NotImplementedError

    def on_FollowersReceived(self, callback: Callable[[list], None], /) -> None:
        """FollowersReceived(followers2)

This event is raised when all of the followers of the logged-in user requested through
RequestFollowers have been retrieved. A list of the followers can then be found in
the followers parameter or the Followers property."""
        raise NotImplementedError

    @staticmethod
    def on_any_FollowersReceived(callback: Callable[['Twitter', bool, list], None], /) -> None:
        """FollowersReceived(followers2)

This event is raised when all of the followers of the logged-in user requested through
RequestFollowers have been retrieved. A list of the followers can then be found in
the followers parameter or the Followers property."""
        raise NotImplementedError

    def on_FriendTimelineReceived(self, callback: Callable[[list], None], /) -> None:
        """FriendTimelineReceived(timeline)

This event is raised when the messages requested through RequestFriendTimeline have
been retrieved. The timeline parameter and the FriendTimeline
property will contain a list of lists, where each sub-list contains a status update of the
form (username message)."""
        raise NotImplementedError

    @staticmethod
    def on_any_FriendTimelineReceived(callback: Callable[['Twitter', bool, list], None], /) -> None:
        """FriendTimelineReceived(timeline)

This event is raised when the messages requested through RequestFriendTimeline have
been retrieved. The timeline parameter and the FriendTimeline
property will contain a list of lists, where each sub-list contains a status update of the
form (username message)."""
        raise NotImplementedError

    def on_IsAuthorized(self, callback: Callable[[], None], /) -> None:
        """IsAuthorized()

This event is raised after the program calls Authorize if the authorization was
successful. It is also called after a call to CheckAuthorized if we already have a
valid access token. After this event has been raised, any other method for this component can
be called."""
        raise NotImplementedError

    @staticmethod
    def on_any_IsAuthorized(callback: Callable[['Twitter', bool], None], /) -> None:
        """IsAuthorized()

This event is raised after the program calls Authorize if the authorization was
successful. It is also called after a call to CheckAuthorized if we already have a
valid access token. After this event has been raised, any other method for this component can
be called."""
        raise NotImplementedError

    def on_MentionsReceived(self, callback: Callable[[list], None], /) -> None:
        """MentionsReceived(mentions)

This event is raised when the mentions of the logged-in user requested through
RequestMentions have been retrieved. A list of the mentions can then be found in
the mentions parameter or the Mentions property."""
        raise NotImplementedError

    @staticmethod
    def on_any_MentionsReceived(callback: Callable[['Twitter', bool, list], None], /) -> None:
        """MentionsReceived(mentions)

This event is raised when the mentions of the logged-in user requested through
RequestMentions have been retrieved. A list of the mentions can then be found in
the mentions parameter or the Mentions property."""
        raise NotImplementedError

    def on_SearchSuccessful(self, callback: Callable[[list], None], /) -> None:
        """SearchSuccessful(searchResults)

This event is raised when the results of the search requested through
SearchTwitter have been retrieved. A list of the results can then be found in
the results parameter or the SearchResults property."""
        raise NotImplementedError

    @staticmethod
    def on_any_SearchSuccessful(callback: Callable[['Twitter', bool, list], None], /) -> None:
        """SearchSuccessful(searchResults)

This event is raised when the results of the search requested through
SearchTwitter have been retrieved. A list of the results can then be found in
the results parameter or the SearchResults property."""
        raise NotImplementedError

class CloudDB(Component):
    """The CloudDB component is a Non-visible component that allows you to store data on a Internet
connected database server (using Redis software). This allows the users of your App to share
data with each other. By default data will be stored in a server maintained by MIT, however you
can setup and run your own server. Set the RedisServer property and
RedisPort property to access your own server."""
    __data__ = {'desc': 'The CloudDB component is a Non-visible component that allows you to store data on a Internet\nconnected database server (using Redis software). This allows the users of your App to share\ndata with each other. By default data will be stored in a server maintained by MIT, however you\ncan setup and run your own server. Set the RedisServer property and\nRedisPort property to access your own server.', 'properties': [{'name': 'ProjectID', 'type': 'str', 'ro': True, 'do': False, 'bo': False, 'desc': 'Gets the ProjectID for this CloudDB project.'}, {'name': 'RedisPort', 'type': 'int', 'ro': True, 'do': False, 'bo': False, 'desc': 'The Redis Server port to use. Defaults to 6381'}, {'name': 'RedisServer', 'type': 'str', 'ro': True, 'do': False, 'bo': False, 'desc': 'The Redis Server to use to store data. A setting of "DEFAULT" means that the MIT server will be used.'}, {'name': 'Token', 'type': 'str', 'ro': True, 'do': True, 'bo': False, 'desc': 'This field contains the authentication token used to login to the backed Redis server. For the\n"DEFAULT" server, do not edit this value, the system will fill it in for you. A system\nadministrator may also provide a special value to you which can be used to share data between\nmultiple projects from multiple people. If using your own Redis server, set a password in the\nserver\'s config and enter it here.'}, {'name': 'UseSSL', 'type': 'bool', 'ro': True, 'do': True, 'bo': False, 'desc': 'Set to true to use SSL to talk to CloudDB/Redis server. This should be set to True for the "DEFAULT" server.'}], 'events': [{'name': 'CloudDBError', 'args': [{'name': 'message', 'type': 'str'}], 'desc': 'Indicates that an error occurred while communicating with the CloudDB Redis server.'}, {'name': 'DataChanged', 'args': [{'name': 'tag', 'type': 'str'}, {'name': 'value', 'type': 'Any'}], 'desc': 'Indicates that the data in the CloudDB project has changed. Launches an event with the\ntag that has been updated and the value it now has.'}, {'name': 'FirstRemoved', 'args': [{'name': 'value', 'type': 'Any'}], 'desc': 'Event triggered by the RemoveFirstFromList function. The argument\nvalue is the object that was the first in the list, and which is now\nremoved.'}, {'name': 'GotValue', 'args': [{'name': 'tag', 'type': 'str'}, {'name': 'value', 'type': 'Any'}], 'desc': 'Indicates that a GetValue request has succeeded.'}, {'name': 'TagList', 'args': [{'name': 'value', 'type': 'list'}], 'desc': 'Event triggered when we have received the list of known tags. Run in response to a call to the\nGetTagList function.'}, {'name': 'UpdateDone', 'args': [{'name': 'tag', 'type': 'str'}, {'name': 'operation', 'type': 'str'}], 'desc': 'Indicates that operations that store data to CloudDB have completed.'}], 'methods': [{'name': 'AppendValueToList', 'args': [{'name': 'tag', 'type': 'str'}, {'name': 'itemToAdd', 'type': 'Any'}], 'returns': None, 'desc': 'Append a value to the end of a list atomically. If two devices use this function simultaneously, both will be appended and no data lost.'}, {'name': 'ClearTag', 'args': [{'name': 'tag', 'type': 'str'}], 'returns': None, 'desc': 'Remove the tag from CloudDB.'}, {'name': 'CloudConnected', 'args': [], 'returns': 'bool', 'desc': 'Returns true if we are on the network and will likely be able to connect to\nthe CloudDB server.'}, {'name': 'GetTagList', 'args': [], 'returns': None, 'desc': 'Asks CloudDB to retrieve all the tags belonging to this project. The\nresulting list is returned in the event TagList.'}, {'name': 'GetValue', 'args': [{'name': 'tag', 'type': 'str'}, {'name': 'valueIfTagNotThere', 'type': 'Any'}], 'returns': None, 'desc': 'GetValue asks CloudDB to get the value stored under the given tag.\nIt will pass the result to the GotValue will be given.'}, {'name': 'RemoveFirstFromList', 'args': [{'name': 'tag', 'type': 'str'}], 'returns': None, 'desc': 'Obtain the first element of a list and atomically remove it. If two devices use this function\nsimultaneously, one will get the first element and the the other will get the second element,\nor an error if there is no available element. When the element is available, the\nFirstRemoved event will be triggered.'}, {'name': 'StoreValue', 'args': [{'name': 'tag', 'type': 'str'}, {'name': 'valueToStore', 'type': 'Any'}], 'returns': None, 'desc': 'Asks CloudDB to store the given value under the given\ntag.'}]}

    def __init__(self, /, *, parent: Component=..., ProjectID: str=..., RedisPort: int=..., RedisServer: str=..., Token: str=..., UseSSL: bool=...):
        raise NotImplementedError

    @property
    def ProjectID(self) -> str:
        """Gets the ProjectID for this CloudDB project."""
        raise NotImplementedError

    @property
    def RedisPort(self) -> int:
        """The Redis Server port to use. Defaults to 6381"""
        raise NotImplementedError

    @property
    def RedisServer(self) -> str:
        """The Redis Server to use to store data. A setting of "DEFAULT" means that the MIT server will be used."""
        raise NotImplementedError

    def AppendValueToList(self, tag: str, itemToAdd: Any, /) -> None:
        """Append a value to the end of a list atomically. If two devices use this function simultaneously, both will be appended and no data lost."""
        raise NotImplementedError

    def ClearTag(self, tag: str, /) -> None:
        """Remove the tag from CloudDB."""
        raise NotImplementedError

    def CloudConnected(self, /) -> bool:
        """Returns true if we are on the network and will likely be able to connect to
the CloudDB server."""
        raise NotImplementedError

    def GetTagList(self, /) -> None:
        """Asks CloudDB to retrieve all the tags belonging to this project. The
resulting list is returned in the event TagList."""
        raise NotImplementedError

    def GetValue(self, tag: str, valueIfTagNotThere: Any, /) -> None:
        """GetValue asks CloudDB to get the value stored under the given tag.
It will pass the result to the GotValue will be given."""
        raise NotImplementedError

    def RemoveFirstFromList(self, tag: str, /) -> None:
        """Obtain the first element of a list and atomically remove it. If two devices use this function
simultaneously, one will get the first element and the the other will get the second element,
or an error if there is no available element. When the element is available, the
FirstRemoved event will be triggered."""
        raise NotImplementedError

    def StoreValue(self, tag: str, valueToStore: Any, /) -> None:
        """Asks CloudDB to store the given value under the given
tag."""
        raise NotImplementedError

    def on_CloudDBError(self, callback: Callable[[str], None], /) -> None:
        """CloudDBError(message)

Indicates that an error occurred while communicating with the CloudDB Redis server."""
        raise NotImplementedError

    @staticmethod
    def on_any_CloudDBError(callback: Callable[['CloudDB', bool, str], None], /) -> None:
        """CloudDBError(message)

Indicates that an error occurred while communicating with the CloudDB Redis server."""
        raise NotImplementedError

    def on_DataChanged(self, callback: Callable[[str, Any], None], /) -> None:
        """DataChanged(tag, value)

Indicates that the data in the CloudDB project has changed. Launches an event with the
tag that has been updated and the value it now has."""
        raise NotImplementedError

    @staticmethod
    def on_any_DataChanged(callback: Callable[['CloudDB', bool, str, Any], None], /) -> None:
        """DataChanged(tag, value)

Indicates that the data in the CloudDB project has changed. Launches an event with the
tag that has been updated and the value it now has."""
        raise NotImplementedError

    def on_FirstRemoved(self, callback: Callable[[Any], None], /) -> None:
        """FirstRemoved(value)

Event triggered by the RemoveFirstFromList function. The argument
value is the object that was the first in the list, and which is now
removed."""
        raise NotImplementedError

    @staticmethod
    def on_any_FirstRemoved(callback: Callable[['CloudDB', bool, Any], None], /) -> None:
        """FirstRemoved(value)

Event triggered by the RemoveFirstFromList function. The argument
value is the object that was the first in the list, and which is now
removed."""
        raise NotImplementedError

    def on_GotValue(self, callback: Callable[[str, Any], None], /) -> None:
        """GotValue(tag, value)

Indicates that a GetValue request has succeeded."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotValue(callback: Callable[['CloudDB', bool, str, Any], None], /) -> None:
        """GotValue(tag, value)

Indicates that a GetValue request has succeeded."""
        raise NotImplementedError

    def on_TagList(self, callback: Callable[[list], None], /) -> None:
        """TagList(value)

Event triggered when we have received the list of known tags. Run in response to a call to the
GetTagList function."""
        raise NotImplementedError

    @staticmethod
    def on_any_TagList(callback: Callable[['CloudDB', bool, list], None], /) -> None:
        """TagList(value)

Event triggered when we have received the list of known tags. Run in response to a call to the
GetTagList function."""
        raise NotImplementedError

    def on_UpdateDone(self, callback: Callable[[str, str], None], /) -> None:
        """UpdateDone(tag, operation)

Indicates that operations that store data to CloudDB have completed."""
        raise NotImplementedError

    @staticmethod
    def on_any_UpdateDone(callback: Callable[['CloudDB', bool, str, str], None], /) -> None:
        """UpdateDone(tag, operation)

Indicates that operations that store data to CloudDB have completed."""
        raise NotImplementedError

class DataFile(Component):
    """Component for DataFile"""
    __data__ = {'desc': 'Component for DataFile', 'properties': [{'name': 'ColumnNames', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': 'Retrieve the column names of the currently loaded Source file.\nFor CSV files, this will return a List of entries in the first row.\nFor JSON files, this will return a List of keys in the JSON object.'}, {'name': 'Columns', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': 'Retrieve a List of columns of the currently loaded Source file.'}, {'name': 'DefaultScope', 'type': 'enums.FileScope', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies the default scope for files accessed using the File component. The App scope should\nwork for most apps. Legacy mode can be used for apps that predate the newer constraints in\nAndroid on app file access.'}, {'name': 'Rows', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': 'Retrieve a List of rows of the currently loaded Source file.'}, {'name': 'SourceFile', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'Sets the source file to parse data from, and then parses the\nfile asynchronously. The results are stored in the Columns,\nRows and ColumnNames properties.\nThe expected formatting of the file is either the CSV or JSON format.'}], 'events': [], 'methods': [{'name': 'ReadFile', 'args': [{'name': 'fileName', 'type': 'str'}], 'returns': None, 'desc': "Indicates source file to load data from. The expected format of the contents of the file\nare either CSV or JSON. Prefix the fileName with / to read from a\nspecific file on the SD card (for example, /myFile.txt will read the file\n/sdcard/myFile.txt). To read assets packaged with an application (also works for the\nCompanion) start the fileName with // (two slashes). If a\nfileName does not start with a slash, it will be read from the application's\nprivate storage (for packaged apps) and from /sdcard/AppInventor/data for the Companion."}]}

    def __init__(self, /, *, parent: Component=..., DefaultScope: enums.FileScope=..., SourceFile: str=...):
        raise NotImplementedError

    @property
    def ColumnNames(self) -> list:
        """Retrieve the column names of the currently loaded Source file.
For CSV files, this will return a List of entries in the first row.
For JSON files, this will return a List of keys in the JSON object."""
        raise NotImplementedError

    @property
    def Columns(self) -> list:
        """Retrieve a List of columns of the currently loaded Source file."""
        raise NotImplementedError

    @property
    def Rows(self) -> list:
        """Retrieve a List of rows of the currently loaded Source file."""
        raise NotImplementedError

    def ReadFile(self, fileName: str, /) -> None:
        """Indicates source file to load data from. The expected format of the contents of the file
are either CSV or JSON. Prefix the fileName with / to read from a
specific file on the SD card (for example, /myFile.txt will read the file
/sdcard/myFile.txt). To read assets packaged with an application (also works for the
Companion) start the fileName with // (two slashes). If a
fileName does not start with a slash, it will be read from the application's
private storage (for packaged apps) and from /sdcard/AppInventor/data for the Companion."""
        raise NotImplementedError

class File(Component):
    """Non-visible component for storing and retrieving files. Use this component to write or read files
on the device."""
    __data__ = {'desc': 'Non-visible component for storing and retrieving files. Use this component to write or read files\non the device.', 'properties': [{'name': 'DefaultScope', 'type': 'enums.FileScope', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies the default scope for files accessed using the File component. The App scope should\nwork for most apps. Legacy mode can be used for apps that predate the newer constraints in\nAndroid on app file access.'}, {'name': 'ReadPermission', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'A designer-only property that can be used to enable read access to file storage outside of the\napp-specific directories.'}, {'name': 'Scope', 'type': 'enums.FileScope', 'ro': False, 'do': False, 'bo': True, 'desc': 'Indicates the current scope for operations such as ReadFrom and SaveFile.'}, {'name': 'WritePermission', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'A designer-only property that can be used to enable write access to file storage outside of the\napp-specific directories.'}], 'events': [{'name': 'AfterFileSaved', 'args': [{'name': 'fileName', 'type': 'str'}], 'desc': 'Event indicating that the contents of the file have been written.'}, {'name': 'GotText', 'args': [{'name': 'text', 'type': 'str'}], 'desc': 'Event indicating that the contents from the file have been read.'}], 'methods': [{'name': 'AppendToFile', 'args': [{'name': 'text', 'type': 'str'}, {'name': 'fileName', 'type': 'str'}], 'returns': None, 'desc': 'Appends text to the end of a file. Creates the file if it does not already exist. See the help\ntext under SaveFile for information about where files are written.\nOn success, the AfterFileSaved event will run.'}, {'name': 'CopyFile', 'args': [{'name': 'fromScope', 'type': 'enums.FileScope'}, {'name': 'fromFileName', 'type': 'str'}, {'name': 'toScope', 'type': 'enums.FileScope'}, {'name': 'toFileName', 'type': 'str'}], 'returns': 'bool', 'desc': 'Copy the contents from the first file to the second file.'}, {'name': 'Delete', 'args': [{'name': 'fileName', 'type': 'str'}], 'returns': None, 'desc': "Deletes a file from storage. Prefix the fileName with / to delete a specific\nfile in the SD card (for example, /myFile.txt will delete the file /sdcard/myFile.txt).\nIf the fileName does not begin with a /, then the file located in the\nprogram's private storage will be deleted. Starting the fileName with // is\nan error because asset files cannot be deleted."}, {'name': 'Exists', 'args': [{'name': 'scope', 'type': 'enums.FileScope'}, {'name': 'path', 'type': 'str'}], 'returns': 'bool', 'desc': 'Tests whether the path exists in the given scope.'}, {'name': 'IsDirectory', 'args': [{'name': 'scope', 'type': 'enums.FileScope'}, {'name': 'path', 'type': 'str'}], 'returns': 'bool', 'desc': 'Tests whether the path named in the given scope is a directory.'}, {'name': 'ListDirectory', 'args': [{'name': 'scope', 'type': 'enums.FileScope'}, {'name': 'directoryName', 'type': 'str'}], 'returns': 'list', 'desc': 'Get a list of files and directories in the given directory.'}, {'name': 'MakeDirectory', 'args': [{'name': 'scope', 'type': 'enums.FileScope'}, {'name': 'directoryName', 'type': 'str'}], 'returns': 'bool', 'desc': 'Create a new directory for storing files. The semantics of this method are such that it will\nreturn true if the directory exists at its completion. This can mean that the directory already\nexisted prior to the call.'}, {'name': 'MakeFullPath', 'args': [{'name': 'scope', 'type': 'enums.FileScope'}, {'name': 'path', 'type': 'str'}], 'returns': 'str', 'desc': 'Converts the scope and path into a single string for other components.'}, {'name': 'MoveFile', 'args': [{'name': 'fromScope', 'type': 'enums.FileScope'}, {'name': 'fromFileName', 'type': 'str'}, {'name': 'toScope', 'type': 'enums.FileScope'}, {'name': 'toFileName', 'type': 'str'}], 'returns': 'bool', 'desc': 'Move a file from one location to another.'}, {'name': 'ReadFrom', 'args': [{'name': 'fileName', 'type': 'str'}], 'returns': None, 'desc': "Reads text from a file in storage. Prefix the fileName with / to read from a\nspecific file on the SD card (for example, /myFile.txt will read the file\n/sdcard/myFile.txt). To read assets packaged with an application (also works for the\nCompanion) start the fileName with // (two slashes). If a\nfileName does not start with a slash, it will be read from the application's\nprivate storage (for packaged apps) and from /sdcard/AppInventor/data for the Companion."}, {'name': 'RemoveDirectory', 'args': [{'name': 'scope', 'type': 'enums.FileScope'}, {'name': 'directoryName', 'type': 'str'}, {'name': 'recursive', 'type': 'bool'}], 'returns': 'bool', 'desc': 'Remove a directory from the file system. If recursive is true, then everything is removed. If\nrecursive is false, only the directory is removed and only if it is empty.'}, {'name': 'SaveFile', 'args': [{'name': 'text', 'type': 'str'}, {'name': 'fileName', 'type': 'str'}], 'returns': None, 'desc': "Saves text to a file. If the fileName begins with a slash (/) the file is\nwritten to the sdcard (for example, writing to /myFile.txt will write the file to\n/sdcard/myFile.txt). If the fileName does not start with a slash, it will be\nwritten in the program's private data directory where it will not be accessible to other\nprograms on the phone. There is a special exception for the AI Companion where these files are\nwritten to /sdcard/AppInventor/data to facilitate debugging.\n\n   Note that this block will overwrite a file if it already exists. If you want to add content\nto an existing file use the AppendToFile method.\n"}]}

    def __init__(self, /, *, parent: Component=..., DefaultScope: enums.FileScope=..., ReadPermission: bool=..., WritePermission: bool=...):
        raise NotImplementedError

    @property
    def Scope(self) -> enums.FileScope:
        """Indicates the current scope for operations such as ReadFrom and SaveFile."""
        raise NotImplementedError

    @Scope.setter
    def Scope(self, value: enums.FileScope, /) -> None:
        raise NotImplementedError

    def AppendToFile(self, text: str, fileName: str, /) -> None:
        """Appends text to the end of a file. Creates the file if it does not already exist. See the help
text under SaveFile for information about where files are written.
On success, the AfterFileSaved event will run."""
        raise NotImplementedError

    def CopyFile(self, fromScope: enums.FileScope, fromFileName: str, toScope: enums.FileScope, toFileName: str, /) -> bool:
        """Copy the contents from the first file to the second file."""
        raise NotImplementedError

    def Delete(self, fileName: str, /) -> None:
        """Deletes a file from storage. Prefix the fileName with / to delete a specific
file in the SD card (for example, /myFile.txt will delete the file /sdcard/myFile.txt).
If the fileName does not begin with a /, then the file located in the
program's private storage will be deleted. Starting the fileName with // is
an error because asset files cannot be deleted."""
        raise NotImplementedError

    def Exists(self, scope: enums.FileScope, path: str, /) -> bool:
        """Tests whether the path exists in the given scope."""
        raise NotImplementedError

    def IsDirectory(self, scope: enums.FileScope, path: str, /) -> bool:
        """Tests whether the path named in the given scope is a directory."""
        raise NotImplementedError

    def ListDirectory(self, scope: enums.FileScope, directoryName: str, /) -> list:
        """Get a list of files and directories in the given directory."""
        raise NotImplementedError

    def MakeDirectory(self, scope: enums.FileScope, directoryName: str, /) -> bool:
        """Create a new directory for storing files. The semantics of this method are such that it will
return true if the directory exists at its completion. This can mean that the directory already
existed prior to the call."""
        raise NotImplementedError

    def MakeFullPath(self, scope: enums.FileScope, path: str, /) -> str:
        """Converts the scope and path into a single string for other components."""
        raise NotImplementedError

    def MoveFile(self, fromScope: enums.FileScope, fromFileName: str, toScope: enums.FileScope, toFileName: str, /) -> bool:
        """Move a file from one location to another."""
        raise NotImplementedError

    def ReadFrom(self, fileName: str, /) -> None:
        """Reads text from a file in storage. Prefix the fileName with / to read from a
specific file on the SD card (for example, /myFile.txt will read the file
/sdcard/myFile.txt). To read assets packaged with an application (also works for the
Companion) start the fileName with // (two slashes). If a
fileName does not start with a slash, it will be read from the application's
private storage (for packaged apps) and from /sdcard/AppInventor/data for the Companion."""
        raise NotImplementedError

    def RemoveDirectory(self, scope: enums.FileScope, directoryName: str, recursive: bool, /) -> bool:
        """Remove a directory from the file system. If recursive is true, then everything is removed. If
recursive is false, only the directory is removed and only if it is empty."""
        raise NotImplementedError

    def SaveFile(self, text: str, fileName: str, /) -> None:
        """Saves text to a file. If the fileName begins with a slash (/) the file is
written to the sdcard (for example, writing to /myFile.txt will write the file to
/sdcard/myFile.txt). If the fileName does not start with a slash, it will be
written in the program's private data directory where it will not be accessible to other
programs on the phone. There is a special exception for the AI Companion where these files are
written to /sdcard/AppInventor/data to facilitate debugging.

   Note that this block will overwrite a file if it already exists. If you want to add content
to an existing file use the AppendToFile method.
"""
        raise NotImplementedError

    def on_AfterFileSaved(self, callback: Callable[[str], None], /) -> None:
        """AfterFileSaved(fileName)

Event indicating that the contents of the file have been written."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterFileSaved(callback: Callable[['File', bool, str], None], /) -> None:
        """AfterFileSaved(fileName)

Event indicating that the contents of the file have been written."""
        raise NotImplementedError

    def on_GotText(self, callback: Callable[[str], None], /) -> None:
        """GotText(text)

Event indicating that the contents from the file have been read."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotText(callback: Callable[['File', bool, str], None], /) -> None:
        """GotText(text)

Event indicating that the contents from the file have been read."""
        raise NotImplementedError

class Spreadsheet(Component):
    """Spreadsheet is a non-visible component for storing and receiving data from
a Google Sheets document using the Google Sheets API."""
    __data__ = {'desc': 'Spreadsheet is a non-visible component for storing and receiving data from\na Google Sheets document using the Google Sheets API.', 'properties': [{'name': 'ApplicationName', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'The name of your application, used when making API calls.'}, {'name': 'CredentialsJson', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'The JSON File with credentials for the Service Account'}, {'name': 'SpreadsheetID', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'The ID for the Google Sheets file you want to edit. You can find the spreadsheetID in the URL of the Google Sheets file.'}], 'events': [{'name': 'ErrorOccurred', 'args': [{'name': 'errorMessage', 'type': 'str'}], 'desc': 'Triggered whenever an API call encounters an error. Details about the error are in errorMessage.'}, {'name': 'FinishedAddColumn', 'args': [{'name': 'columnNumber', 'type': 'int'}], 'desc': 'The callback event for the AddColumn block, called once the\nvalues on the table have been updated. Additionally, this returns the\ncolumn number for the new column.'}, {'name': 'FinishedAddRow', 'args': [{'name': 'rowNumber', 'type': 'int'}], 'desc': 'The callback event for the AddRow block, called once the\nvalues on the table have been updated. Additionally, this returns the\nrow number for the new row.'}, {'name': 'FinishedClearRange', 'args': [], 'desc': 'The callback event for the ClearRange block, called once the\nvalues on the table have been updated.'}, {'name': 'FinishedRemoveColumn', 'args': [], 'desc': 'The callback event for the RemoveColumn block, called once the\nvalues on the table have been updated.'}, {'name': 'FinishedRemoveRow', 'args': [], 'desc': 'The callback event for the RemoveRow block, called once the\nvalues on the table have been updated.'}, {'name': 'FinishedWriteCell', 'args': [], 'desc': 'The callback event for the WriteCell block, called once the\nvalues on the table have been updated.'}, {'name': 'FinishedWriteColumn', 'args': [], 'desc': 'The callback event for the WriteColumn block, called once the\nvalues on the table have been updated.'}, {'name': 'FinishedWriteRange', 'args': [], 'desc': 'The callback event for the WriteRange block, called once the\nvalues on the table have been updated.'}, {'name': 'FinishedWriteRow', 'args': [], 'desc': 'The callback event for the WriteRow block, called once the\nvalues on the table have been updated.'}, {'name': 'GotCellData', 'args': [{'name': 'cellData', 'type': 'str'}], 'desc': 'The callback event for the ReadCell block. The cellData is\nthe text value in the cell.'}, {'name': 'GotColumnData', 'args': [{'name': 'columnData', 'type': 'list'}], 'desc': 'The callback event for the ReadColumn block. The columnData is a\nlist of text cell-values in order of increasing row number.'}, {'name': 'GotRangeData', 'args': [{'name': 'rangeData', 'type': 'list'}], 'desc': 'The callback event for the ReadRange block. The rangeData is\na list of rows, where the dimensions are the same as the rangeReference.'}, {'name': 'GotRowData', 'args': [{'name': 'rowDataList', 'type': 'list'}], 'desc': 'The callback event for the ReadRow block. The rowDataList is a\nlist of text cell-values in order of increasing column number.'}, {'name': 'GotSheetData', 'args': [{'name': 'sheetData', 'type': 'list'}], 'desc': 'The callback event for the ReadSheet block. The sheetData is a\nlist of rows.'}], 'methods': [{'name': 'AddColumn', 'args': [{'name': 'sheetName', 'type': 'str'}, {'name': 'data', 'type': 'list'}], 'returns': None, 'desc': 'Given a list of values as data, appends the values to the next empty\ncolumn of the sheet. It will always start from the top row and continue\ndownwards. Once complete, it triggers the FinishedAddColumn\ncallback event.'}, {'name': 'AddRow', 'args': [{'name': 'sheetName', 'type': 'str'}, {'name': 'data', 'type': 'list'}], 'returns': None, 'desc': 'Given a list of values as data, appends the values to the next\nempty row of the sheet. It will always start from the left most column and\ncontinue to the right. Once complete, it triggers the FinishedAddRow\ncallback event. Additionally, this returns the row number for the new row.'}, {'name': 'ClearRange', 'args': [{'name': 'sheetName', 'type': 'str'}, {'name': 'rangeReference', 'type': 'str'}], 'returns': None, 'desc': 'Empties the cells in the given range. Once complete, this block triggers\nthe FinishedClearRange callback event.'}, {'name': 'GetCellReference', 'args': [{'name': 'row', 'type': 'int'}, {'name': 'column', 'type': 'int'}], 'returns': 'str', 'desc': 'Converts the integer representation of rows and columns to A1-Notation used\nin Google Sheets for a single cell. For example, row 1 and col 2\ncorresponds to the string "B1".'}, {'name': 'GetRangeReference', 'args': [{'name': 'row1', 'type': 'int'}, {'name': 'column1', 'type': 'int'}, {'name': 'row2', 'type': 'int'}, {'name': 'column2', 'type': 'int'}], 'returns': 'str', 'desc': 'Converts the integer representation of rows and columns for the corners of\nthe range to A1-Notation used in Google Sheets. For example, selecting the\nrange from row 1, col 2 to row 3, col 4 corresponds to the string "B1:D3".'}, {'name': 'ReadCell', 'args': [{'name': 'sheetName', 'type': 'str'}, {'name': 'cellReference', 'type': 'str'}], 'returns': None, 'desc': 'On the page with the provided sheetName, reads the cell at the given\ncellReference and triggers the GotCellData callback event. The\ncellReference can be either a text block with A1-Notation, or the result of\nthe GetCellReference block.'}, {'name': 'ReadColumn', 'args': [{'name': 'sheetName', 'type': 'str'}, {'name': 'column', 'type': 'str'}], 'returns': None, 'desc': 'On the page with the provided sheetName, reads the column at the given\ncolNumber and triggers the GotColumnData callback event.'}, {'name': 'ReadRange', 'args': [{'name': 'sheetName', 'type': 'str'}, {'name': 'rangeReference', 'type': 'str'}], 'returns': None, 'desc': 'On the page with the provided sheetName, reads the cells at the given\nrangeReference and triggers the GotRangeData callback event. The\nrangeReference can be either a text block with A1-Notation, or the result\nof the GetRangeReference block.'}, {'name': 'ReadRow', 'args': [{'name': 'sheetName', 'type': 'str'}, {'name': 'rowNumber', 'type': 'int'}], 'returns': None, 'desc': 'On the page with the provided sheetName, reads the row at the given\nrowNumber and triggers the GotRowData callback event.'}, {'name': 'ReadSheet', 'args': [{'name': 'sheetName', 'type': 'str'}], 'returns': None, 'desc': 'Reads the entire Google Sheets document and triggers the\nGotSheetData callback event.'}, {'name': 'ReadWithExactFilter', 'args': [{'name': 'sheetName', 'type': 'str'}, {'name': 'colID', 'type': 'int'}, {'name': 'value', 'type': 'str'}], 'returns': None, 'desc': 'Filters a Google Sheet for rows where the given column number matches the provided value.'}, {'name': 'ReadWithPartialFilter', 'args': [{'name': 'sheetName', 'type': 'str'}, {'name': 'colID', 'type': 'int'}, {'name': 'value', 'type': 'str'}], 'returns': None, 'desc': 'Filters a Google Sheet for rows where the given column number contains the provided value string.'}, {'name': 'RemoveColumn', 'args': [{'name': 'sheetName', 'type': 'str'}, {'name': 'column', 'type': 'str'}], 'returns': None, 'desc': 'Deletes the column with the given column number from the table. This does\nnot clear the column, but removes it entirely. The sheet\'s grid id can be\nfound at the end of the url of the Google Sheets document, right after the\n"gid=". Once complete, it triggers the FinishedRemoveColumn\ncallback event.'}, {'name': 'RemoveRow', 'args': [{'name': 'sheetName', 'type': 'str'}, {'name': 'rowNumber', 'type': 'int'}], 'returns': None, 'desc': 'Deletes the row with the given row number (1-indexed) from the table. This\ndoes not clear the row, but removes it entirely. The sheet\'s grid id can be\nfound at the end of the url of the Google Sheets document, right after the\n"gid=". Once complete, it triggers the FinishedRemoveRow\ncallback event.'}, {'name': 'WriteCell', 'args': [{'name': 'sheetName', 'type': 'str'}, {'name': 'cellReference', 'type': 'str'}, {'name': 'data', 'type': 'Any'}], 'returns': None, 'desc': 'Given text or a number as data, writes the value to the cell. It will\noverride any existing data in the cell with the one provided. Once complete,\nit triggers the FinishedWriteCell callback event.'}, {'name': 'WriteColumn', 'args': [{'name': 'sheetName', 'type': 'str'}, {'name': 'column', 'type': 'str'}, {'name': 'data', 'type': 'list'}], 'returns': None, 'desc': 'Given a list of values as data, writes the values to the column with the\ngiven column number, overriding existing values from top down. (Note: It\nwill not erase the entire column.) Once complete, it triggers the\nFinishedWriteColumn callback event.'}, {'name': 'WriteRange', 'args': [{'name': 'sheetName', 'type': 'str'}, {'name': 'rangeReference', 'type': 'str'}, {'name': 'data', 'type': 'list'}], 'returns': None, 'desc': 'Given list of lists as data, writes the values to cells in the range. The\nnumber of rows and columns in the range must match the dimensions of your\ndata. This method will override existing data in the range. Once complete,\nit triggers the FinishedWriteRange callback event.'}, {'name': 'WriteRow', 'args': [{'name': 'sheetName', 'type': 'str'}, {'name': 'rowNumber', 'type': 'int'}, {'name': 'data', 'type': 'list'}], 'returns': None, 'desc': 'Given a list of values as data, writes the values to the row  with the\ngiven row number, overriding existing values from left to right. (Note: It\nwill not erase the entire row.) Once complete, it triggers the\nFinishedWriteRow callback event.'}]}

    def __init__(self, /, *, parent: Component=..., ApplicationName: str=..., CredentialsJson: str=..., SpreadsheetID: str=...):
        raise NotImplementedError

    @property
    def CredentialsJson(self) -> str:
        """The JSON File with credentials for the Service Account"""
        raise NotImplementedError

    @CredentialsJson.setter
    def CredentialsJson(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def SpreadsheetID(self) -> str:
        """The ID for the Google Sheets file you want to edit. You can find the spreadsheetID in the URL of the Google Sheets file."""
        raise NotImplementedError

    @SpreadsheetID.setter
    def SpreadsheetID(self, value: str, /) -> None:
        raise NotImplementedError

    def AddColumn(self, sheetName: str, data: list, /) -> None:
        """Given a list of values as data, appends the values to the next empty
column of the sheet. It will always start from the top row and continue
downwards. Once complete, it triggers the FinishedAddColumn
callback event."""
        raise NotImplementedError

    def AddRow(self, sheetName: str, data: list, /) -> None:
        """Given a list of values as data, appends the values to the next
empty row of the sheet. It will always start from the left most column and
continue to the right. Once complete, it triggers the FinishedAddRow
callback event. Additionally, this returns the row number for the new row."""
        raise NotImplementedError

    def ClearRange(self, sheetName: str, rangeReference: str, /) -> None:
        """Empties the cells in the given range. Once complete, this block triggers
the FinishedClearRange callback event."""
        raise NotImplementedError

    def GetCellReference(self, row: int, column: int, /) -> str:
        """Converts the integer representation of rows and columns to A1-Notation used
in Google Sheets for a single cell. For example, row 1 and col 2
corresponds to the string "B1"."""
        raise NotImplementedError

    def GetRangeReference(self, row1: int, column1: int, row2: int, column2: int, /) -> str:
        """Converts the integer representation of rows and columns for the corners of
the range to A1-Notation used in Google Sheets. For example, selecting the
range from row 1, col 2 to row 3, col 4 corresponds to the string "B1:D3"."""
        raise NotImplementedError

    def ReadCell(self, sheetName: str, cellReference: str, /) -> None:
        """On the page with the provided sheetName, reads the cell at the given
cellReference and triggers the GotCellData callback event. The
cellReference can be either a text block with A1-Notation, or the result of
the GetCellReference block."""
        raise NotImplementedError

    def ReadColumn(self, sheetName: str, column: str, /) -> None:
        """On the page with the provided sheetName, reads the column at the given
colNumber and triggers the GotColumnData callback event."""
        raise NotImplementedError

    def ReadRange(self, sheetName: str, rangeReference: str, /) -> None:
        """On the page with the provided sheetName, reads the cells at the given
rangeReference and triggers the GotRangeData callback event. The
rangeReference can be either a text block with A1-Notation, or the result
of the GetRangeReference block."""
        raise NotImplementedError

    def ReadRow(self, sheetName: str, rowNumber: int, /) -> None:
        """On the page with the provided sheetName, reads the row at the given
rowNumber and triggers the GotRowData callback event."""
        raise NotImplementedError

    def ReadSheet(self, sheetName: str, /) -> None:
        """Reads the entire Google Sheets document and triggers the
GotSheetData callback event."""
        raise NotImplementedError

    def ReadWithExactFilter(self, sheetName: str, colID: int, value: str, /) -> None:
        """Filters a Google Sheet for rows where the given column number matches the provided value."""
        raise NotImplementedError

    def ReadWithPartialFilter(self, sheetName: str, colID: int, value: str, /) -> None:
        """Filters a Google Sheet for rows where the given column number contains the provided value string."""
        raise NotImplementedError

    def RemoveColumn(self, sheetName: str, column: str, /) -> None:
        """Deletes the column with the given column number from the table. This does
not clear the column, but removes it entirely. The sheet's grid id can be
found at the end of the url of the Google Sheets document, right after the
"gid=". Once complete, it triggers the FinishedRemoveColumn
callback event."""
        raise NotImplementedError

    def RemoveRow(self, sheetName: str, rowNumber: int, /) -> None:
        """Deletes the row with the given row number (1-indexed) from the table. This
does not clear the row, but removes it entirely. The sheet's grid id can be
found at the end of the url of the Google Sheets document, right after the
"gid=". Once complete, it triggers the FinishedRemoveRow
callback event."""
        raise NotImplementedError

    def WriteCell(self, sheetName: str, cellReference: str, data: Any, /) -> None:
        """Given text or a number as data, writes the value to the cell. It will
override any existing data in the cell with the one provided. Once complete,
it triggers the FinishedWriteCell callback event."""
        raise NotImplementedError

    def WriteColumn(self, sheetName: str, column: str, data: list, /) -> None:
        """Given a list of values as data, writes the values to the column with the
given column number, overriding existing values from top down. (Note: It
will not erase the entire column.) Once complete, it triggers the
FinishedWriteColumn callback event."""
        raise NotImplementedError

    def WriteRange(self, sheetName: str, rangeReference: str, data: list, /) -> None:
        """Given list of lists as data, writes the values to cells in the range. The
number of rows and columns in the range must match the dimensions of your
data. This method will override existing data in the range. Once complete,
it triggers the FinishedWriteRange callback event."""
        raise NotImplementedError

    def WriteRow(self, sheetName: str, rowNumber: int, data: list, /) -> None:
        """Given a list of values as data, writes the values to the row  with the
given row number, overriding existing values from left to right. (Note: It
will not erase the entire row.) Once complete, it triggers the
FinishedWriteRow callback event."""
        raise NotImplementedError

    def on_ErrorOccurred(self, callback: Callable[[str], None], /) -> None:
        """ErrorOccurred(errorMessage)

Triggered whenever an API call encounters an error. Details about the error are in errorMessage."""
        raise NotImplementedError

    @staticmethod
    def on_any_ErrorOccurred(callback: Callable[['Spreadsheet', bool, str], None], /) -> None:
        """ErrorOccurred(errorMessage)

Triggered whenever an API call encounters an error. Details about the error are in errorMessage."""
        raise NotImplementedError

    def on_FinishedAddColumn(self, callback: Callable[[int], None], /) -> None:
        """FinishedAddColumn(columnNumber)

The callback event for the AddColumn block, called once the
values on the table have been updated. Additionally, this returns the
column number for the new column."""
        raise NotImplementedError

    @staticmethod
    def on_any_FinishedAddColumn(callback: Callable[['Spreadsheet', bool, int], None], /) -> None:
        """FinishedAddColumn(columnNumber)

The callback event for the AddColumn block, called once the
values on the table have been updated. Additionally, this returns the
column number for the new column."""
        raise NotImplementedError

    def on_FinishedAddRow(self, callback: Callable[[int], None], /) -> None:
        """FinishedAddRow(rowNumber)

The callback event for the AddRow block, called once the
values on the table have been updated. Additionally, this returns the
row number for the new row."""
        raise NotImplementedError

    @staticmethod
    def on_any_FinishedAddRow(callback: Callable[['Spreadsheet', bool, int], None], /) -> None:
        """FinishedAddRow(rowNumber)

The callback event for the AddRow block, called once the
values on the table have been updated. Additionally, this returns the
row number for the new row."""
        raise NotImplementedError

    def on_FinishedClearRange(self, callback: Callable[[], None], /) -> None:
        """FinishedClearRange()

The callback event for the ClearRange block, called once the
values on the table have been updated."""
        raise NotImplementedError

    @staticmethod
    def on_any_FinishedClearRange(callback: Callable[['Spreadsheet', bool], None], /) -> None:
        """FinishedClearRange()

The callback event for the ClearRange block, called once the
values on the table have been updated."""
        raise NotImplementedError

    def on_FinishedRemoveColumn(self, callback: Callable[[], None], /) -> None:
        """FinishedRemoveColumn()

The callback event for the RemoveColumn block, called once the
values on the table have been updated."""
        raise NotImplementedError

    @staticmethod
    def on_any_FinishedRemoveColumn(callback: Callable[['Spreadsheet', bool], None], /) -> None:
        """FinishedRemoveColumn()

The callback event for the RemoveColumn block, called once the
values on the table have been updated."""
        raise NotImplementedError

    def on_FinishedRemoveRow(self, callback: Callable[[], None], /) -> None:
        """FinishedRemoveRow()

The callback event for the RemoveRow block, called once the
values on the table have been updated."""
        raise NotImplementedError

    @staticmethod
    def on_any_FinishedRemoveRow(callback: Callable[['Spreadsheet', bool], None], /) -> None:
        """FinishedRemoveRow()

The callback event for the RemoveRow block, called once the
values on the table have been updated."""
        raise NotImplementedError

    def on_FinishedWriteCell(self, callback: Callable[[], None], /) -> None:
        """FinishedWriteCell()

The callback event for the WriteCell block, called once the
values on the table have been updated."""
        raise NotImplementedError

    @staticmethod
    def on_any_FinishedWriteCell(callback: Callable[['Spreadsheet', bool], None], /) -> None:
        """FinishedWriteCell()

The callback event for the WriteCell block, called once the
values on the table have been updated."""
        raise NotImplementedError

    def on_FinishedWriteColumn(self, callback: Callable[[], None], /) -> None:
        """FinishedWriteColumn()

The callback event for the WriteColumn block, called once the
values on the table have been updated."""
        raise NotImplementedError

    @staticmethod
    def on_any_FinishedWriteColumn(callback: Callable[['Spreadsheet', bool], None], /) -> None:
        """FinishedWriteColumn()

The callback event for the WriteColumn block, called once the
values on the table have been updated."""
        raise NotImplementedError

    def on_FinishedWriteRange(self, callback: Callable[[], None], /) -> None:
        """FinishedWriteRange()

The callback event for the WriteRange block, called once the
values on the table have been updated."""
        raise NotImplementedError

    @staticmethod
    def on_any_FinishedWriteRange(callback: Callable[['Spreadsheet', bool], None], /) -> None:
        """FinishedWriteRange()

The callback event for the WriteRange block, called once the
values on the table have been updated."""
        raise NotImplementedError

    def on_FinishedWriteRow(self, callback: Callable[[], None], /) -> None:
        """FinishedWriteRow()

The callback event for the WriteRow block, called once the
values on the table have been updated."""
        raise NotImplementedError

    @staticmethod
    def on_any_FinishedWriteRow(callback: Callable[['Spreadsheet', bool], None], /) -> None:
        """FinishedWriteRow()

The callback event for the WriteRow block, called once the
values on the table have been updated."""
        raise NotImplementedError

    def on_GotCellData(self, callback: Callable[[str], None], /) -> None:
        """GotCellData(cellData)

The callback event for the ReadCell block. The cellData is
the text value in the cell."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotCellData(callback: Callable[['Spreadsheet', bool, str], None], /) -> None:
        """GotCellData(cellData)

The callback event for the ReadCell block. The cellData is
the text value in the cell."""
        raise NotImplementedError

    def on_GotColumnData(self, callback: Callable[[list], None], /) -> None:
        """GotColumnData(columnData)

The callback event for the ReadColumn block. The columnData is a
list of text cell-values in order of increasing row number."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotColumnData(callback: Callable[['Spreadsheet', bool, list], None], /) -> None:
        """GotColumnData(columnData)

The callback event for the ReadColumn block. The columnData is a
list of text cell-values in order of increasing row number."""
        raise NotImplementedError

    def on_GotRangeData(self, callback: Callable[[list], None], /) -> None:
        """GotRangeData(rangeData)

The callback event for the ReadRange block. The rangeData is
a list of rows, where the dimensions are the same as the rangeReference."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotRangeData(callback: Callable[['Spreadsheet', bool, list], None], /) -> None:
        """GotRangeData(rangeData)

The callback event for the ReadRange block. The rangeData is
a list of rows, where the dimensions are the same as the rangeReference."""
        raise NotImplementedError

    def on_GotRowData(self, callback: Callable[[list], None], /) -> None:
        """GotRowData(rowDataList)

The callback event for the ReadRow block. The rowDataList is a
list of text cell-values in order of increasing column number."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotRowData(callback: Callable[['Spreadsheet', bool, list], None], /) -> None:
        """GotRowData(rowDataList)

The callback event for the ReadRow block. The rowDataList is a
list of text cell-values in order of increasing column number."""
        raise NotImplementedError

    def on_GotSheetData(self, callback: Callable[[list], None], /) -> None:
        """GotSheetData(sheetData)

The callback event for the ReadSheet block. The sheetData is a
list of rows."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotSheetData(callback: Callable[['Spreadsheet', bool, list], None], /) -> None:
        """GotSheetData(sheetData)

The callback event for the ReadSheet block. The sheetData is a
list of rows."""
        raise NotImplementedError

class TinyDB(Component):
    """TinyDB is a non-visible component that stores data for an app."""
    __data__ = {'desc': 'TinyDB is a non-visible component that stores data for an app.', 'properties': [{'name': 'Namespace', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Namespace for storing data.'}], 'events': [], 'methods': [{'name': 'ClearAll', 'args': [], 'returns': None, 'desc': 'Clear the entire data store.'}, {'name': 'ClearTag', 'args': [{'name': 'tag', 'type': 'str'}], 'returns': None, 'desc': 'Clear the entry with the given tag.'}, {'name': 'GetTags', 'args': [], 'returns': 'Any', 'desc': 'Return a list of all the tags in the data store.'}, {'name': 'GetValue', 'args': [{'name': 'tag', 'type': 'str'}, {'name': 'valueIfTagNotThere', 'type': 'Any'}], 'returns': 'Any', 'desc': "Retrieve the value stored under the given tag.  If there's no such tag, then\nreturn valueIfTagNotThere."}, {'name': 'StoreValue', 'args': [{'name': 'tag', 'type': 'str'}, {'name': 'valueToStore', 'type': 'Any'}], 'returns': None, 'desc': 'Store the given valueToStore under the given tag.\nThe storage persists on the phone when the app is restarted.'}]}

    def __init__(self, /, *, parent: Component=..., Namespace: str=...):
        raise NotImplementedError

    @property
    def Namespace(self) -> str:
        """Namespace for storing data."""
        raise NotImplementedError

    @Namespace.setter
    def Namespace(self, value: str, /) -> None:
        raise NotImplementedError

    def ClearAll(self, /) -> None:
        """Clear the entire data store."""
        raise NotImplementedError

    def ClearTag(self, tag: str, /) -> None:
        """Clear the entry with the given tag."""
        raise NotImplementedError

    def GetTags(self, /) -> Any:
        """Return a list of all the tags in the data store."""
        raise NotImplementedError

    def GetValue(self, tag: str, valueIfTagNotThere: Any, /) -> Any:
        """Retrieve the value stored under the given tag.  If there's no such tag, then
return valueIfTagNotThere."""
        raise NotImplementedError

    def StoreValue(self, tag: str, valueToStore: Any, /) -> None:
        """Store the given valueToStore under the given tag.
The storage persists on the phone when the app is restarted."""
        raise NotImplementedError

class TinyWebDB(Component):
    """The TinyWebDB component communicates with a Web service to store
and retrieve information.  Although this component is usable, it is
very limited and meant primarily as a demonstration for people who
would like to create their own components that talk to the Web.
The accompanying Web service is at
(http://tinywebdb.appinventor.mit.edu).  The component has methods to
store a value under a tag and to
retrieve the value associated with
the tag.  The interpretation of what "store" and "retrieve" means
is up to the Web service.  In this implementation, all tags and
values are strings (text).  This restriction may be relaxed in
future versions."""
    __data__ = {'desc': 'The TinyWebDB component communicates with a Web service to store\nand retrieve information.  Although this component is usable, it is\nvery limited and meant primarily as a demonstration for people who\nwould like to create their own components that talk to the Web.\nThe accompanying Web service is at\n(http://tinywebdb.appinventor.mit.edu).  The component has methods to\nstore a value under a tag and to\nretrieve the value associated with\nthe tag.  The interpretation of what "store" and "retrieve" means\nis up to the Web service.  In this implementation, all tags and\nvalues are strings (text).  This restriction may be relaxed in\nfuture versions.', 'properties': [{'name': 'ServiceURL', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the URL of the  Web service.\nThe default value is the demo service running on App Engine.'}], 'events': [{'name': 'GotValue', 'args': [{'name': 'tagFromWebDB', 'type': 'str'}, {'name': 'valueFromWebDB', 'type': 'Any'}], 'desc': 'Indicates that a GetValue server request has succeeded.'}, {'name': 'ValueStored', 'args': [], 'desc': 'Event indicating that a StoreValue  server request has succeeded.'}, {'name': 'WebServiceError', 'args': [{'name': 'message', 'type': 'str'}], 'desc': 'Indicates that the communication with the Web service signaled an error.'}], 'methods': [{'name': 'GetValue', 'args': [{'name': 'tag', 'type': 'str'}], 'returns': None, 'desc': 'GetValue asks the Web service to get the value stored under the given tag.\nIt is up to the Web service what to return if there is no value stored under the\ntag.  This component just accepts whatever is returned. The\nGotValue event will be run on completion.'}, {'name': 'StoreValue', 'args': [{'name': 'tag', 'type': 'str'}, {'name': 'valueToStore', 'type': 'Any'}], 'returns': None, 'desc': 'Sends a request to the Web service to store the given valueToStore under\nthe given tag. The ValueStored event will be run on completion.'}]}

    def __init__(self, /, *, parent: Component=..., ServiceURL: str=...):
        raise NotImplementedError

    @property
    def ServiceURL(self) -> str:
        """Specifies the URL of the  Web service.
The default value is the demo service running on App Engine."""
        raise NotImplementedError

    @ServiceURL.setter
    def ServiceURL(self, value: str, /) -> None:
        raise NotImplementedError

    def GetValue(self, tag: str, /) -> None:
        """GetValue asks the Web service to get the value stored under the given tag.
It is up to the Web service what to return if there is no value stored under the
tag.  This component just accepts whatever is returned. The
GotValue event will be run on completion."""
        raise NotImplementedError

    def StoreValue(self, tag: str, valueToStore: Any, /) -> None:
        """Sends a request to the Web service to store the given valueToStore under
the given tag. The ValueStored event will be run on completion."""
        raise NotImplementedError

    def on_GotValue(self, callback: Callable[[str, Any], None], /) -> None:
        """GotValue(tagFromWebDB, valueFromWebDB)

Indicates that a GetValue server request has succeeded."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotValue(callback: Callable[['TinyWebDB', bool, str, Any], None], /) -> None:
        """GotValue(tagFromWebDB, valueFromWebDB)

Indicates that a GetValue server request has succeeded."""
        raise NotImplementedError

    def on_ValueStored(self, callback: Callable[[], None], /) -> None:
        """ValueStored()

Event indicating that a StoreValue  server request has succeeded."""
        raise NotImplementedError

    @staticmethod
    def on_any_ValueStored(callback: Callable[['TinyWebDB', bool], None], /) -> None:
        """ValueStored()

Event indicating that a StoreValue  server request has succeeded."""
        raise NotImplementedError

    def on_WebServiceError(self, callback: Callable[[str], None], /) -> None:
        """WebServiceError(message)

Indicates that the communication with the Web service signaled an error."""
        raise NotImplementedError

    @staticmethod
    def on_any_WebServiceError(callback: Callable[['TinyWebDB', bool, str], None], /) -> None:
        """WebServiceError(message)

Indicates that the communication with the Web service signaled an error."""
        raise NotImplementedError

class ActivityStarter(Component):
    """A component that can launch an activity using the StartActivity method."""
    __data__ = {'desc': 'A component that can launch an activity using the StartActivity method.', 'properties': [{'name': 'Action', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the action that will be used to start the activity.'}, {'name': 'ActivityClass', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the class part of the specific component that will be started.'}, {'name': 'ActivityPackage', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the package part of the specific component that will be started.'}, {'name': 'DataType', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the MIME type to pass to the activity.'}, {'name': 'DataUri', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the data URI that will be used to start the activity.'}, {'name': 'ExtraKey', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the extra key that will be passed to the activity.\nObsolete. Should use Extras instead'}, {'name': 'ExtraValue', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the extra value that will be passed to the activity.\nObsolete. Should use Extras instead'}, {'name': 'Extras', 'type': 'list', 'ro': False, 'do': False, 'bo': True, 'desc': 'Returns the list of key-value pairs that will be passed as extra data to the activity.'}, {'name': 'Result', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the result from the activity.'}, {'name': 'ResultName', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the name that will be used to retrieve a result from the\nactivity.'}, {'name': 'ResultType', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the MIME type from the activity.'}, {'name': 'ResultUri', 'type': 'str', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns the URI from the activity.'}], 'events': [{'name': 'ActivityCanceled', 'args': [], 'desc': 'Event raised if this `ActivityStarter returns because the activity was canceled.'}, {'name': 'AfterActivity', 'args': [{'name': 'result', 'type': 'str'}], 'desc': 'Event raised after this ActivityStarter returns.'}], 'methods': [{'name': 'ResolveActivity', 'args': [], 'returns': 'str', 'desc': 'Returns the name of the activity that corresponds to this ActivityStarter,\nor an empty string if no corresponding activity can be found.'}, {'name': 'StartActivity', 'args': [], 'returns': None, 'desc': 'Start the activity corresponding to this ActivityStarter.'}]}

    def __init__(self, /, *, parent: Component=..., Action: str=..., ActivityClass: str=..., ActivityPackage: str=..., DataType: str=..., DataUri: str=..., ExtraKey: str=..., ExtraValue: str=..., ResultName: str=...):
        raise NotImplementedError

    @property
    def Action(self) -> str:
        """Specifies the action that will be used to start the activity."""
        raise NotImplementedError

    @Action.setter
    def Action(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def ActivityClass(self) -> str:
        """Specifies the class part of the specific component that will be started."""
        raise NotImplementedError

    @ActivityClass.setter
    def ActivityClass(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def ActivityPackage(self) -> str:
        """Specifies the package part of the specific component that will be started."""
        raise NotImplementedError

    @ActivityPackage.setter
    def ActivityPackage(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def DataType(self) -> str:
        """Specifies the MIME type to pass to the activity."""
        raise NotImplementedError

    @DataType.setter
    def DataType(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def DataUri(self) -> str:
        """Specifies the data URI that will be used to start the activity."""
        raise NotImplementedError

    @DataUri.setter
    def DataUri(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def ExtraKey(self) -> str:
        """Specifies the extra key that will be passed to the activity.
Obsolete. Should use Extras instead"""
        raise NotImplementedError

    @ExtraKey.setter
    def ExtraKey(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def ExtraValue(self) -> str:
        """Specifies the extra value that will be passed to the activity.
Obsolete. Should use Extras instead"""
        raise NotImplementedError

    @ExtraValue.setter
    def ExtraValue(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Extras(self) -> list:
        """Returns the list of key-value pairs that will be passed as extra data to the activity."""
        raise NotImplementedError

    @Extras.setter
    def Extras(self, value: list, /) -> None:
        raise NotImplementedError

    @property
    def Result(self) -> str:
        """Returns the result from the activity."""
        raise NotImplementedError

    @property
    def ResultName(self) -> str:
        """Specifies the name that will be used to retrieve a result from the
activity."""
        raise NotImplementedError

    @ResultName.setter
    def ResultName(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def ResultType(self) -> str:
        """Returns the MIME type from the activity."""
        raise NotImplementedError

    @property
    def ResultUri(self) -> str:
        """Returns the URI from the activity."""
        raise NotImplementedError

    def ResolveActivity(self, /) -> str:
        """Returns the name of the activity that corresponds to this ActivityStarter,
or an empty string if no corresponding activity can be found."""
        raise NotImplementedError

    def StartActivity(self, /) -> None:
        """Start the activity corresponding to this ActivityStarter."""
        raise NotImplementedError

    def on_ActivityCanceled(self, callback: Callable[[], None], /) -> None:
        """ActivityCanceled()

Event raised if this `ActivityStarter returns because the activity was canceled."""
        raise NotImplementedError

    @staticmethod
    def on_any_ActivityCanceled(callback: Callable[['ActivityStarter', bool], None], /) -> None:
        """ActivityCanceled()

Event raised if this `ActivityStarter returns because the activity was canceled."""
        raise NotImplementedError

    def on_AfterActivity(self, callback: Callable[[str], None], /) -> None:
        """AfterActivity(result)

Event raised after this ActivityStarter returns."""
        raise NotImplementedError

    @staticmethod
    def on_any_AfterActivity(callback: Callable[['ActivityStarter', bool, str], None], /) -> None:
        """AfterActivity(result)

Event raised after this ActivityStarter returns."""
        raise NotImplementedError

class BluetoothClient(Component):
    """Use BluetoothClient to connect your device to other devices using Bluetooth. This component
uses the Serial Port Profile (SPP) for communication. If you are interested in using Bluetooth
low energy, please see the
BluetoothLE extension."""
    __data__ = {'desc': 'Use BluetoothClient to connect your device to other devices using Bluetooth. This component\nuses the Serial Port Profile (SPP) for communication. If you are interested in using Bluetooth\nlow energy, please see the\nBluetoothLE extension.', 'properties': [{'name': 'AddressesAndNames', 'type': 'list', 'ro': True, 'do': False, 'bo': True, 'desc': "Returns the list of paired Bluetooth devices. Each element of the returned\nlist is a String consisting of the device's address, a space, and the\ndevice's name. On Android 12 or later, if the permissions BLUETOOTH_CONNECT\nand BLUETOOTH_SCAN have not been granted to the app, the block will raise\nan error via the Screen's PermissionDenied event."}, {'name': 'Available', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns true if Bluetooth is available on the device,\nfalse otherwise.'}, {'name': 'CharacterEncoding', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Returns the character encoding to use when sending and receiving text.'}, {'name': 'DelimiterByte', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Returns the delimiter byte to use when passing a negative number for the\nnumberOfBytes parameter when calling ReceiveText, ReceiveSignedBytes, or\nReceiveUnsignedBytes.'}, {'name': 'DisconnectOnError', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether BluetoothClient/BluetoothServer should be disconnected automatically when an error occurs.'}, {'name': 'Enabled', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns true if Bluetooth is enabled, false otherwise.'}, {'name': 'HighByteFirst', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether numbers are sent and received with the most significant\nbyte first.'}, {'name': 'IsConnected', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns frue if a connection to a Bluetooth device has been made.'}, {'name': 'NoLocationNeeded', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': "On Android 12 and later, indicates that Bluetooth is not used to determine the user's location."}, {'name': 'PollingRate', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Returns the configured polling rate value of the Bluetooth Client.'}, {'name': 'Secure', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether a secure connection should be used.'}], 'events': [], 'methods': [{'name': 'BytesAvailableToReceive', 'args': [], 'returns': 'int', 'desc': 'Returns number of bytes available from the input stream.'}, {'name': 'Connect', 'args': [{'name': 'address', 'type': 'str'}], 'returns': 'bool', 'desc': 'Connect to a Bluetooth device with the given address.'}, {'name': 'ConnectWithUUID', 'args': [{'name': 'address', 'type': 'str'}, {'name': 'uuid', 'type': 'str'}], 'returns': 'bool', 'desc': 'Connect to a Bluetooth device with the given address and a specific UUID.'}, {'name': 'Disconnect', 'args': [], 'returns': None, 'desc': 'Disconnects from the connected Bluetooth device.'}, {'name': 'IsDevicePaired', 'args': [{'name': 'address', 'type': 'str'}], 'returns': 'bool', 'desc': 'Checks whether the Bluetooth device with the given address is paired.'}, {'name': 'ReceiveSigned1ByteNumber', 'args': [], 'returns': 'int', 'desc': 'Reads a signed 1-byte number.'}, {'name': 'ReceiveSigned2ByteNumber', 'args': [], 'returns': 'int', 'desc': 'Reads a signed 2-byte number.'}, {'name': 'ReceiveSigned4ByteNumber', 'args': [], 'returns': 'int', 'desc': 'Reads a signed 4-byte number.'}, {'name': 'ReceiveSignedBytes', 'args': [{'name': 'numberOfBytes', 'type': 'int'}], 'returns': 'list', 'desc': 'Reads a number of signed bytes from the input stream and returns them as\na List.\n\n   If numberOfBytes is negative, this method reads until a delimiter byte\nvalue is read. The delimiter byte value is included in the returned list.\n'}, {'name': 'ReceiveText', 'args': [{'name': 'numberOfBytes', 'type': 'int'}], 'returns': 'str', 'desc': 'Reads a number of bytes from the input stream and converts them to text.\n\n   If numberOfBytes is negative, read until a delimiter byte value is read.\n'}, {'name': 'ReceiveUnsigned1ByteNumber', 'args': [], 'returns': 'int', 'desc': 'Reads an unsigned 1-byte number.'}, {'name': 'ReceiveUnsigned2ByteNumber', 'args': [], 'returns': 'int', 'desc': 'Reads an unsigned 2-byte number.'}, {'name': 'ReceiveUnsigned4ByteNumber', 'args': [], 'returns': 'int', 'desc': 'Reads an unsigned 4-byte number.'}, {'name': 'ReceiveUnsignedBytes', 'args': [{'name': 'numberOfBytes', 'type': 'int'}], 'returns': 'list', 'desc': 'Reads a number of unsigned bytes from the input stream and returns them as\na List.\n\n   If numberOfBytes is negative, this method reads until a delimiter byte\nvalue is read. The delimiter byte value is included in the returned list.\n'}, {'name': 'Send1ByteNumber', 'args': [{'name': 'number', 'type': 'str'}], 'returns': None, 'desc': "Decodes the given number String to an integer and writes it as one byte\nto the output stream.\n\n   If the number could not be decoded to an integer, or the integer would not\nfit in one byte, then the Form's ErrorOccurred event is triggered and this\nmethod returns without writing any bytes to the output stream.\n"}, {'name': 'Send2ByteNumber', 'args': [{'name': 'number', 'type': 'str'}], 'returns': None, 'desc': "Decodes the given number String to an integer and writes it as two bytes\nto the output stream.\n\n   If the number could not be decoded to an integer, or the integer would not\nfit in two bytes, then the Form's ErrorOccurred event is triggered and this\nmethod returns without writing any bytes to the output stream.\n"}, {'name': 'Send4ByteNumber', 'args': [{'name': 'number', 'type': 'str'}], 'returns': None, 'desc': "Decodes the given number String to an integer and writes it as four bytes\nto the output stream.\n\n   If the number could not be decoded to an integer, or the integer would not\nfit in four bytes, then the Form's ErrorOccurred event is triggered and this\nmethod returns without writing any bytes to the output stream.\n"}, {'name': 'SendBytes', 'args': [{'name': 'list', 'type': 'list'}], 'returns': None, 'desc': "Takes each element from the given list, converts it to a String, decodes\nthe String to an integer, and writes it as one byte to the output stream.\n\n   If an element could not be decoded to an integer, or the integer would not\nfit in one byte, then the Form's ErrorOccurred event is triggered and this\nmethod returns without writing any bytes to the output stream.\n"}, {'name': 'SendText', 'args': [{'name': 'text', 'type': 'str'}], 'returns': None, 'desc': 'Converts the given text to bytes and writes them to the output stream.'}]}

    def __init__(self, /, *, parent: Component=..., CharacterEncoding: str=..., DelimiterByte: int=..., DisconnectOnError: bool=..., HighByteFirst: bool=..., NoLocationNeeded: bool=..., PollingRate: int=..., Secure: bool=...):
        raise NotImplementedError

    @property
    def AddressesAndNames(self) -> list:
        """Returns the list of paired Bluetooth devices. Each element of the returned
list is a String consisting of the device's address, a space, and the
device's name. On Android 12 or later, if the permissions BLUETOOTH_CONNECT
and BLUETOOTH_SCAN have not been granted to the app, the block will raise
an error via the Screen's PermissionDenied event."""
        raise NotImplementedError

    @property
    def Available(self) -> bool:
        """Returns true if Bluetooth is available on the device,
false otherwise."""
        raise NotImplementedError

    @property
    def CharacterEncoding(self) -> str:
        """Returns the character encoding to use when sending and receiving text."""
        raise NotImplementedError

    @CharacterEncoding.setter
    def CharacterEncoding(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def DelimiterByte(self) -> int:
        """Returns the delimiter byte to use when passing a negative number for the
numberOfBytes parameter when calling ReceiveText, ReceiveSignedBytes, or
ReceiveUnsignedBytes."""
        raise NotImplementedError

    @DelimiterByte.setter
    def DelimiterByte(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def DisconnectOnError(self) -> bool:
        """Specifies whether BluetoothClient/BluetoothServer should be disconnected automatically when an error occurs."""
        raise NotImplementedError

    @DisconnectOnError.setter
    def DisconnectOnError(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Returns true if Bluetooth is enabled, false otherwise."""
        raise NotImplementedError

    @property
    def HighByteFirst(self) -> bool:
        """Specifies whether numbers are sent and received with the most significant
byte first."""
        raise NotImplementedError

    @HighByteFirst.setter
    def HighByteFirst(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def IsConnected(self) -> bool:
        """Returns frue if a connection to a Bluetooth device has been made."""
        raise NotImplementedError

    @property
    def PollingRate(self) -> int:
        """Returns the configured polling rate value of the Bluetooth Client."""
        raise NotImplementedError

    @PollingRate.setter
    def PollingRate(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Secure(self) -> bool:
        """Specifies whether a secure connection should be used."""
        raise NotImplementedError

    @Secure.setter
    def Secure(self, value: bool, /) -> None:
        raise NotImplementedError

    def BytesAvailableToReceive(self, /) -> int:
        """Returns number of bytes available from the input stream."""
        raise NotImplementedError

    def Connect(self, address: str, /) -> bool:
        """Connect to a Bluetooth device with the given address."""
        raise NotImplementedError

    def ConnectWithUUID(self, address: str, uuid: str, /) -> bool:
        """Connect to a Bluetooth device with the given address and a specific UUID."""
        raise NotImplementedError

    def Disconnect(self, /) -> None:
        """Disconnects from the connected Bluetooth device."""
        raise NotImplementedError

    def IsDevicePaired(self, address: str, /) -> bool:
        """Checks whether the Bluetooth device with the given address is paired."""
        raise NotImplementedError

    def ReceiveSigned1ByteNumber(self, /) -> int:
        """Reads a signed 1-byte number."""
        raise NotImplementedError

    def ReceiveSigned2ByteNumber(self, /) -> int:
        """Reads a signed 2-byte number."""
        raise NotImplementedError

    def ReceiveSigned4ByteNumber(self, /) -> int:
        """Reads a signed 4-byte number."""
        raise NotImplementedError

    def ReceiveSignedBytes(self, numberOfBytes: int, /) -> list:
        """Reads a number of signed bytes from the input stream and returns them as
a List.

   If numberOfBytes is negative, this method reads until a delimiter byte
value is read. The delimiter byte value is included in the returned list.
"""
        raise NotImplementedError

    def ReceiveText(self, numberOfBytes: int, /) -> str:
        """Reads a number of bytes from the input stream and converts them to text.

   If numberOfBytes is negative, read until a delimiter byte value is read.
"""
        raise NotImplementedError

    def ReceiveUnsigned1ByteNumber(self, /) -> int:
        """Reads an unsigned 1-byte number."""
        raise NotImplementedError

    def ReceiveUnsigned2ByteNumber(self, /) -> int:
        """Reads an unsigned 2-byte number."""
        raise NotImplementedError

    def ReceiveUnsigned4ByteNumber(self, /) -> int:
        """Reads an unsigned 4-byte number."""
        raise NotImplementedError

    def ReceiveUnsignedBytes(self, numberOfBytes: int, /) -> list:
        """Reads a number of unsigned bytes from the input stream and returns them as
a List.

   If numberOfBytes is negative, this method reads until a delimiter byte
value is read. The delimiter byte value is included in the returned list.
"""
        raise NotImplementedError

    def Send1ByteNumber(self, number: str, /) -> None:
        """Decodes the given number String to an integer and writes it as one byte
to the output stream.

   If the number could not be decoded to an integer, or the integer would not
fit in one byte, then the Form's ErrorOccurred event is triggered and this
method returns without writing any bytes to the output stream.
"""
        raise NotImplementedError

    def Send2ByteNumber(self, number: str, /) -> None:
        """Decodes the given number String to an integer and writes it as two bytes
to the output stream.

   If the number could not be decoded to an integer, or the integer would not
fit in two bytes, then the Form's ErrorOccurred event is triggered and this
method returns without writing any bytes to the output stream.
"""
        raise NotImplementedError

    def Send4ByteNumber(self, number: str, /) -> None:
        """Decodes the given number String to an integer and writes it as four bytes
to the output stream.

   If the number could not be decoded to an integer, or the integer would not
fit in four bytes, then the Form's ErrorOccurred event is triggered and this
method returns without writing any bytes to the output stream.
"""
        raise NotImplementedError

    def SendBytes(self, list: list, /) -> None:
        """Takes each element from the given list, converts it to a String, decodes
the String to an integer, and writes it as one byte to the output stream.

   If an element could not be decoded to an integer, or the integer would not
fit in one byte, then the Form's ErrorOccurred event is triggered and this
method returns without writing any bytes to the output stream.
"""
        raise NotImplementedError

    def SendText(self, text: str, /) -> None:
        """Converts the given text to bytes and writes them to the output stream."""
        raise NotImplementedError

class BluetoothServer(Component):
    """Use the BluetoothServer component to turn your device into a server that receive connections
from other apps that use the BluetoothClient component."""
    __data__ = {'desc': 'Use the BluetoothServer component to turn your device into a server that receive connections\nfrom other apps that use the BluetoothClient component.', 'properties': [{'name': 'Available', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns true if Bluetooth is available on the device,\nfalse otherwise.'}, {'name': 'CharacterEncoding', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Returns the character encoding to use when sending and receiving text.'}, {'name': 'DelimiterByte', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Returns the delimiter byte to use when passing a negative number for the\nnumberOfBytes parameter when calling ReceiveText, ReceiveSignedBytes, or\nReceiveUnsignedBytes.'}, {'name': 'Enabled', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns true if Bluetooth is enabled, false otherwise.'}, {'name': 'HighByteFirst', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether numbers are sent and received with the most significant\nbyte first.'}, {'name': 'IsAccepting', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns true if this BluetoothServer component is accepting an\nincoming connection.'}, {'name': 'IsConnected', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns frue if a connection to a Bluetooth device has been made.'}, {'name': 'Secure', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether a secure connection should be used.'}], 'events': [{'name': 'ConnectionAccepted', 'args': [], 'desc': 'Indicates that a bluetooth connection has been accepted.'}], 'methods': [{'name': 'AcceptConnection', 'args': [{'name': 'serviceName', 'type': 'str'}], 'returns': None, 'desc': 'Accept an incoming connection with the Serial Port Profile (SPP).'}, {'name': 'AcceptConnectionWithUUID', 'args': [{'name': 'serviceName', 'type': 'str'}, {'name': 'uuid', 'type': 'str'}], 'returns': None, 'desc': 'Accept an incoming connection with a specific UUID.'}, {'name': 'BytesAvailableToReceive', 'args': [], 'returns': 'int', 'desc': 'Returns number of bytes available from the input stream.'}, {'name': 'Disconnect', 'args': [], 'returns': None, 'desc': 'Disconnects from the connected Bluetooth device.'}, {'name': 'ReceiveSigned1ByteNumber', 'args': [], 'returns': 'int', 'desc': 'Reads a signed 1-byte number.'}, {'name': 'ReceiveSigned2ByteNumber', 'args': [], 'returns': 'int', 'desc': 'Reads a signed 2-byte number.'}, {'name': 'ReceiveSigned4ByteNumber', 'args': [], 'returns': 'int', 'desc': 'Reads a signed 4-byte number.'}, {'name': 'ReceiveSignedBytes', 'args': [{'name': 'numberOfBytes', 'type': 'int'}], 'returns': 'list', 'desc': 'Reads a number of signed bytes from the input stream and returns them as\na List.\n\n   If numberOfBytes is negative, this method reads until a delimiter byte\nvalue is read. The delimiter byte value is included in the returned list.\n'}, {'name': 'ReceiveText', 'args': [{'name': 'numberOfBytes', 'type': 'int'}], 'returns': 'str', 'desc': 'Reads a number of bytes from the input stream and converts them to text.\n\n   If numberOfBytes is negative, read until a delimiter byte value is read.\n'}, {'name': 'ReceiveUnsigned1ByteNumber', 'args': [], 'returns': 'int', 'desc': 'Reads an unsigned 1-byte number.'}, {'name': 'ReceiveUnsigned2ByteNumber', 'args': [], 'returns': 'int', 'desc': 'Reads an unsigned 2-byte number.'}, {'name': 'ReceiveUnsigned4ByteNumber', 'args': [], 'returns': 'int', 'desc': 'Reads an unsigned 4-byte number.'}, {'name': 'ReceiveUnsignedBytes', 'args': [{'name': 'numberOfBytes', 'type': 'int'}], 'returns': 'list', 'desc': 'Reads a number of unsigned bytes from the input stream and returns them as\na List.\n\n   If numberOfBytes is negative, this method reads until a delimiter byte\nvalue is read. The delimiter byte value is included in the returned list.\n'}, {'name': 'Send1ByteNumber', 'args': [{'name': 'number', 'type': 'str'}], 'returns': None, 'desc': "Decodes the given number String to an integer and writes it as one byte\nto the output stream.\n\n   If the number could not be decoded to an integer, or the integer would not\nfit in one byte, then the Form's ErrorOccurred event is triggered and this\nmethod returns without writing any bytes to the output stream.\n"}, {'name': 'Send2ByteNumber', 'args': [{'name': 'number', 'type': 'str'}], 'returns': None, 'desc': "Decodes the given number String to an integer and writes it as two bytes\nto the output stream.\n\n   If the number could not be decoded to an integer, or the integer would not\nfit in two bytes, then the Form's ErrorOccurred event is triggered and this\nmethod returns without writing any bytes to the output stream.\n"}, {'name': 'Send4ByteNumber', 'args': [{'name': 'number', 'type': 'str'}], 'returns': None, 'desc': "Decodes the given number String to an integer and writes it as four bytes\nto the output stream.\n\n   If the number could not be decoded to an integer, or the integer would not\nfit in four bytes, then the Form's ErrorOccurred event is triggered and this\nmethod returns without writing any bytes to the output stream.\n"}, {'name': 'SendBytes', 'args': [{'name': 'list', 'type': 'list'}], 'returns': None, 'desc': "Takes each element from the given list, converts it to a String, decodes\nthe String to an integer, and writes it as one byte to the output stream.\n\n   If an element could not be decoded to an integer, or the integer would not\nfit in one byte, then the Form's ErrorOccurred event is triggered and this\nmethod returns without writing any bytes to the output stream.\n"}, {'name': 'SendText', 'args': [{'name': 'text', 'type': 'str'}], 'returns': None, 'desc': 'Converts the given text to bytes and writes them to the output stream.'}, {'name': 'StopAccepting', 'args': [], 'returns': None, 'desc': 'Stop accepting an incoming connection.'}]}

    def __init__(self, /, *, parent: Component=..., CharacterEncoding: str=..., DelimiterByte: int=..., HighByteFirst: bool=..., Secure: bool=...):
        raise NotImplementedError

    @property
    def Available(self) -> bool:
        """Returns true if Bluetooth is available on the device,
false otherwise."""
        raise NotImplementedError

    @property
    def CharacterEncoding(self) -> str:
        """Returns the character encoding to use when sending and receiving text."""
        raise NotImplementedError

    @CharacterEncoding.setter
    def CharacterEncoding(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def DelimiterByte(self) -> int:
        """Returns the delimiter byte to use when passing a negative number for the
numberOfBytes parameter when calling ReceiveText, ReceiveSignedBytes, or
ReceiveUnsignedBytes."""
        raise NotImplementedError

    @DelimiterByte.setter
    def DelimiterByte(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Enabled(self) -> bool:
        """Returns true if Bluetooth is enabled, false otherwise."""
        raise NotImplementedError

    @property
    def HighByteFirst(self) -> bool:
        """Specifies whether numbers are sent and received with the most significant
byte first."""
        raise NotImplementedError

    @HighByteFirst.setter
    def HighByteFirst(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def IsAccepting(self) -> bool:
        """Returns true if this BluetoothServer component is accepting an
incoming connection."""
        raise NotImplementedError

    @property
    def IsConnected(self) -> bool:
        """Returns frue if a connection to a Bluetooth device has been made."""
        raise NotImplementedError

    @property
    def Secure(self) -> bool:
        """Specifies whether a secure connection should be used."""
        raise NotImplementedError

    @Secure.setter
    def Secure(self, value: bool, /) -> None:
        raise NotImplementedError

    def AcceptConnection(self, serviceName: str, /) -> None:
        """Accept an incoming connection with the Serial Port Profile (SPP)."""
        raise NotImplementedError

    def AcceptConnectionWithUUID(self, serviceName: str, uuid: str, /) -> None:
        """Accept an incoming connection with a specific UUID."""
        raise NotImplementedError

    def BytesAvailableToReceive(self, /) -> int:
        """Returns number of bytes available from the input stream."""
        raise NotImplementedError

    def Disconnect(self, /) -> None:
        """Disconnects from the connected Bluetooth device."""
        raise NotImplementedError

    def ReceiveSigned1ByteNumber(self, /) -> int:
        """Reads a signed 1-byte number."""
        raise NotImplementedError

    def ReceiveSigned2ByteNumber(self, /) -> int:
        """Reads a signed 2-byte number."""
        raise NotImplementedError

    def ReceiveSigned4ByteNumber(self, /) -> int:
        """Reads a signed 4-byte number."""
        raise NotImplementedError

    def ReceiveSignedBytes(self, numberOfBytes: int, /) -> list:
        """Reads a number of signed bytes from the input stream and returns them as
a List.

   If numberOfBytes is negative, this method reads until a delimiter byte
value is read. The delimiter byte value is included in the returned list.
"""
        raise NotImplementedError

    def ReceiveText(self, numberOfBytes: int, /) -> str:
        """Reads a number of bytes from the input stream and converts them to text.

   If numberOfBytes is negative, read until a delimiter byte value is read.
"""
        raise NotImplementedError

    def ReceiveUnsigned1ByteNumber(self, /) -> int:
        """Reads an unsigned 1-byte number."""
        raise NotImplementedError

    def ReceiveUnsigned2ByteNumber(self, /) -> int:
        """Reads an unsigned 2-byte number."""
        raise NotImplementedError

    def ReceiveUnsigned4ByteNumber(self, /) -> int:
        """Reads an unsigned 4-byte number."""
        raise NotImplementedError

    def ReceiveUnsignedBytes(self, numberOfBytes: int, /) -> list:
        """Reads a number of unsigned bytes from the input stream and returns them as
a List.

   If numberOfBytes is negative, this method reads until a delimiter byte
value is read. The delimiter byte value is included in the returned list.
"""
        raise NotImplementedError

    def Send1ByteNumber(self, number: str, /) -> None:
        """Decodes the given number String to an integer and writes it as one byte
to the output stream.

   If the number could not be decoded to an integer, or the integer would not
fit in one byte, then the Form's ErrorOccurred event is triggered and this
method returns without writing any bytes to the output stream.
"""
        raise NotImplementedError

    def Send2ByteNumber(self, number: str, /) -> None:
        """Decodes the given number String to an integer and writes it as two bytes
to the output stream.

   If the number could not be decoded to an integer, or the integer would not
fit in two bytes, then the Form's ErrorOccurred event is triggered and this
method returns without writing any bytes to the output stream.
"""
        raise NotImplementedError

    def Send4ByteNumber(self, number: str, /) -> None:
        """Decodes the given number String to an integer and writes it as four bytes
to the output stream.

   If the number could not be decoded to an integer, or the integer would not
fit in four bytes, then the Form's ErrorOccurred event is triggered and this
method returns without writing any bytes to the output stream.
"""
        raise NotImplementedError

    def SendBytes(self, list: list, /) -> None:
        """Takes each element from the given list, converts it to a String, decodes
the String to an integer, and writes it as one byte to the output stream.

   If an element could not be decoded to an integer, or the integer would not
fit in one byte, then the Form's ErrorOccurred event is triggered and this
method returns without writing any bytes to the output stream.
"""
        raise NotImplementedError

    def SendText(self, text: str, /) -> None:
        """Converts the given text to bytes and writes them to the output stream."""
        raise NotImplementedError

    def StopAccepting(self, /) -> None:
        """Stop accepting an incoming connection."""
        raise NotImplementedError

    def on_ConnectionAccepted(self, callback: Callable[[], None], /) -> None:
        """ConnectionAccepted()

Indicates that a bluetooth connection has been accepted."""
        raise NotImplementedError

    @staticmethod
    def on_any_ConnectionAccepted(callback: Callable[['BluetoothServer', bool], None], /) -> None:
        """ConnectionAccepted()

Indicates that a bluetooth connection has been accepted."""
        raise NotImplementedError

class Serial(Component):
    """Component for Serial"""
    __data__ = {'desc': 'Component for Serial', 'properties': [{'name': 'BaudRate', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Returns the current baud rate'}, {'name': 'BufferSize', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Returns the buffer size in bytes'}, {'name': 'IsInitialized', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns true when the Serial has been initialized.'}, {'name': 'IsOpen', 'type': 'bool', 'ro': True, 'do': False, 'bo': True, 'desc': 'Returns true when the Serial connection is open.'}], 'events': [], 'methods': [{'name': 'CloseSerial', 'args': [], 'returns': 'bool', 'desc': 'Closes serial connection. Returns true when closed.'}, {'name': 'InitializeSerial', 'args': [], 'returns': None, 'desc': 'Initializes serial connection.'}, {'name': 'OpenSerial', 'args': [], 'returns': 'bool', 'desc': 'Opens serial connection. Returns true when opened.'}, {'name': 'PrintSerial', 'args': [{'name': 'data', 'type': 'str'}], 'returns': None, 'desc': 'Writes given data to serial, and appends a new line at the end.'}, {'name': 'ReadSerial', 'args': [], 'returns': 'str', 'desc': 'Reads data from serial.'}, {'name': 'WriteSerial', 'args': [{'name': 'data', 'type': 'str'}], 'returns': None, 'desc': 'Writes given data to serial.'}]}

    def __init__(self, /, *, parent: Component=..., BaudRate: int=..., BufferSize: int=...):
        raise NotImplementedError

    @property
    def BaudRate(self) -> int:
        """Returns the current baud rate"""
        raise NotImplementedError

    @BaudRate.setter
    def BaudRate(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def BufferSize(self) -> int:
        """Returns the buffer size in bytes"""
        raise NotImplementedError

    @BufferSize.setter
    def BufferSize(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def IsInitialized(self) -> bool:
        """Returns true when the Serial has been initialized."""
        raise NotImplementedError

    @property
    def IsOpen(self) -> bool:
        """Returns true when the Serial connection is open."""
        raise NotImplementedError

    def CloseSerial(self, /) -> bool:
        """Closes serial connection. Returns true when closed."""
        raise NotImplementedError

    def InitializeSerial(self, /) -> None:
        """Initializes serial connection."""
        raise NotImplementedError

    def OpenSerial(self, /) -> bool:
        """Opens serial connection. Returns true when opened."""
        raise NotImplementedError

    def PrintSerial(self, data: str, /) -> None:
        """Writes given data to serial, and appends a new line at the end."""
        raise NotImplementedError

    def ReadSerial(self, /) -> str:
        """Reads data from serial."""
        raise NotImplementedError

    def WriteSerial(self, data: str, /) -> None:
        """Writes given data to serial."""
        raise NotImplementedError

class Web(Component):
    """Non-visible component that provides functions for HTTP GET, POST, PUT, and DELETE requests."""
    __data__ = {'desc': 'Non-visible component that provides functions for HTTP GET, POST, PUT, and DELETE requests.', 'properties': [{'name': 'AllowCookies', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether cookies should be allowed'}, {'name': 'RequestHeaders', 'type': 'list', 'ro': False, 'do': False, 'bo': True, 'desc': 'Sets the request headers.'}, {'name': 'ResponseFileName', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the name of the file where the response should be saved.\nIf SaveResponse is true and ResponseFileName is empty, then a new file\nname will be generated.'}, {'name': 'SaveResponse', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the response should be saved in a file.'}, {'name': 'Timeout', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Returns the number of milliseconds that each request will wait for a response before they time out.\nIf set to 0, then the request will wait for a response indefinitely.'}, {'name': 'Url', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the URL.'}], 'events': [{'name': 'GotFile', 'args': [{'name': 'url', 'type': 'str'}, {'name': 'responseCode', 'type': 'int'}, {'name': 'responseType', 'type': 'str'}, {'name': 'fileName', 'type': 'str'}], 'desc': 'Event indicating that a request has finished.'}, {'name': 'GotText', 'args': [{'name': 'url', 'type': 'str'}, {'name': 'responseCode', 'type': 'int'}, {'name': 'responseType', 'type': 'str'}, {'name': 'responseContent', 'type': 'str'}], 'desc': 'Event indicating that a request has finished.'}, {'name': 'TimedOut', 'args': [{'name': 'url', 'type': 'str'}], 'desc': 'Event indicating that a request has timed out.'}], 'methods': [{'name': 'BuildRequestData', 'args': [{'name': 'list', 'type': 'list'}], 'returns': 'str', 'desc': 'Converts a list of two-element sublists, representing name and value pairs, to a\nstring formatted as application/x-www-form-urlencoded media type, suitable to pass to\nPostText.'}, {'name': 'ClearCookies', 'args': [], 'returns': None, 'desc': 'Clears all cookies for this Web component.'}, {'name': 'Delete', 'args': [], 'returns': None, 'desc': 'Performs an HTTP DELETE request using the Url property and retrieves the\nresponse.\n\n   If the SaveResponse property is true, the response will be saved in a file\nand the GotFile event will be triggered. The ResponseFileName property\ncan be used to specify the name of the file.\nIf the SaveResponse property is false, the GotText event will be\ntriggered.\n'}, {'name': 'Get', 'args': [], 'returns': None, 'desc': 'Performs an HTTP GET request using the Url property and retrieves the\nresponse.\n\n   If the SaveResponse property is true, the response will be saved in a file\nand the GotFile event will be triggered. The ResponseFileName property\ncan be used to specify the name of the file.\nIf the SaveResponse property is false, the GotText event will be\ntriggered.\n'}, {'name': 'HtmlTextDecode', 'args': [{'name': 'htmlText', 'type': 'str'}], 'returns': 'str', 'desc': 'Decodes the given HTML text value.\n\n   HTML Character Entities such as &amp;, &lt;, &gt;, &apos;, and &quot; are\nchanged to &, <, >, \', and ".\nEntities such as &#xhhhh;, and &#nnnn; are changed to the appropriate characters.\n'}, {'name': 'JsonObjectEncode', 'args': [{'name': 'jsonObject', 'type': 'Any'}], 'returns': 'str', 'desc': "Returns the value of a built-in type (i.e., boolean, number, text, list, dictionary)\nin its JavaScript Object Notation representation. If the value cannot be\nrepresented as JSON, the Screen's ErrorOccurred event will be run, if any,\nand the Web component will return the empty string."}, {'name': 'JsonTextDecode', 'args': [{'name': 'jsonText', 'type': 'str'}], 'returns': 'Any', 'desc': 'Decodes the given JSON encoded value to produce a corresponding AppInventor value.\nA JSON list [x, y, z] decodes to a list (x y z),  A JSON object with key A and value B,\n(denoted as {A:B}) decodes to a list ((A B)), that is, a list containing the two-element\nlist (A B).\n\n   Use the method JsonTextDecodeWithDictionaries if you\nwould prefer to get back dictionary objects rather than lists-of-lists in the result.\n'}, {'name': 'JsonTextDecodeWithDictionaries', 'args': [{'name': 'jsonText', 'type': 'str'}], 'returns': 'Any', 'desc': 'Decodes the given JSON encoded value to produce a corresponding App Inventor value.\nA JSON list [x, y, z] decodes to a list (x y z). A JSON Object with name A and value B,\ndenoted as {a: b} decodes to a dictionary with the key a and value b.'}, {'name': 'PatchFile', 'args': [{'name': 'path', 'type': 'str'}], 'returns': None, 'desc': 'Performs an HTTP PATCH request using the Url property and data from the specified file.\n\n   If the SaveResponse property is true, the response will be saved in a file\nand the GotFile event will be triggered. The ResponseFileName property can be\nused to specify the name of the file.\nIf the SaveResponse property is false, the GotText event will be triggered.\n'}, {'name': 'PatchText', 'args': [{'name': 'text', 'type': 'str'}], 'returns': None, 'desc': 'Performs an HTTP PATCH request using the Url property and the specified text.\n\n   The characters of the text are encoded using UTF-8 encoding.\nIf the SaveResponse property is true, the response will be saved in a\nfile and the GotFile event will be triggered. The responseFileName property\ncan be used to specify the name of the file.\nIf the SaveResponse property is false, the GotText event will be triggered.\n'}, {'name': 'PatchTextWithEncoding', 'args': [{'name': 'text', 'type': 'str'}, {'name': 'encoding', 'type': 'str'}], 'returns': None, 'desc': 'Performs an HTTP PATCH request using the Url property and the specified text.\n\n   The characters of the text are encoded using the given encoding.\nIf the SaveResponse property is true, the response will be saved in a\nfile and the GotFile event will be triggered. The ResponseFileName property\ncan be used to specify the name of the file.\nIf the SaveResponse property is false, the GotText event will be triggered.\n'}, {'name': 'PostFile', 'args': [{'name': 'path', 'type': 'str'}], 'returns': None, 'desc': 'Performs an HTTP POST request using the Url property and data from the specified file.\n\n   If the SaveResponse property is true, the response will be saved in a file\nand the GotFile event will be triggered. The ResponseFileName property can be\nused to specify the name of the file.\nIf the SaveResponse property is false, the GotText event will be triggered.\n'}, {'name': 'PostText', 'args': [{'name': 'text', 'type': 'str'}], 'returns': None, 'desc': 'Performs an HTTP POST request using the Url property and the specified text.\n\n   The characters of the text are encoded using UTF-8 encoding.\nIf the SaveResponse property is true, the response will be saved in a\nfile and the GotFile event will be triggered. The responseFileName property\ncan be used to specify the name of the file.\nIf the SaveResponse property is false, the GotText event will be triggered.\n'}, {'name': 'PostTextWithEncoding', 'args': [{'name': 'text', 'type': 'str'}, {'name': 'encoding', 'type': 'str'}], 'returns': None, 'desc': 'Performs an HTTP POST request using the Url property and the specified text.\n\n   The characters of the text are encoded using the given encoding.\nIf the SaveResponse property is true, the response will be saved in a\nfile and the GotFile event will be triggered. The ResponseFileName property\ncan be used to specify the name of the file.\nIf the SaveResponse property is false, the GotText event will be triggered.\n'}, {'name': 'PutFile', 'args': [{'name': 'path', 'type': 'str'}], 'returns': None, 'desc': 'Performs an HTTP PUT request using the Url property and data from the specified file.\n\n   If the SaveResponse property is true, the response will be saved in a file\nand the GotFile event will be triggered. The ResponseFileName property can be\nused to specify the name of the file.\nIf the SaveResponse property is false, the GotText event will be triggered.\n'}, {'name': 'PutText', 'args': [{'name': 'text', 'type': 'str'}], 'returns': None, 'desc': 'Performs an HTTP PUT request using the Url property and the specified text.\n\n   The characters of the text are encoded using UTF-8 encoding.\nIf the SaveResponse property is true, the response will be saved in a\nfile and the GotFile event will be triggered. The responseFileName property\ncan be used to specify the name of the file.\nIf the SaveResponse property is false, the GotText event will be triggered.\n'}, {'name': 'PutTextWithEncoding', 'args': [{'name': 'text', 'type': 'str'}, {'name': 'encoding', 'type': 'str'}], 'returns': None, 'desc': 'Performs an HTTP PUT request using the Url property and the specified text.\n\n   The characters of the text are encoded using the given encoding.\nIf the SaveResponse property is true, the response will be saved in a\nfile and the GotFile event will be triggered. The ResponseFileName property\ncan be used to specify the name of the file.\nIf the SaveResponse property is false, the GotText event will be triggered.\n'}, {'name': 'UriDecode', 'args': [{'name': 'text', 'type': 'str'}], 'returns': 'str', 'desc': "Decodes the encoded text value so that the values aren't URL encoded anymore."}, {'name': 'UriEncode', 'args': [{'name': 'text', 'type': 'str'}], 'returns': 'str', 'desc': 'Encodes the given text value so that it can be used in a URL.'}, {'name': 'XMLTextDecode', 'args': [{'name': 'XmlText', 'type': 'str'}], 'returns': 'Any', 'desc': 'Decodes the given XML string to produce a list structure. <tag>string</tag> decodes to\na list that contains a pair of tag and string.  More generally, if obj1, obj2, â\x80¦\nare tag-delimited XML strings, then <tag>obj1 obj2 ...</tag> decodes to a list\nthat contains a pair whose first element is tag and whose second element is the\nlist of the decoded obj\'s, ordered alphabetically by tags.\n\n   Examples:\n\n<foo><123/foo> decodes to a one-item list containing the pair (foo 123)\n<foo>1 2 3</foo> decodes to a one-item list containing the pair (foo "1 2 3")\n<a><foo>1 2 3</foo><bar>456</bar></a> decodes to a list containing the pair (a X)\nwhere X is a 2-item list that contains the pair (bar 123) and the pair (foo "1 2 3").\n\nIf the sequence of obj\'s mixes tag-delimited and non-tag-delimited items, then the\nnon-tag-delimited items are pulled out of the sequence and wrapped with a "content" tag.\nFor example, decoding <a><bar>456</bar>many<foo>1 2 3</foo>apples<a></code>\nis similar to above, except that the list X is a 3-item list that contains the additional pair\nwhose first item is the string "content", and whose second item is the list (many, apples).\nThis method signals an error and returns the empty list if the result is not well-formed XML.\n'}, {'name': 'XMLTextDecodeAsDictionary', 'args': [{'name': 'XmlText', 'type': 'str'}], 'returns': 'Any', 'desc': 'Decodes the given XML string to produce a dictionary structure. The dictionary includes the\nspecial keys $tag, $localName, $namespace, $namespaceUri, $attributes, and $content,\nas well as a key for each unique tag for every node, which points to a list of elements of\nthe same structure as described here.\n\n   The $tag key is the full tag name, e.g., foo:bar. The $localName is the local portion of\nthe name (everything after the colon : character). If a namespace is given (everything before\nthe colon : character), it is provided in $namespace and the corresponding URI is given\nin $namespaceUri. The attributes are stored in a dictionary in $attributes and the\nchild nodes are given as a list under $content.\nMore Information on Special Keys\nConsider the following XML document:\n  <ex:Book xmlns:ex="http://example.com/">\n    <ex:title xml:lang="en">On the Origin of Species</ex:title>\n    <ex:author>Charles Darwin</ex:author>\n  </ex:Book>\n\nWhen parsed, the $tag key will be "ex:Book", the $localName key will be "Book", the\n$namespace key will be "ex", $namespaceUri will be "http://example.com/", the\n$attributes key will be a dictionary {} (xmlns is removed for the namespace), and the\n$content will be a list of two items representing the decoded <ex:title> and <ex:author>\nelements. The first item, which corresponds to the <ex:title> element, will have an\n$attributes key containing the dictionary {"xml:lang": "en"}. For each name=value\nattribute on an element, a key-value pair mapping name to value will exist in the\n$attributes dictionary. In addition to these special keys, there will also be "ex:title"\nand "ex:author" to allow lookups faster than having to traverse the $content list.\n'}]}

    def __init__(self, /, *, parent: Component=..., AllowCookies: bool=..., ResponseFileName: str=..., SaveResponse: bool=..., Timeout: int=..., Url: str=...):
        raise NotImplementedError

    @property
    def AllowCookies(self) -> bool:
        """Specifies whether cookies should be allowed"""
        raise NotImplementedError

    @AllowCookies.setter
    def AllowCookies(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def RequestHeaders(self) -> list:
        """Sets the request headers."""
        raise NotImplementedError

    @RequestHeaders.setter
    def RequestHeaders(self, value: list, /) -> None:
        raise NotImplementedError

    @property
    def ResponseFileName(self) -> str:
        """Specifies the name of the file where the response should be saved.
If SaveResponse is true and ResponseFileName is empty, then a new file
name will be generated."""
        raise NotImplementedError

    @ResponseFileName.setter
    def ResponseFileName(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def SaveResponse(self) -> bool:
        """Specifies whether the response should be saved in a file."""
        raise NotImplementedError

    @SaveResponse.setter
    def SaveResponse(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Timeout(self) -> int:
        """Returns the number of milliseconds that each request will wait for a response before they time out.
If set to 0, then the request will wait for a response indefinitely."""
        raise NotImplementedError

    @Timeout.setter
    def Timeout(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Url(self) -> str:
        """Specifies the URL."""
        raise NotImplementedError

    @Url.setter
    def Url(self, value: str, /) -> None:
        raise NotImplementedError

    def BuildRequestData(self, list: list, /) -> str:
        """Converts a list of two-element sublists, representing name and value pairs, to a
string formatted as application/x-www-form-urlencoded media type, suitable to pass to
PostText."""
        raise NotImplementedError

    def ClearCookies(self, /) -> None:
        """Clears all cookies for this Web component."""
        raise NotImplementedError

    def Delete(self, /) -> None:
        """Performs an HTTP DELETE request using the Url property and retrieves the
response.

   If the SaveResponse property is true, the response will be saved in a file
and the GotFile event will be triggered. The ResponseFileName property
can be used to specify the name of the file.
If the SaveResponse property is false, the GotText event will be
triggered.
"""
        raise NotImplementedError

    def Get(self, /) -> None:
        """Performs an HTTP GET request using the Url property and retrieves the
response.

   If the SaveResponse property is true, the response will be saved in a file
and the GotFile event will be triggered. The ResponseFileName property
can be used to specify the name of the file.
If the SaveResponse property is false, the GotText event will be
triggered.
"""
        raise NotImplementedError

    def HtmlTextDecode(self, htmlText: str, /) -> str:
        """Decodes the given HTML text value.

   HTML Character Entities such as &amp;, &lt;, &gt;, &apos;, and &quot; are
changed to &, <, >, ', and ".
Entities such as &#xhhhh;, and &#nnnn; are changed to the appropriate characters.
"""
        raise NotImplementedError

    def JsonObjectEncode(self, jsonObject: Any, /) -> str:
        """Returns the value of a built-in type (i.e., boolean, number, text, list, dictionary)
in its JavaScript Object Notation representation. If the value cannot be
represented as JSON, the Screen's ErrorOccurred event will be run, if any,
and the Web component will return the empty string."""
        raise NotImplementedError

    def JsonTextDecode(self, jsonText: str, /) -> Any:
        """Decodes the given JSON encoded value to produce a corresponding AppInventor value.
A JSON list [x, y, z] decodes to a list (x y z),  A JSON object with key A and value B,
(denoted as {A:B}) decodes to a list ((A B)), that is, a list containing the two-element
list (A B).

   Use the method JsonTextDecodeWithDictionaries if you
would prefer to get back dictionary objects rather than lists-of-lists in the result.
"""
        raise NotImplementedError

    def JsonTextDecodeWithDictionaries(self, jsonText: str, /) -> Any:
        """Decodes the given JSON encoded value to produce a corresponding App Inventor value.
A JSON list [x, y, z] decodes to a list (x y z). A JSON Object with name A and value B,
denoted as {a: b} decodes to a dictionary with the key a and value b."""
        raise NotImplementedError

    def PatchFile(self, path: str, /) -> None:
        """Performs an HTTP PATCH request using the Url property and data from the specified file.

   If the SaveResponse property is true, the response will be saved in a file
and the GotFile event will be triggered. The ResponseFileName property can be
used to specify the name of the file.
If the SaveResponse property is false, the GotText event will be triggered.
"""
        raise NotImplementedError

    def PatchText(self, text: str, /) -> None:
        """Performs an HTTP PATCH request using the Url property and the specified text.

   The characters of the text are encoded using UTF-8 encoding.
If the SaveResponse property is true, the response will be saved in a
file and the GotFile event will be triggered. The responseFileName property
can be used to specify the name of the file.
If the SaveResponse property is false, the GotText event will be triggered.
"""
        raise NotImplementedError

    def PatchTextWithEncoding(self, text: str, encoding: str, /) -> None:
        """Performs an HTTP PATCH request using the Url property and the specified text.

   The characters of the text are encoded using the given encoding.
If the SaveResponse property is true, the response will be saved in a
file and the GotFile event will be triggered. The ResponseFileName property
can be used to specify the name of the file.
If the SaveResponse property is false, the GotText event will be triggered.
"""
        raise NotImplementedError

    def PostFile(self, path: str, /) -> None:
        """Performs an HTTP POST request using the Url property and data from the specified file.

   If the SaveResponse property is true, the response will be saved in a file
and the GotFile event will be triggered. The ResponseFileName property can be
used to specify the name of the file.
If the SaveResponse property is false, the GotText event will be triggered.
"""
        raise NotImplementedError

    def PostText(self, text: str, /) -> None:
        """Performs an HTTP POST request using the Url property and the specified text.

   The characters of the text are encoded using UTF-8 encoding.
If the SaveResponse property is true, the response will be saved in a
file and the GotFile event will be triggered. The responseFileName property
can be used to specify the name of the file.
If the SaveResponse property is false, the GotText event will be triggered.
"""
        raise NotImplementedError

    def PostTextWithEncoding(self, text: str, encoding: str, /) -> None:
        """Performs an HTTP POST request using the Url property and the specified text.

   The characters of the text are encoded using the given encoding.
If the SaveResponse property is true, the response will be saved in a
file and the GotFile event will be triggered. The ResponseFileName property
can be used to specify the name of the file.
If the SaveResponse property is false, the GotText event will be triggered.
"""
        raise NotImplementedError

    def PutFile(self, path: str, /) -> None:
        """Performs an HTTP PUT request using the Url property and data from the specified file.

   If the SaveResponse property is true, the response will be saved in a file
and the GotFile event will be triggered. The ResponseFileName property can be
used to specify the name of the file.
If the SaveResponse property is false, the GotText event will be triggered.
"""
        raise NotImplementedError

    def PutText(self, text: str, /) -> None:
        """Performs an HTTP PUT request using the Url property and the specified text.

   The characters of the text are encoded using UTF-8 encoding.
If the SaveResponse property is true, the response will be saved in a
file and the GotFile event will be triggered. The responseFileName property
can be used to specify the name of the file.
If the SaveResponse property is false, the GotText event will be triggered.
"""
        raise NotImplementedError

    def PutTextWithEncoding(self, text: str, encoding: str, /) -> None:
        """Performs an HTTP PUT request using the Url property and the specified text.

   The characters of the text are encoded using the given encoding.
If the SaveResponse property is true, the response will be saved in a
file and the GotFile event will be triggered. The ResponseFileName property
can be used to specify the name of the file.
If the SaveResponse property is false, the GotText event will be triggered.
"""
        raise NotImplementedError

    def UriDecode(self, text: str, /) -> str:
        """Decodes the encoded text value so that the values aren't URL encoded anymore."""
        raise NotImplementedError

    def UriEncode(self, text: str, /) -> str:
        """Encodes the given text value so that it can be used in a URL."""
        raise NotImplementedError

    def XMLTextDecode(self, XmlText: str, /) -> Any:
        """Decodes the given XML string to produce a list structure. <tag>string</tag> decodes to
a list that contains a pair of tag and string.  More generally, if obj1, obj2, â\x80¦
are tag-delimited XML strings, then <tag>obj1 obj2 ...</tag> decodes to a list
that contains a pair whose first element is tag and whose second element is the
list of the decoded obj's, ordered alphabetically by tags.

   Examples:

<foo><123/foo> decodes to a one-item list containing the pair (foo 123)
<foo>1 2 3</foo> decodes to a one-item list containing the pair (foo "1 2 3")
<a><foo>1 2 3</foo><bar>456</bar></a> decodes to a list containing the pair (a X)
where X is a 2-item list that contains the pair (bar 123) and the pair (foo "1 2 3").

If the sequence of obj's mixes tag-delimited and non-tag-delimited items, then the
non-tag-delimited items are pulled out of the sequence and wrapped with a "content" tag.
For example, decoding <a><bar>456</bar>many<foo>1 2 3</foo>apples<a></code>
is similar to above, except that the list X is a 3-item list that contains the additional pair
whose first item is the string "content", and whose second item is the list (many, apples).
This method signals an error and returns the empty list if the result is not well-formed XML.
"""
        raise NotImplementedError

    def XMLTextDecodeAsDictionary(self, XmlText: str, /) -> Any:
        """Decodes the given XML string to produce a dictionary structure. The dictionary includes the
special keys $tag, $localName, $namespace, $namespaceUri, $attributes, and $content,
as well as a key for each unique tag for every node, which points to a list of elements of
the same structure as described here.

   The $tag key is the full tag name, e.g., foo:bar. The $localName is the local portion of
the name (everything after the colon : character). If a namespace is given (everything before
the colon : character), it is provided in $namespace and the corresponding URI is given
in $namespaceUri. The attributes are stored in a dictionary in $attributes and the
child nodes are given as a list under $content.
More Information on Special Keys
Consider the following XML document:
  <ex:Book xmlns:ex="http://example.com/">
    <ex:title xml:lang="en">On the Origin of Species</ex:title>
    <ex:author>Charles Darwin</ex:author>
  </ex:Book>

When parsed, the $tag key will be "ex:Book", the $localName key will be "Book", the
$namespace key will be "ex", $namespaceUri will be "http://example.com/", the
$attributes key will be a dictionary {} (xmlns is removed for the namespace), and the
$content will be a list of two items representing the decoded <ex:title> and <ex:author>
elements. The first item, which corresponds to the <ex:title> element, will have an
$attributes key containing the dictionary {"xml:lang": "en"}. For each name=value
attribute on an element, a key-value pair mapping name to value will exist in the
$attributes dictionary. In addition to these special keys, there will also be "ex:title"
and "ex:author" to allow lookups faster than having to traverse the $content list.
"""
        raise NotImplementedError

    def on_GotFile(self, callback: Callable[[str, int, str, str], None], /) -> None:
        """GotFile(url, responseCode, responseType, fileName)

Event indicating that a request has finished."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotFile(callback: Callable[['Web', bool, str, int, str, str], None], /) -> None:
        """GotFile(url, responseCode, responseType, fileName)

Event indicating that a request has finished."""
        raise NotImplementedError

    def on_GotText(self, callback: Callable[[str, int, str, str], None], /) -> None:
        """GotText(url, responseCode, responseType, responseContent)

Event indicating that a request has finished."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotText(callback: Callable[['Web', bool, str, int, str, str], None], /) -> None:
        """GotText(url, responseCode, responseType, responseContent)

Event indicating that a request has finished."""
        raise NotImplementedError

    def on_TimedOut(self, callback: Callable[[str], None], /) -> None:
        """TimedOut(url)

Event indicating that a request has timed out."""
        raise NotImplementedError

    @staticmethod
    def on_any_TimedOut(callback: Callable[['Web', bool, str], None], /) -> None:
        """TimedOut(url)

Event indicating that a request has timed out."""
        raise NotImplementedError

class ChatBot(Component):
    """The ChatBot component is a non-visible component for chatting with an AI
chatbot. This version uses a proxy run by MIT that in turn uses the ChatGPT
generative large language model."""
    __data__ = {'desc': 'The ChatBot component is a non-visible component for chatting with an AI\nchatbot. This version uses a proxy run by MIT that in turn uses the ChatGPT\ngenerative large language model.', 'properties': [{'name': 'ApiKey', 'type': 'str', 'ro': False, 'do': False, 'bo': True, 'desc': 'An ApiKey for ChatGPT. User supplied. If provided, we will use it instead of the\nAPI key embedded in the chat proxy service.'}, {'name': 'Model', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Set the name of the model to use. See https://appinv.us/chatbot for the current list of supported models. Leaving this blank will result in the default model set by the provider being used'}, {'name': 'Provider', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Set the name of the provider to use. See https://appinv.us/chatbot for the current list of supported providers.'}, {'name': 'System', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'The "System" value given to ChatGPT. It is used to set the tone of a conversation. For example: "You are a funny person."'}, {'name': 'Token', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'The MIT Access token to use. MIT App Inventor will automatically fill this\nvalue in. You should not need to change it.'}], 'events': [{'name': 'ErrorOccurred', 'args': [{'name': 'responseCode', 'type': 'int'}, {'name': 'responseText', 'type': 'str'}], 'desc': 'The ErrorOccurred event will be run when an error occurs during\nprocessing, such as if your you are over usage quota, or some\nother error signaled by ChatGPT or PaLM. See\nhttps://appinv.us/chatbot for current information.'}, {'name': 'GotResponse', 'args': [{'name': 'responseText', 'type': 'str'}], 'desc': 'Event indicating that a request has finished and has returned data (output from ChatBot).'}], 'methods': [{'name': 'Converse', 'args': [{'name': 'question', 'type': 'str'}], 'returns': None, 'desc': 'Ask a question of the Chat Bot. Successive calls will remember information from earlier in the conversation. Use the "ResetConversation" function to reset for a new conversation.'}, {'name': 'ResetConversation', 'args': [], 'returns': None, 'desc': 'Reset the current conversation, Chat bot will forget any previous conversation when resonding in the future.'}]}

    def __init__(self, /, *, parent: Component=..., Model: str=..., Provider: str=..., System: str=..., Token: str=...):
        raise NotImplementedError

    @property
    def ApiKey(self) -> str:
        """An ApiKey for ChatGPT. User supplied. If provided, we will use it instead of the
API key embedded in the chat proxy service."""
        raise NotImplementedError

    @ApiKey.setter
    def ApiKey(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Model(self) -> str:
        """Set the name of the model to use. See https://appinv.us/chatbot for the current list of supported models. Leaving this blank will result in the default model set by the provider being used"""
        raise NotImplementedError

    @Model.setter
    def Model(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Provider(self) -> str:
        """Set the name of the provider to use. See https://appinv.us/chatbot for the current list of supported providers."""
        raise NotImplementedError

    @Provider.setter
    def Provider(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def System(self) -> str:
        '''The "System" value given to ChatGPT. It is used to set the tone of a conversation. For example: "You are a funny person."'''
        raise NotImplementedError

    @System.setter
    def System(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def Token(self) -> str:
        """The MIT Access token to use. MIT App Inventor will automatically fill this
value in. You should not need to change it."""
        raise NotImplementedError

    @Token.setter
    def Token(self, value: str, /) -> None:
        raise NotImplementedError

    def Converse(self, question: str, /) -> None:
        """Ask a question of the Chat Bot. Successive calls will remember information from earlier in the conversation. Use the "ResetConversation" function to reset for a new conversation."""
        raise NotImplementedError

    def ResetConversation(self, /) -> None:
        """Reset the current conversation, Chat bot will forget any previous conversation when resonding in the future."""
        raise NotImplementedError

    def on_ErrorOccurred(self, callback: Callable[[int, str], None], /) -> None:
        """ErrorOccurred(responseCode, responseText)

The ErrorOccurred event will be run when an error occurs during
processing, such as if your you are over usage quota, or some
other error signaled by ChatGPT or PaLM. See
https://appinv.us/chatbot for current information."""
        raise NotImplementedError

    @staticmethod
    def on_any_ErrorOccurred(callback: Callable[['ChatBot', bool, int, str], None], /) -> None:
        """ErrorOccurred(responseCode, responseText)

The ErrorOccurred event will be run when an error occurs during
processing, such as if your you are over usage quota, or some
other error signaled by ChatGPT or PaLM. See
https://appinv.us/chatbot for current information."""
        raise NotImplementedError

    def on_GotResponse(self, callback: Callable[[str], None], /) -> None:
        """GotResponse(responseText)

Event indicating that a request has finished and has returned data (output from ChatBot)."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotResponse(callback: Callable[['ChatBot', bool, str], None], /) -> None:
        """GotResponse(responseText)

Event indicating that a request has finished and has returned data (output from ChatBot)."""
        raise NotImplementedError

class FirebaseDB(Component):
    """The Firebase component communicates with a Web service to store
and retrieve information.  The component has methods to
store a value under a tag and to retrieve the value associated with
the tag. It also possesses a listener to fire events when stored
values are changed."""
    __data__ = {'desc': 'The Firebase component communicates with a Web service to store\nand retrieve information.  The component has methods to\nstore a value under a tag and to retrieve the value associated with\nthe tag. It also possesses a listener to fire events when stored\nvalues are changed.', 'properties': [{'name': 'DeveloperBucket', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'Getter for the DeveloperBucket.'}, {'name': 'FirebaseToken', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'Getter for the FirebaseToken.'}, {'name': 'FirebaseURL', 'type': 'str', 'ro': False, 'do': True, 'bo': False, 'desc': 'Specifies the URL for the Firebase.'}, {'name': 'Persist', 'type': 'bool', 'ro': False, 'do': True, 'bo': False, 'desc': 'If true, variables will retain their values when off-line and the App exits. Values will be uploaded to Firebase the next time the App is run while connected to the network. This is useful for applications which will gather data while not connected to the network. Note: AppendValue and RemoveFirst will not work correctly when off-line, they require a network connection. Note: If you set Persist on any Firebase component, on any screen, it makes all Firebase components on all screens persistent. This is a limitation of the low level Firebase library. Also be aware that if you want to set persist to true, you should do so before connecting the Companion for incremental development.'}, {'name': 'ProjectBucket', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'Getter for the ProjectBucket.'}], 'events': [{'name': 'DataChanged', 'args': [{'name': 'tag', 'type': 'str'}, {'name': 'value', 'type': 'Any'}], 'desc': 'Indicates that the data in the Firebase has changed.\nLaunches an event with the tag and value that have been updated.'}, {'name': 'FirebaseError', 'args': [{'name': 'message', 'type': 'str'}], 'desc': 'Indicates that the communication with the Firebase signaled an error.'}, {'name': 'FirstRemoved', 'args': [{'name': 'value', 'type': 'Any'}], 'desc': 'Event triggered by the "RemoveFirst" function. The argument "value" is the object that was the first in the list, and which is now removed.'}, {'name': 'GotValue', 'args': [{'name': 'tag', 'type': 'str'}, {'name': 'value', 'type': 'Any'}], 'desc': 'Indicates that a GetValue request has succeeded.'}, {'name': 'TagList', 'args': [{'name': 'value', 'type': 'list'}], 'desc': 'Event triggered when we have received the list of known tags. Used with the "GetTagList" Function.'}], 'methods': [{'name': 'AppendValue', 'args': [{'name': 'tag', 'type': 'str'}, {'name': 'valueToAdd', 'type': 'Any'}], 'returns': None, 'desc': 'Append a value to the end of a list atomically. If two devices use this function simultaneously, both will be appended and no data lost.'}, {'name': 'ClearTag', 'args': [{'name': 'tag', 'type': 'str'}], 'returns': None, 'desc': 'Asks Firebase to forget (delete or set to "null") a given tag.'}, {'name': 'GetTagList', 'args': [], 'returns': None, 'desc': 'Get the list of tags for this application. When complete a "TagList" event will be triggered with the list of known tags.'}, {'name': 'GetValue', 'args': [{'name': 'tag', 'type': 'str'}, {'name': 'valueIfTagNotThere', 'type': 'Any'}], 'returns': None, 'desc': 'GetValue asks Firebase to get the value stored under the given tag.\nIt will pass valueIfTagNotThere to GotValue if there is no value stored\nunder the tag.'}, {'name': 'RemoveFirst', 'args': [{'name': 'tag', 'type': 'str'}], 'returns': None, 'desc': 'Return the first element of a list and atomically remove it. If two devices use this function simultaneously, one will get the first element and the the other will get the second element, or an error if there is no available element. When the element is available, the "FirstRemoved" event will be triggered.'}, {'name': 'StoreValue', 'args': [{'name': 'tag', 'type': 'str'}, {'name': 'valueToStore', 'type': 'Any'}], 'returns': None, 'desc': 'Asks Firebase to store the given value under the given tag.'}, {'name': 'Unauthenticate', 'args': [], 'returns': None, 'desc': 'Unauthenticate from Firebase.\n\n   Firebase keeps track of credentials in a cache in shared_prefs\nIt will re-use these credentials as long as they are valid. Given\nThat we retrieve a FirebaseToken with a version long life, this will\neffectively be forever. Shared_prefs survive an application update\nand depending on how backup is configured on a device, it might survive\nan application removal and reinstallation.\nNormally this is not a problem, however if we change the credentials\nused, for example the App author is switching from one Firebase account\nto another, or invalided their firebase.secret, this cached credential\nis invalid, but will continue to be used, which results in errors.\nThis function permits us to unauthenticate, which tosses the cached\ncredentials. The next time authentication is needed we will use our\ncurrent FirebaseToken and get fresh credentials.\n'}]}

    def __init__(self, /, *, parent: Component=..., DeveloperBucket: str=..., FirebaseToken: str=..., FirebaseURL: str=..., Persist: bool=..., ProjectBucket: str=...):
        raise NotImplementedError

    @property
    def ProjectBucket(self) -> str:
        """Getter for the ProjectBucket."""
        raise NotImplementedError

    @ProjectBucket.setter
    def ProjectBucket(self, value: str, /) -> None:
        raise NotImplementedError

    def AppendValue(self, tag: str, valueToAdd: Any, /) -> None:
        """Append a value to the end of a list atomically. If two devices use this function simultaneously, both will be appended and no data lost."""
        raise NotImplementedError

    def ClearTag(self, tag: str, /) -> None:
        """Asks Firebase to forget (delete or set to "null") a given tag."""
        raise NotImplementedError

    def GetTagList(self, /) -> None:
        """Get the list of tags for this application. When complete a "TagList" event will be triggered with the list of known tags."""
        raise NotImplementedError

    def GetValue(self, tag: str, valueIfTagNotThere: Any, /) -> None:
        """GetValue asks Firebase to get the value stored under the given tag.
It will pass valueIfTagNotThere to GotValue if there is no value stored
under the tag."""
        raise NotImplementedError

    def RemoveFirst(self, tag: str, /) -> None:
        """Return the first element of a list and atomically remove it. If two devices use this function simultaneously, one will get the first element and the the other will get the second element, or an error if there is no available element. When the element is available, the "FirstRemoved" event will be triggered."""
        raise NotImplementedError

    def StoreValue(self, tag: str, valueToStore: Any, /) -> None:
        """Asks Firebase to store the given value under the given tag."""
        raise NotImplementedError

    def Unauthenticate(self, /) -> None:
        """Unauthenticate from Firebase.

   Firebase keeps track of credentials in a cache in shared_prefs
It will re-use these credentials as long as they are valid. Given
That we retrieve a FirebaseToken with a version long life, this will
effectively be forever. Shared_prefs survive an application update
and depending on how backup is configured on a device, it might survive
an application removal and reinstallation.
Normally this is not a problem, however if we change the credentials
used, for example the App author is switching from one Firebase account
to another, or invalided their firebase.secret, this cached credential
is invalid, but will continue to be used, which results in errors.
This function permits us to unauthenticate, which tosses the cached
credentials. The next time authentication is needed we will use our
current FirebaseToken and get fresh credentials.
"""
        raise NotImplementedError

    def on_DataChanged(self, callback: Callable[[str, Any], None], /) -> None:
        """DataChanged(tag, value)

Indicates that the data in the Firebase has changed.
Launches an event with the tag and value that have been updated."""
        raise NotImplementedError

    @staticmethod
    def on_any_DataChanged(callback: Callable[['FirebaseDB', bool, str, Any], None], /) -> None:
        """DataChanged(tag, value)

Indicates that the data in the Firebase has changed.
Launches an event with the tag and value that have been updated."""
        raise NotImplementedError

    def on_FirebaseError(self, callback: Callable[[str], None], /) -> None:
        """FirebaseError(message)

Indicates that the communication with the Firebase signaled an error."""
        raise NotImplementedError

    @staticmethod
    def on_any_FirebaseError(callback: Callable[['FirebaseDB', bool, str], None], /) -> None:
        """FirebaseError(message)

Indicates that the communication with the Firebase signaled an error."""
        raise NotImplementedError

    def on_FirstRemoved(self, callback: Callable[[Any], None], /) -> None:
        """FirstRemoved(value)

Event triggered by the "RemoveFirst" function. The argument "value" is the object that was the first in the list, and which is now removed."""
        raise NotImplementedError

    @staticmethod
    def on_any_FirstRemoved(callback: Callable[['FirebaseDB', bool, Any], None], /) -> None:
        """FirstRemoved(value)

Event triggered by the "RemoveFirst" function. The argument "value" is the object that was the first in the list, and which is now removed."""
        raise NotImplementedError

    def on_GotValue(self, callback: Callable[[str, Any], None], /) -> None:
        """GotValue(tag, value)

Indicates that a GetValue request has succeeded."""
        raise NotImplementedError

    @staticmethod
    def on_any_GotValue(callback: Callable[['FirebaseDB', bool, str, Any], None], /) -> None:
        """GotValue(tag, value)

Indicates that a GetValue request has succeeded."""
        raise NotImplementedError

    def on_TagList(self, callback: Callable[[list], None], /) -> None:
        """TagList(value)

Event triggered when we have received the list of known tags. Used with the "GetTagList" Function."""
        raise NotImplementedError

    @staticmethod
    def on_any_TagList(callback: Callable[['FirebaseDB', bool, list], None], /) -> None:
        """TagList(value)

Event triggered when we have received the list of known tags. Used with the "GetTagList" Function."""
        raise NotImplementedError

class ImageBot(Component):
    """The ImageBot is a non-visible component that uses DALL-E 2 to create and edit images. You must
supply your own OpenAI API key for this component by setting its ApiKey property in the blocks."""
    __data__ = {'desc': 'The ImageBot is a non-visible component that uses DALL-E 2 to create and edit images. You must\nsupply your own OpenAI API key for this component by setting its ApiKey property in the blocks.', 'properties': [{'name': 'ApiKey', 'type': 'str', 'ro': False, 'do': False, 'bo': True, 'desc': 'Specifies the ApiKey used to authenticate with the ImageBot.'}, {'name': 'InvertMask', 'type': 'bool', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies whether the mask used for editing should have its alpha channel inverted.'}, {'name': 'Size', 'type': 'int', 'ro': False, 'do': False, 'bo': False, 'desc': 'Specifies the size of the generated image. Can be one of 256, 512, or 1024.'}, {'name': 'Token', 'type': 'str', 'ro': False, 'do': False, 'bo': False, 'desc': 'The MIT Access token to use. MIT App Inventor will automatically fill this\nvalue in. You should not need to change it.'}], 'events': [{'name': 'ErrorOccurred', 'args': [{'name': 'responseCode', 'type': 'int'}, {'name': 'responseText', 'type': 'str'}], 'desc': 'The ErrorOccurred event will be run when an error occurs during processing, such as if you\nforget to provide an API key or the server is overloaded.'}, {'name': 'ImageCreated', 'args': [{'name': 'fileName', 'type': 'str'}], 'desc': 'The ImageCreated event will be run when the ImageBot successfully creates an image.'}, {'name': 'ImageEdited', 'args': [{'name': 'fileName', 'type': 'str'}], 'desc': 'The ImageCreated event will be run when the ImageBot successfully edits an image.'}], 'methods': [{'name': 'CreateImage', 'args': [{'name': 'description', 'type': 'str'}], 'returns': None, 'desc': 'Create an image using the given description.'}, {'name': 'EditImage', 'args': [{'name': 'source', 'type': 'Any'}, {'name': 'description', 'type': 'str'}], 'returns': None, 'desc': 'Edit the source image using the given description. Editable areas of the image should have\na transparent alpha. The source can be a Canvas component, an Image component, or a string\nrepresenting the path to a file.'}, {'name': 'EditImageWithMask', 'args': [{'name': 'imageSource', 'type': 'Any'}, {'name': 'maskSource', 'type': 'Any'}, {'name': 'prompt', 'type': 'str'}], 'returns': None, 'desc': 'Edit the imageSource using the given description. The editable area of the image should be\nindicated by the maskSource. The sources can be a Canvas, an Image, or a string\nrepresenting the path to a file.'}]}

    def __init__(self, /, *, parent: Component=..., InvertMask: bool=..., Size: int=..., Token: str=...):
        raise NotImplementedError

    @property
    def ApiKey(self) -> str:
        """Specifies the ApiKey used to authenticate with the ImageBot."""
        raise NotImplementedError

    @ApiKey.setter
    def ApiKey(self, value: str, /) -> None:
        raise NotImplementedError

    @property
    def InvertMask(self) -> bool:
        """Specifies whether the mask used for editing should have its alpha channel inverted."""
        raise NotImplementedError

    @InvertMask.setter
    def InvertMask(self, value: bool, /) -> None:
        raise NotImplementedError

    @property
    def Size(self) -> int:
        """Specifies the size of the generated image. Can be one of 256, 512, or 1024."""
        raise NotImplementedError

    @Size.setter
    def Size(self, value: int, /) -> None:
        raise NotImplementedError

    @property
    def Token(self) -> str:
        """The MIT Access token to use. MIT App Inventor will automatically fill this
value in. You should not need to change it."""
        raise NotImplementedError

    @Token.setter
    def Token(self, value: str, /) -> None:
        raise NotImplementedError

    def CreateImage(self, description: str, /) -> None:
        """Create an image using the given description."""
        raise NotImplementedError

    def EditImage(self, source: Any, description: str, /) -> None:
        """Edit the source image using the given description. Editable areas of the image should have
a transparent alpha. The source can be a Canvas component, an Image component, or a string
representing the path to a file."""
        raise NotImplementedError

    def EditImageWithMask(self, imageSource: Any, maskSource: Any, prompt: str, /) -> None:
        """Edit the imageSource using the given description. The editable area of the image should be
indicated by the maskSource. The sources can be a Canvas, an Image, or a string
representing the path to a file."""
        raise NotImplementedError

    def on_ErrorOccurred(self, callback: Callable[[int, str], None], /) -> None:
        """ErrorOccurred(responseCode, responseText)

The ErrorOccurred event will be run when an error occurs during processing, such as if you
forget to provide an API key or the server is overloaded."""
        raise NotImplementedError

    @staticmethod
    def on_any_ErrorOccurred(callback: Callable[['ImageBot', bool, int, str], None], /) -> None:
        """ErrorOccurred(responseCode, responseText)

The ErrorOccurred event will be run when an error occurs during processing, such as if you
forget to provide an API key or the server is overloaded."""
        raise NotImplementedError

    def on_ImageCreated(self, callback: Callable[[str], None], /) -> None:
        """ImageCreated(fileName)

The ImageCreated event will be run when the ImageBot successfully creates an image."""
        raise NotImplementedError

    @staticmethod
    def on_any_ImageCreated(callback: Callable[['ImageBot', bool, str], None], /) -> None:
        """ImageCreated(fileName)

The ImageCreated event will be run when the ImageBot successfully creates an image."""
        raise NotImplementedError

    def on_ImageEdited(self, callback: Callable[[str], None], /) -> None:
        """ImageEdited(fileName)

The ImageCreated event will be run when the ImageBot successfully edits an image."""
        raise NotImplementedError

    @staticmethod
    def on_any_ImageEdited(callback: Callable[['ImageBot', bool, str], None], /) -> None:
        """ImageEdited(fileName)

The ImageCreated event will be run when the ImageBot successfully edits an image."""
        raise NotImplementedError