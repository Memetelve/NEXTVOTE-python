import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class SettingsPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text="Champion Id's"))
        self.champions = TextInput(multiline=False)
        self.add_widget(self.champions)

        self.add_widget(Label(text="Stop when game starts"))
        self.stopWhenMatchStarts = TextInput(multiline=False)
        self.add_widget(self.stopWhenMatchStarts)

        self.add_widget(Label(text="Lock champion"))
        self.championLock = TextInput(multiline=False)
        self.add_widget(self.championLock)

        self.save = Button(text="Save")
        self.add_widget(Label())
        self.add_widget(self.save)


class NEXTVOTEApp(App):
    def build(self):
        return SettingsPage()

if __name__ == '__main__':
    NEXTVOTEApp().run()
