from py2ai.magic import *
from py2ai.components import *

Screen1 = Form(BigDefaultText=True)
Spacing1 = HorizontalArrangement(Height=10, Width=-2)
LimitRow = HorizontalArrangement(AlignVertical=2, Width=-2)
LimitLabel = Label(parent=LimitRow, FontBold=True, Width=100, Text='Limit')
MinusButton = Button(parent=LimitRow, Width=48, Text='-')
LimitInput = TextBox(
    parent=LimitRow, Height=-2, Width=-2, NumbersOnly=True, Text='60', TextAlignment=1
)
AddButton = Button(parent=LimitRow, Width=48, Text='+')
CounterLabel = Label(FontSize=100, Width=-2, Text='0000', TextAlignment=1)
ResetButton = Button(FontSize=70, Height=240, Width=-2, Text='Start')
PauseButton = Button(Height=100, Width=-2, Text='Pause/Resume', Visible=False)
OptionsRow = HorizontalArrangement(AlignVertical=2, Width=-2)
OptionsLabel = Label(parent=OptionsRow, FontBold=True, Width=100, Text='Options')
VibrateCheckbox = CheckBox(parent=OptionsRow, Checked=True, Width=-2, Text='Vibrate')
BeepCheckbox = CheckBox(parent=OptionsRow, Checked=True, Width=-2, Text='Beep')
Sound1 = Sound(Source='beep.wav')
Clock1 = Clock(TimerEnabled=False)


def limit_sub():
    LimitInput.Text = str(max(int(LimitInput.Text) - 15, 0))


def limit_add():
    LimitInput.Text = str(int(LimitInput.Text) + 15)


def reset():
    ResetButton.Text = 'Reset'
    Clock1.TimerEnabled = True
    PauseButton.Visible = True
    CounterLabel.Text = '0000'


def pause():
    Clock1.TimerEnabled = not Clock1.TimerEnabled


def tick():
    tim = int(CounterLabel.Text) + 1
    if tim >= int(LimitInput.Text):
        if BeepCheckbox.Checked:
            Sound1.Play()
        if VibrateCheckbox.Checked:
            Sound1.Vibrate(500)
    if tim < 10:
        CounterLabel.Text = '000' + str(tim)
    elif tim < 100:
        CounterLabel.Text = '00' + str(tim)
    elif tim < 1000:
        CounterLabel.Text = '0' + str(tim)
    else:
        CounterLabel.Text = str(tim)


MinusButton.on_Click(limit_sub)
AddButton.on_Click(limit_add)
ResetButton.on_Click(reset)
PauseButton.on_Click(pause)
Clock1.on_Timer(tick)
