import time
import cv2
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.graphics.texture import Texture

Window.size = (310, 670)

class LoadingPage(Screen):
    pass

class HomeMenu(Screen):
    pass

class FirstAidMenu1(Screen):
    pass

class FirstAidMenu2(Screen):
    pass

class CameraMenu(Screen):
    pass

class BruisePage(Screen):
    pass

class AbrasionPage(Screen):
    pass

class BurnPage(Screen):
    pass

class MinorWoundPage(Screen):
    pass

class BleedingPage(Screen):
    pass

class SprainPage(Screen):
    pass

class MappingMenu(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

class WindowManager(ScreenManager):
    pass

file=Builder.load_file('FirstAidResponder.kv')

class FirstAidApp(App):
   def build(self):
        return file
    
FirstAidApp().run()
