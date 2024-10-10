from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

Config.set('graphics', 'Resizable','0')
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '650')


class LoadingPage(Screen):
    pass

class HomeMenu(Screen):
    pass
    
class CameraMenu(Screen):
    pass

class FirstAidMenu(Screen):
    pass

class Q3(Screen):
    pass

class FinalPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

file=Builder.load_file('FirstAidResponder.kv')

class FirstAidApp(App):
    def build(self):
        return file

FirstAidApp().run()
